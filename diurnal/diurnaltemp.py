import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset as Ncdf
from netCDF4 import num2date
import datetime
from mpl_toolkits.basemap import Basemap
import matplotlib

matplotlib.use("Agg")
nc = Ncdf('ta_2m_diurnal_mean_d02_2009-2018.nc', 'r')
nc55 = Ncdf('ta_2m_diurnal_mean_d02_2055-2064.nc', 'r')
for i in nc.variables:
    print(i, nc.variables[i].units, nc.variables[i].shape)
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]
time = nc.variables['time'][:]
t2 = nc.variables['ta_2m'][:]
t_units = nc.variables['time'].units
temp_c = t2
for j in range(0, 23):
    print(j)
    for k in range(0, 698):
        for d in range(0, 599):
            temp_c[j, k, d] = t2[j, k, d] - 273.15
datevar = num2date(time[:], units='hours since 1970-01-01 00:00:00', calendar='standard')
# print(datevar[:])
map = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
              resolution='i')
# map.drawcoastlines()
# map.drawstates()
# map.drawcountries()
# map.drawlsmask(land_color='Linen', ocean_color='#CCFFFF')
lon2, lat2 = np.meshgrid(lons, lats)
x, y = map(lon2, lat2)
plt.gca().set_axis_off()
plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                    hspace=0, wspace=0)
plt.margins(0, 0)
map.pcolormesh(x, y, temp_c[0, :, :], cmap='rainbow')
# plt.colorbar(label="Temperature (Celsius)")
plt.clim(-5, 40)
for b in range(0, 1):
    map.pcolormesh(x, y, temp_c[b, :, :], cmap='rainbow')
    # plt.title('2m Temperature on %s' % datevar[b])
    plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/ta2m_diurnal_mean_nokey_%s.png" % b, transparent='True',
                bbox_inches='tight', pad_inches=0)
    print('saved %s' % b)
