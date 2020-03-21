import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset as Ncdf
from mpl_toolkits.basemap import Basemap
import matplotlib
from netCDF4 import num2date

matplotlib.use("Agg")
nc = Ncdf('daily_temperature_month_d02_2009-2018.nc', 'r')
n90 = Ncdf('daily_temperature_month_d02_2090-2099.nc', 'r')

month = nc.variables['month'][:]
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]

month90 = nc.variables['month'][:]
lons90 = nc.variables['lon'][:]
lats90 = nc.variables['lat'][:]

datevar = num2date(month[:], units='hours since 1970-01-01 00:00:00', calendar='standard')
print(datevar[:])

temp_max_daily = nc.variables['Tmax_daily'][:]
temp90_max_daily = n90.variables['Tmax_daily'][:]

# temp_min_daily = nc.variables['Tmin_daily'][:]
# temp90_min_daily = n90.variables['Tmin_daily'][:]

# temp_mean_daily = nc.variables['Tmean_daily'][:]
# temp90_mean_daily = n90.variables['Tmean_daily'][:]

# temp_min_daily_c = temp_min_daily
# temp90_min_daily_c = temp90_min_daily

temp_max_daily_c = temp_max_daily
temp90_max_daily_c = temp90_max_daily

# temp_mean_daily_c = temp_mean_daily
# temp90_mean_daily_c = temp90_mean_daily

diff = temp_max_daily

# for i in range(0, 12):
#     print(i)
#     for j in range(0, 699):
#         for k in range(0, 600):
#             temp_max_daily_c[i,j,k] = temp_max_daily[i,j,k] - 273.15
#             temp90_max_daily_c[i,j,k] = temp90_max_daily[i,j,k] - 273.15
#             diff[i,j,k] = temp90_max_daily_c[i,j,k] - temp_max_daily_c[i,j,k]
#             if diff[i,j,k] < 0.55:
#                 print(diff[i,j,k])

# temp_min = 6896876
# temp_max = -3536533
# for i in range(0, 12):
#     print(i)
#     for j in range(0, 699):
#         for k in range(0, 600):
#             if diff[i,j,k] < temp_min:
#                 temp_min = diff[i,j,k]
#             if diff[i,j,k] > temp_max:
#                 temp_max = diff[i,j,k]
# print(temp_min)
# print(temp_max)

# map = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
#               resolution='i')

# lon2, lat2 = np.meshgrid(lons, lats)
# x, y = map(lon2, lat2)

# plt.figure(figsize=(601/100, 700/100))
# my_cmap = plt.get_cmap('bwr')
# plt.gca().set_axis_off()
# plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
# plt.margins(0, 0)

# # map.pcolormesh(x, y, diff[0, :, :], cmap='bwr', vmin=-6, vmax=6)
# # plt.colorbar(label="Temperature (Celsius)")

# for b in range(0, 12):
#     map.pcolormesh(x, y, diff[b, :, :], cmap='bwr', vmin=-6, vmax=6)   
#     # plt.title('Daily Mean Temperature Difference for Month %s' % month[b])
#     plt.savefig("temp_mean_daily_diff_2090-2099_%s.png" % b, transparent='True',
#                   bbox_inches='tight', pad_inches=0)
#     print('saved %s' % b)