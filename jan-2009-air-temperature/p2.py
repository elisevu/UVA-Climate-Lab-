import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset as Ncdf
from netCDF4 import num2date, date2num
import datetime
from mpl_toolkits.basemap import Basemap
import matplotlib
matplotlib.use("Agg")
nc = Ncdf('ta_2m_1hr_20090101_d02.nc', 'r')
next = Ncdf("ta_max_1day.nc", 'r')
print(next.variables["max temp"][:])
#print(nc)
# for i in nc.variables:
#     print(i, nc.variables[i].units, nc.variables[i].shape)
#     print(nc.dimensions)
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]
time = nc.variables['time'][:]
t2 = nc.variables['ta_2m'][:]
t_units = nc.variables['time'].units
datevar = num2date(time[:], units='hours since 1970-01-01 00:00:00', calendar='standard')

another = Ncdf("ta_over_35.nc", "w", format="NETCDF4")
day_dim = another.createDimension("days over 35")
lat_dim = another.createDimension("lat")
lon_dim = another.createDimension("lon")
day = another.createVariable("day", "u1", ("days over 35",))
another_latitude = another.createVariable("lat", 'f4', ("lon",))
another_longitude = another.createVariable("lon", 'f4', ("lat",))
another_longitude[:] = lons[:]
another_latitude[:] = lats[:]
day.units = "days since 2009-01-01 00:00:00"
dates = []
count = 0
for j in range(1, len(t2[:][:][:][:])-2):
    print(j)
    for k in range(1, len(t2[:][:][:][j])-2):
        for d in range(1, len(t2[:][:][k][j])-2):
            current = int(datevar[d].day)
            t = t2[:][d][k][j] - 273.15
            if t >= 35.0:
                count += 1

        dates.append(count)
day[:] = dates
nc.close()
another.close()
print("done")
quit()

