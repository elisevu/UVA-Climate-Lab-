import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset as Ncdf
from netCDF4 import num2date
import datetime
from mpl_toolkits.basemap import Basemap
import matplotlib

matplotlib.use("Agg")
nc = Ncdf('ta_2m_1hr_20090101_d02.nc', 'r')
print(nc)
for i in nc.variables:
    print(i, nc.variables[i].units, nc.variables[i].shape)
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]
time = nc.variables['time'][:]
t2 = nc.variables['ta_2m'][:]
t_units = nc.variables['time'].units
add = 0.0
avg = 0
# avg_temps = []
# for i in lons:
#     for j in lats:
#         for x in t2[:]:
#             add += x
#             if x % 24 == 0:
#                 break
#         avg_temps.append(add / 24)
#         add = 0
# print(avg_temps)

datevar = num2date(time[:], units='hours since 1970-01-01 00:00:00', calendar='standard')
print(datevar[:])
map = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
              resolution='i')
# map.drawcoastlines()
# map.drawstates()
# map.drawcountries()
# map.drawlsmask(land_color='Linen', ocean_color='#CCFFFF')
lon2, lat2 = np.meshgrid(lons, lats)
x, y = map(lon2, lat2)
my_cmap = plt.get_cmap('RdBu_r')
plt.gca().set_axis_off()
plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                    hspace=0, wspace=0)
plt.margins(0, 0)
map.pcolormesh(x, y, t2[0, :, :], cmap='RdBu_r')
plt.colorbar(label="Temperature (Celsius)")
for b in range(0, 31):
    map.pcolormesh(x, y, t2[b, :, :], cmap='RdBu_r')
    plt.title('2m Temperature on %s' % datevar[b])
    plt.savefig("E:/elise/Documents/JungoBunbo/jan-2009-air-temperature/ta2m_%s.png" % b, transparent='True',
                bbox_inches='tight', pad_inches=0)
    print('saved %s' % b)
