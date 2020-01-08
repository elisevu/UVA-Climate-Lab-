import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset as Ncdf
from netCDF4 import num2date, date2num
import datetime
from mpl_toolkits.basemap import Basemap
import matplotlib

matplotlib.use("Agg")
max = Ncdf("ta_max_1day.nc", "r")
print(max)
max_latitude = max.variables["lat"][:]
max_longitude = max.variables["lon"][:]
max_temps = max.variables["max temp"][:]
days = max.variables["day"][:]
datevar = num2date(days[:], units='hours since 1970-01-01 00:00:00', calendar='standard')
avg = 0
for j in range(0, 599):
    for k in range(0, 698):
        for d in range(0, len(days[:])):
            avg += max_temps[:][d][k][j]
        if j % 25 == 0 & k % 25 == 0:
            domain = []
            fig = plt.figure()
            ax = plt.axes()
            ax.plot(datevar, avg)
            plt.show()
max.close()
print("done")
quit()