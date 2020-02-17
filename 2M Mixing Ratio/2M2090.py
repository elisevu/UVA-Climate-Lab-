import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from netCDF4 import Dataset as Ncdf
from netCDF4 import num2date
import datetime
from mpl_toolkits.basemap import Basemap
import matplotlib

matplotlib.use("Agg")
nc = Ncdf('qv_2m_monthly_mean_d02_2009-2018.nc', 'r')
nc55 = Ncdf('qv_2m_monthly_mean_d02_2090-2099.nc', 'r')
print(nc)
for i in nc.variables:
    print(i, nc.variables[i].units, nc.variables[i].shape)
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]
time = nc.variables['time'][:]
qv2m = nc.variables['qv_2m'][:]

lons55 = nc55.variables['lon'][:]
lats55 = nc55.variables['lat'][:]
time55 = nc55.variables['time'][:]
qv2m55 = nc55.variables['qv_2m'][:]

diff55 = qv2m55

for j in range(0, 12):
    print(j)
    for k in range(0, 699):
        for d in range(0, 600):
            diff55[j, k, d] = qv2m55[j, k, d] - qv2m[j, k, d]
            

t_units = nc.variables['time'].units
datevar = num2date(time55[:], units='hours since 1970-01-01 00:00:00', calendar='standard')
print(datevar[:])
map = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
              resolution='i')

lon2, lat2 = np.meshgrid(lons, lats)
x, y = map(lon2, lat2)
my_cmap = plt.get_cmap('RdBu_r')
plt.gca().set_axis_off()
plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                    hspace=0, wspace=0)
plt.margins(0, 0)
map.pcolormesh(x, y, diff55[0, :, :], cmap='RdBu_r', vmax = 0.0040, vmin = -0.0040)
#plt.colorbar(label="2-m Mixing Ratio")
for b in range(0, 31):
    map.pcolormesh(x, y, diff55[b, :, :], cmap='RdBu_r')
    #plt.title('Difference In 2-m Mixing Ratio From 2009-2018 to %s' % datevar[b])
    cb = plt.colorbar();
    cb.remove();
    plt.draw();
    plt.savefig("qv_2m_monthly_mean_d02_2090-2099_%s.png" % b, transparent='True',
                bbox_inches='tight', pad_inches=0)
    print('saved %s' % b)