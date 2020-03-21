import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset as Ncdf
from mpl_toolkits.basemap import Basemap
import matplotlib

matplotlib.use("Agg")
nc = Ncdf('daily_temperature_month_d02_2009-2018.nc', 'r')
nc55 = Ncdf('daily_temperature_month_d02_2055-2064.nc', 'r')

month = nc.variables['month'][:]
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]

month55 = nc.variables['month'][:]
lons55 = nc.variables['lon'][:]
lats55 = nc.variables['lat'][:]

# temp_max_daily = nc.variables['Tmax_daily'][:]
# temp55_max_daily = nc55.variables['Tmax_daily'][:]

# temp_min_daily = nc.variables['Tmin_daily'][:]
# temp55_min_daily = nc55.variables['Tmin_daily'][:]

temp_mean_daily = nc.variables['Tmean_daily'][:]
temp55_mean_daily = nc55.variables['Tmean_daily'][:]

# temp_min_daily_c = temp_min_daily
# temp55_min_daily_c = temp55_min_daily

# temp_max_daily_c = temp_max_daily
# temp55_max_daily_c = temp55_max_daily

temp_mean_daily_c = temp_mean_daily
temp55_mean_daily_c = temp55_mean_daily

diff = temp_mean_daily

for i in range(0, 12):
    print(i)
    for j in range(0, 699):
        for k in range(0, 600):
            temp_mean_daily_c[i,j,k] = temp_mean_daily[i,j,k] - 273.15
            temp55_mean_daily_c[i,j,k] = temp55_mean_daily[i,j,k] - 273.15
            diff[i,j,k] = temp55_mean_daily_c[i,j,k] - temp_mean_daily_c[i,j,k]
            # if diff[i,j,k] < 0.6:
            #     print(diff[i,j,k])

temp_min = 6896876
temp_max = -3536533
for i in range(0, 12):
    print(i)
    for j in range(0, 699):
        for k in range(0, 600):
            if diff[i,j,k] < temp_min:
                temp_min = diff[i,j,k]
            if diff[i,j,k] > temp_max:
                temp_max = diff[i,j,k]
print(temp_min)
print(temp_max)

# map = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
#               resolution='i')

# lon2, lat2 = np.meshgrid(lons, lats)
# x, y = map(lon2, lat2)

# plt.figure(figsize=(601/100, 700/100))
# my_cmap = plt.get_cmap('bwr')
# plt.gca().set_axis_off()
# plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
# plt.margins(0, 0)

# # map.pcolormesh(x, y, diff[0, :, :], cmap='bwr', vmin=-4, vmax=4)
# # plt.colorbar(label="Temperature (Celsius)")

# for b in range(0, 12):
#     map.pcolormesh(x, y, diff[b, :, :], cmap='bwr', vmin=-4, vmax=4 )   
#     # plt.title('Daily Mean Temperature Difference for Month %s' % month[b])
#     plt.savefig("temp_mean_daily_diff_2055-2064_%s.png" % b, transparent='True',
#                   bbox_inches='tight', pad_inches=0)
#     print('saved %s' % b)