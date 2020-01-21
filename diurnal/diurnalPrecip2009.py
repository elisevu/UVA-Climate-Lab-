import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from netCDF4 import Dataset as Ncdf
from netCDF4 import num2date
from mpl_toolkits.basemap import Basemap
import matplotlib
from PIL import Image

matplotlib.use("Agg")
nc = Ncdf('precip_diurnal_mean_d02_2009-2018.nc', 'r')
nc55 = Ncdf('precip_diurnal_mean_d02_2055-2064.nc', 'r')
for i in nc.variables:
    print(i, nc.variables[i].units, nc.variables[i].shape)
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]
time = nc.variables['time'][:]
rr = nc.variables['rainfall_rate'][:]
t_units = nc.variables['time'].units
max = -478324
min = 7489324
for j in range(0, 24):
    print(j)
    for k in range(0, 699):
        for d in range(0, 600):
            if rr[j, k, d] >= max:
                max = rr[j, k, d]
            if rr[j, k, d] <= min:
                min = rr[j, k, d]

print(max)
print(min)

datevar = num2date(time[:], units='hours since 1970-01-01 00:00:00', calendar='standard')
mapp = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
               resolution='i')
lon2, lat2 = np.meshgrid(lons, lats)
x, y = mapp(lon2, lat2)
plt.figure(figsize=(601 / 100, 700 / 100))
plt.gca().set_axis_off()
plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                    hspace=0, wspace=0)
plt.margins(0, 0)

# plt.title('2m Temperature on %s' % datevar[b])
for b in range(0, 24):
    mapp.pcolormesh(x, y, rr[b, :, :], cmap='gist_rainbow', vmin=0, vmax=6)
    # plt.title('2m Temperature on %s' % datevar[b])
    plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/precip_diurnal_2009-2018_%s.png" % b, transparent='True',
                bbox_inches='tight', pad_inches=0)
    print('saved %s' % b)
plt.colorbar(label="Rainfall Rate (mm/hr)")
plt.savefig("E:/elise/Documents/UVA-Climate-Lab-/diurnal/precip_diurnal_2009-2018_KEY.png", transparent='True',
            bbox_inches='tight', pad_inches=0)
