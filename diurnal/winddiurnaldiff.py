import numpy as np

import matplotlib.pyplot as plt
from netCDF4 import Dataset as Ncdf
import matplotlib.colors as colors
from mpl_toolkits.basemap import Basemap
import matplotlib

matplotlib.use("Agg")
ua = Ncdf('ua_10m_diurnal_mean_d02_2009-2018.nc', 'r')
va = Ncdf('va_10m_diurnal_mean_d02_2009-2018.nc', 'r')
ua55 = Ncdf('ua_10m_diurnal_mean_d02_2055-2064.nc', 'r')
va55 = Ncdf('va_10m_diurnal_mean_d02_2055-2064.nc', 'r')
ua90 = Ncdf('ua_10m_diurnal_mean_d02_2090-2099.nc', 'r')
va90 = Ncdf('va_10m_diurnal_mean_d02_2090-2099.nc', 'r')
print(ua55)
lons = ua.variables['lon'][:]
lats = ua.variables['lat'][:]

time = ua.variables['time'][:]
u10 = np.array(ua.variables['ua_10m'][:])
v10 = np.array(va.variables['va_10m'][:])
ws = np.sqrt(u10[:] ** 2 + v10[:] ** 2)

u55 = np.array(ua55.variables['ua_10m'][:])
v55 = np.array(va55.variables['va_10m'][:])
ws55 = np.sqrt(u55[:] ** 2 + v55[:] ** 2)

u90 = np.array(ua90.variables['ua_10m'][:])
v90 = np.array(va90.variables['va_10m'][:])
ws90 = np.sqrt(u90[:] ** 2 + v90[:] ** 2)

diff55 = ws
diff90 = ws
diffua55 = u55
diffva55 = v55
diffua90 = u90
diffva90 = v90

for j in range(0, 24):
    print(j)
    for k in range(0, 699):
        for d in range(0, 600):
            diff55[j, k, d] = ws55[j, k, d] - ws[j, k, d]
            diff90[j, k, d] = ws90[j, k, d] - ws[j, k, d]
            diffua55[j, k, d] = u55[j, k, d] - u10[j, k, d]
            diffva55[j, k, d] = v55[j, k, d] - v10[j, k, d]
            diffua90[j, k, d] = u90[j, k, d] - u10[j, k, d]
            diffva90[j, k, d] = v90[j, k, d] - v10[j, k, d]
print("wind speed")
print(np.amax(ws))
print(np.amin(ws))
print("wind speed diff")
print(np.amin(diff55), np.amax(diff55))
print(np.amin(diff90), np.amax(diff90))
print("wind direction u 55")
print(np.amin(diffua55), np.amax(diffua55))
print("wind direction u 90")
print(np.amin(diffua90), np.amax(diffua90))
print("wind direction v 55")
print(np.amin(diffva55), np.amax(diffva55))
print("wind direction v 90")
print(np.amin(diffva90), np.amax(diffva90))

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


cmap2 = truncate_colormap(cmap, 0.0, 1.0)

map.pcolormesh(x, y, diff55[0, :, :], cmap='bwr', vmin=-13, vmax=13)
plt.colorbar(label="Wind Speed and Direction m/s")
qd5 = plt.quiver(x[::20, ::20], y[::20, ::20], diffua55[0, ::20, ::20], diffva55[0, ::20, ::20], color="black")
qk5 = plt.quiverkey(qd5, 0.7, 0.95, 1, r'$2 \frac{m}{s}$', labelpos='E', coordinates='figure')
plt.savefig("wind_diurnal_diff_2055_2064/wind_diurnal_diff_2055-2064_KEY.png",
            transparent='True', bbox_inches='tight', pad_inches=0)
print('saved diff 55 key')
plt.clf()

map.pcolormesh(x, y, diff90[0, :, :], cmap='bwr', vmin=-13, vmax=13)
plt.colorbar(label="Wind Speed and Direction m/s")
qd9 = plt.quiver(x[::20, ::20], y[::20, ::20], diffua90[0, ::20, ::20], diffva90[0, ::20, ::20], color="black")
qk9 = plt.quiverkey(qd9, 0.7, 0.95, 1, r'$2 \frac{m}{s}$', labelpos='E', coordinates='figure')
plt.savefig("wind_diurnal_diff_2090_2099/wind_diurnal_diff_2090-2099_KEY.png",
            transparent='True', bbox_inches='tight', pad_inches=0)
plt.clf()
print('saved diff 90 key')

for b in range(0, 24):
    map.pcolormesh(x, y, diff55[b, :, :], cmap='bwr', vmin=-13, vmax=13)
    qd5 = plt.quiver(x[::20, ::20], y[::20, ::20], diffua55[b, ::20, ::20], diffva55[b, ::20, ::20], color="black")
    plt.savefig("wind_diurnal_diff_2055_2064/wind_diurnal_diff_2055-2064_%s.png" % b,
                transparent='True', bbox_inches='tight', pad_inches=0)
    print('saved diff 55 %s' % b)
    plt.clf()
    map.pcolormesh(x, y, diff90[b, :, :], cmap='bwr', vmin=-13, vmax=13)
    qd9 = plt.quiver(x[::20, ::20], y[::20, ::20], diffua90[b, ::20, ::20], diffva90[b, ::20, ::20], color="black")
    plt.savefig("wind_diurnal_diff_2090_2099/wind_diurnal_diff_2090-2099_%s.png" % b,
                transparent='True', bbox_inches='tight', pad_inches=0)
    print('saved diff 90 %s' % b)
    plt.clf()

