import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from netCDF4 import Dataset as Ncdf
from netCDF4 import num2date
from mpl_toolkits.basemap import Basemap
import matplotlib

matplotlib.use("Agg")
nc = Ncdf('precip_exc_freq_d02_2009-2018.nc', 'r')
print(nc)
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]
month = nc.variables['month'][:]
mean = nc.variables['mean_daily_precip'][:]
max = -478324
min = 7489324
for j in range(0, 12):
    print(j)
    for k in range(0, 699):
        for d in range(0, 600):
            if mean[j, k, d] >= max:
                max = mean[j, k, d]
            if mean[j, k, d] <= min:
                min = mean[j, k, d]
print(max)
print(min)

mapp = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
               resolution='i')
lon2, lat2 = np.meshgrid(lons, lats)
x, y = mapp(lon2, lat2)
plt.figure(figsize=(601 / 100, 700 / 100))
plt.gca().set_axis_off()
plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                    hspace=0, wspace=0)
plt.margins(0, 0)
cmap = plt.get_cmap('gist_rainbow_r')


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=117):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    new_cmap.set_under('white')  # 1.0 represents not transparent
    new_cmap.set_bad('white')
    return new_cmap


cmap2 = truncate_colormap(cmap, 0.08, 1.0)
# plt.title('Daily Precip Mean over Month of X')
for b in range(0, 12):
    mapp.pcolormesh(x, y, mean[b, :, :], cmap=cmap2, vmin=0, vmax=117)
    # plt.title('2m Temperature on %s' % datevar[b])
    plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/precip_monthly_mean_2009-2018_%s.png" % b, transparent='True',
                bbox_inches='tight', pad_inches=0)
    print('saved %s' % b)
    plt.clf()
mapp.pcolormesh(x, y, mean[1, :, :], cmap=cmap2, vmin=0, vmax=117)
plt.colorbar(label="Mean Rainfall Rate (mm/day)")
plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/precip_monthly_mean_2009-2018_KEY.png", transparent='True',
            bbox_inches='tight', pad_inches=0)
