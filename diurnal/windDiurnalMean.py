import numpy as np

import matplotlib.pyplot as plt
from netCDF4 import Dataset as Ncdf
import matplotlib.colors as colors
from mpl_toolkits.basemap import Basemap
import matplotlib

matplotlib.use("Agg")
ua = Ncdf('ua_10m_diurnal_mean_d02_2009-2018.nc', 'r')
va = Ncdf('va_10m_diurnal_mean_d02_2009-2018.nc', 'r')
print(ua)
print(va)
for i in ua.variables:
    print(i, ua.variables[i].units, ua.variables[i].shape)
for x in va.variables:
    print(x, va.variables[x].units, va.variables[x].shape)
lons = ua.variables['lon'][:]
lats = ua.variables['lat'][:]
time = ua.variables['time'][:]
u10 = ua.variables['ua_10m'][:]
v10 = va.variables['va_10m'][:]
ws = np.sqrt(u10[:] ** 2 + v10[:] ** 2)

print(np.amax(ws))
print(np.amin(ws))

# datevar = num2date(time[:], units='hours since 1970-01-01 00:00:00', calendar='standard')
# print(datevar[:])
map = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
              resolution='i')
lon2, lat2 = np.meshgrid(lons, lats)
x, y = map(lon2, lat2)
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


cmap2 = truncate_colormap(cmap, 0.2, 1.0)

for b in range(0, 1):
    map.pcolormesh(x, y, ws[b, :, :], cmap=cmap2, vmin=0, vmax=15)
    plt.quiver(x, y, u10[b, :, :], v10[b, :, :], scale=500)
    # plt.title('2m Temperature on %s' % datevar[b])
    plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/wind_diurnal_mean_%s.png" % b, transparent='True',
                bbox_inches='tight', pad_inches=0)
    print('saved %s' % b)
    plt.clf()
map.pcolormesh(x, y, ws[0, :, :], cmap=cmap2, vmin=0, vmax=15)
plt.colorbar(label="Wind Speed and Direction m/s")
plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/wind_diurnal_mean_KEY.png", transparent='True',
            bbox_inches='tight', pad_inches=0)
