import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from netCDF4 import Dataset as Ncdf
from mpl_toolkits.basemap import Basemap
import matplotlib

matplotlib.use("Agg")
nc = Ncdf('precip_exc_freq_d02_2009-2018.nc', 'r')
nc55 = Ncdf('precip_exc_freq_d02_2055-2064.nc', 'r')
nc90 = Ncdf('precip_exc_freq_d02_2090-2099.nc', 'r')
print(nc)
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]
month = nc.variables['month'][:]
mean = nc.variables['mean_daily_precip'][:]
lons55 = nc55.variables['lon'][:]
lats55 = nc55.variables['lat'][:]
month55 = nc55.variables['month'][:]
mean55 = nc55.variables['mean_daily_precip'][:]
diff55 = mean
lons90 = nc90.variables['lon'][:]
lats90 = nc90.variables['lat'][:]
month90 = nc90.variables['month'][:]
mean90 = nc90.variables['mean_daily_precip'][:]
diff90 = mean
max0 = -7432984
min0 = 74389247
max55 = -7432984
min55 = 74389247
max90 = -7432984
min90 = 74389247

for j in range(0, 12):
    print(j)
    for k in range(0, 699):
        for d in range(0, 600):
            diff55[j, k, d] = mean55[j, k, d] - mean[j, k, d]
            diff90[j, k, d] = mean90[j, k, d] - mean[j, k, d]
            print(diff55[j, k, d])
            if mean[j, k, d] >= max0:
                max0 = mean[j, k, d]
            elif mean[j, k, d] <= min0:
                min0 = mean[j, k, d]

            if diff55[j, k, d] >= max55:
                max55 = diff55[j, k, d]
            elif diff55[j, k, d] <= min55:
                min55 = diff55[j, k, d]

            if diff90[j, k, d] >= max90:
                max90 = diff90[j, k, d]
            elif diff90[j, k, d] <= min90:
                min90 = diff90[j, k, d]
print(max0)
print(min0)
print(max55)
print(min55)
print(max90)
print(min90)
# mapp = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
#                resolution='i')
# lon2, lat2 = np.meshgrid(lons, lats)
# x, y = mapp(lon2, lat2)
# plt.figure(figsize=(601 / 100, 700 / 100))
# plt.gca().set_axis_off()
# plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
#                     hspace=0, wspace=0)
# plt.margins(0, 0)
# cmap = plt.get_cmap('gist_rainbow_r')
#
#
# def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=117):
#     new_cmap = colors.LinearSegmentedColormap.from_list(
#         'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
#         cmap(np.linspace(minval, maxval, n)))
#     new_cmap.set_under('white')  # 1.0 represents not transparent
#     new_cmap.set_bad('white')
#     return new_cmap
#
#
# cmap2 = truncate_colormap(cmap, 0.08, 1.0)
# # plt.title('Daily Precip Mean over Month of X')
# for b in range(0, 12):
#     mapp.pcolormesh(x, y, mean[b, :, :], cmap=cmap2, vmin=0, vmax=117)
#     # plt.title('2m Temperature on %s' % datevar[b])
#     plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/precip_monthly_mean_2009-2018_%s.png" % b,
#                 transparent='True',
#                 bbox_inches='tight', pad_inches=0)
#     mapp.pcolormesh(x, y, diff55[b, :, :], cmap=cmap2, vmin=0, vmax=117)
#     plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/precip_monthly_diff_2055-2064_%s.png" % b,
#                 transparent='True',
#                 bbox_inches='tight', pad_inches=0)
#     mapp.pcolormesh(x, y, diff90[b, :, :], cmap=cmap2, vmin=0, vmax=117)
#     plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/precip_monthly_diff_2090-2099_%s.png" % b,
#                 transparent='True',
#                 bbox_inches='tight', pad_inches=0)
#     print('saved %s' % b)
#     plt.clf()
# mapp.pcolormesh(x, y, mean[1, :, :], cmap=cmap2, vmin=0, vmax=117)
# plt.colorbar(label="Mean Rainfall Rate (mm/day)")
# plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/precip_monthly_mean_2009-2018_KEY.png", transparent='True',
#             bbox_inches='tight', pad_inches=0)
# mapp.pcolormesh(x, y, diff55[1, :, :], cmap=cmap2, vmin=0, vmax=117)
# plt.colorbar(label="Difference in Mean Rainfall Rate (mm/day)")
# plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/precip_monthly_diff_2055-2064_KEY.png", transparent='True',
#             bbox_inches='tight', pad_inches=0)
# mapp.pcolormesh(x, y, diff90[1, :, :], cmap=cmap2, vmin=0, vmax=117)
# plt.colorbar(label="Difference in Mean Rainfall Rate (mm/day)")
# plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/precip_monthly_diff_2090-2099_KEY.png", transparent='True',
#             bbox_inches='tight', pad_inches=0)
