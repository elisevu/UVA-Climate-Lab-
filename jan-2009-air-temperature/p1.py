import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset as Ncdf
from netCDF4 import num2date, date2num
import datetime
from mpl_toolkits.basemap import Basemap
import matplotlib

matplotlib.use("Agg")
nc = Ncdf('ta_2m_1hr_20090101_d02.nc', 'r')
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
another = Ncdf("ta_max_1day.nc", "w", format="NETCDF4")
temp_dim = another.createDimension("max temp")
day_dim = another.createDimension("days in jan")
lat_dim = another.createDimension("lat")
lon_dim = another.createDimension("lon")
temp = another.createVariable("max temp", 'f4', ("max temp",))
day = another.createVariable("day", "u1", ("days in jan",))
another_latitude = another.createVariable("lat", 'f4', ("lon",))
another_longitude = another.createVariable("lon", 'f4', ("lat",))
another_longitude[:] = lons[:]
another_latitude[:] = lats[:]
day.units = "days since 2009-01-01 00:00:00"
temp.units = "Celsius"
temps = []
days = []
maxi = -100000
prev = 0
print(prev)
print(another)
print(t2[:][0][0][0])
for j in range(0, 599):
    print(j)
    for k in range(0, 698):
        for d in range(0, len(t2[:][:][k][j])-1):
            dayy = int(datevar[d].day)
            if t2[:][d][k][j] >= maxi:
                maxi = round(t2[:][d][k][j] - 273.15, 1)
                #print(maxi)
            if dayy > prev or (dayy == 1 and prev == 31):
                # print(maxi)
                temps.append(maxi)
                days.append(dayy)
            prev = dayy
temp[:] = temps
day[:] = days
nc.close()
another.close()
print("done")
quit()