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
# for i in nc.variables:
#     print(i, nc.variables[i].units, nc.variables[i].shape)
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]
time = nc.variables['time'][:]
t2 = nc.variables['ta_2m'][:]
t_units = nc.variables['time'].units
temp_c = t2
lons55 = nc55.variables['lon'][:]
lats55 = nc55.variables['lat'][:]
time55 = nc55.variables['time'][:]
t255 = nc55.variables['ta_2m'][:]
t_units55 = nc55.variables['time'].units
temp_c55 = t255
diff = t2
max  = -478324
min = 7489324
# for j in range(0, 24):
#     print(j)
#     for k in range(0, 699):
#         for d in range(0, 600):
#             temp_c[j,k,d] = t2[j,k,d] - 273.15
#             temp_c55[j, k, d] = t255[j, k, d] - 273.15
#             diff[j,k,d] = temp_c55[j, k, d] - temp_c[j, k, d]
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

plt.figure(figsize=(601/100, 700/100))
plt.gca().set_axis_off()
plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                    hspace=0, wspace=0)
plt.margins(0, 0)
#plt.colorbar(label="Temperature (Celsius)")

for b in range(0, 24):
    map.pcolormesh(x, y, diff[b, :, :], cmap='bwr', vmin=-6, vmax=6)
    #plt.title('2m Temperature on %s' % datevar[b])
    plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/ta2m_diurnal_mean_diff_2055-2064_%s.png" % b, transparent='True',
                bbox_inches='tight', pad_inches=0)
    print('saved %s' % b)
plt.colorbar(label="Difference in Temperature (Celsius)")
plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/ta2m_diurnal_mean_diff_2055-2064_KEY_%s.png" % b, transparent='True',
            bbox_inches='tight', pad_inches=0)
