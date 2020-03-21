import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset as Ncdf
from netCDF4 import num2date
from mpl_toolkits.basemap import Basemap
import matplotlib

matplotlib.use("Agg")
nc = Ncdf('daily_temperature_month_d02_2055-2064.nc', 'r')
print(nc)

month = nc.variables['month'][:]
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]

# time = nc.variables['time'][:]
# t_units = nc.variables['time'].units

temp_max_daily = nc.variables['Tmax_daily'][:]
# temp_min_daily = nc.variables['Tmin_daily'][:]
# temp_mean_daily = nc.variables['Tmean_daily'][:]

temp_max_daily_c = temp_max_daily
# temp_min_daily_c = temp_min_daily
# temp_mean_daily_c = temp_mean_daily

for i in range(0, 12):
    print(i)
    for j in range(0, 699):
        for k in range(0, 600):
            temp_max_daily_c[i,j,k] = temp_max_daily[i,j,k] - 273.15
           # temp_min_daily_c[i, j, k] = temp_min_daily[i, j, k] - 273.15
           # temp_mean_daily_c[i, j, k] = temp_mean_daily[i, j, k] - 273.15

# temp_min = 0.0
# temp_max = 0.0
# for i in range(0, 12):
#     for j in range(0, 699):
#         for k in range(0, 600):
#             if temp_mean_daily_c[i, j, k] < temp_min:
#                 temp_min = temp_mean_daily_c[i, j, k]
#             if temp_mean_daily_c[i, j, k] > temp_max:
#                 temp_max = temp_mean_daily_c[i, j, k]
# print(temp_min)
# print(temp_max)



# datevar = num2date(time[:], units='hours since 1970-01-01 00:00:00', calendar='standard')
# print(datevar[:])
map = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
              resolution='i')

lon2, lat2 = np.meshgrid(lons, lats)
x, y = map(lon2, lat2)

plt.figure(figsize=(601/100, 700/100))
my_cmap = plt.get_cmap('rainbow')
plt.gca().set_axis_off()
plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                    hspace=0, wspace=0)
plt.margins(0, 0)
#map.pcolormesh(x, y, temp_min_daily_c[0, :, :], cmap='rainbow', vmin=-5, vmax=35)
#plt.colorbar(label="Temperature (Celsius)")
for b in range(0, 12):
      map.pcolormesh(x, y, temp_min_daily_c[b, :, :], cmap='rainbow')
      #plt.title('Daily Min Temperature for Month %s' % month[b])
      plt.savefig("temp_min_daily_%s.png" % b, transparent='True',
                  bbox_inches='tight', pad_inches=0)
      print('saved %s' % b)