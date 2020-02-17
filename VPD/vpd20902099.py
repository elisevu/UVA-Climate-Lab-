import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from netCDF4 import Dataset as Ncdf
from netCDF4 import num2date
import datetime
from mpl_toolkits.basemap import Basemap
import matplotlib

matplotlib.use("Agg")
nc = Ncdf('VPD_monthly_mean_d02_2009-2018.nc', 'r')
nc99 = Ncdf('VPD_monthly_mean_d02_2090-2099.nc', 'r')
print(nc)
for i in nc.variables:
    print(i, nc.variables[i].units, nc.variables[i].shape)
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]
time = nc.variables['time'][:]
vpd = nc.variables['VPD'][:]

lons99 = nc99.variables['lon'][:]
lats99 = nc99.variables['lat'][:]
time99 = nc99.variables['time'][:]
vpd99 = nc99.variables['VPD'][:]

diff99 = vpd99

for j in range(0, 12):
    print(j)
    for k in range(0, 699):
        for d in range(0, 600):
            diff99[j, k, d] = vpd99[j, k, d] - vpd[j, k, d]
            

t_units = nc.variables['time'].units
datevar = num2date(time99[:], units='hours since 1970-01-01 00:00:00', calendar='standard')
print(datevar[:])
map = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
              resolution='i')

lon2, lat2 = np.meshgrid(lons, lats)
x, y = map(lon2, lat2)
my_cmap = plt.get_cmap('rainbow')
plt.gca().set_axis_off()
plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                    hspace=0, wspace=0)
plt.margins(0, 0)
map.pcolormesh(x, y, diff99[0, :, :], cmap='RdBu_r', vmax = 8, vmin = -8)
#plt.colorbar(label="Vapor Pressure Deficit (hPa)")
for b in range(0, 31):
    map.pcolormesh(x, y, diff99[b, :, :], cmap='RdBu_r')
    #plt.title('Difference In Vapor Pressure Deficit From 2009-2018 to %s' % datevar[b])
    cb = plt.colorbar();
    cb.remove();
    plt.draw();
    plt.savefig("VPD_monthly_mean_d02_2090-2099_%s.png" % b, transparent='True',
                bbox_inches='tight', pad_inches=0)
    print('saved %s' % b)