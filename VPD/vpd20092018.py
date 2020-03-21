import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset as Ncdf
from netCDF4 import num2date
import datetime
from mpl_toolkits.basemap import Basemap
import matplotlib

matplotlib.use("Agg")
nc = Ncdf('VPD_monthly_mean_d02_2009-2018.nc', 'r')
print(nc)
for i in nc.variables:
    print(i, nc.variables[i].units, nc.variables[i].shape)
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]
time = nc.variables['time'][:]
vpd = nc.variables['VPD'][:]
t_units = nc.variables['time'].units
datevar = num2date(time[:], units='hours since 1970-01-01 00:00:00', calendar='standard')
print(datevar[:])
map = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
              resolution='i')

lon2, lat2 = np.meshgrid(lons, lats)
x, y = map(lon2, lat2)
my_cmap = plt.get_cmap('rainbow_r')
plt.gca().set_axis_off()
plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                    hspace=0, wspace=0)
plt.margins(0, 0)
map.pcolormesh(x, y, vpd[0, :, :], cmap='rainbow_r')
plt.colorbar(label="Vapor Pressure Deficit (hPa)")
for b in range(0, 31):
    map.pcolormesh(x, y, vpd[b, :, :], cmap='rainbow_r')
    plt.title('Vapor Pressure Deficit on %s' % datevar[b])
    # cb = plt.colorbar();
    # cb.remove();
    # plt.draw();
    plt.savefig("VPD_monthly_mean_d02_2009-2018_%s.png" % b, transparent='True',
                bbox_inches='tight', pad_inches=0)
    print('saved %s' % b)