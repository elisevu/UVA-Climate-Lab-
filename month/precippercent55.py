import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from netCDF4 import Dataset as Ncdf
from mpl_toolkits.basemap import Basemap
import matplotlib
# CREATE DIRECTORIES /precip_amnt_freq_month_2055_2064_cat0_maps/ for cat0 - cat3
matplotlib.use("Agg")
nc = Ncdf('precip_exc_freq_d02_2055-2064.nc', 'r')
print(nc)
print(nc.variables["category"][:])
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]
month = nc.variables['month'][:]
precip = nc.variables['precip_amnt_freq_month'][:]
cat = nc.variables["category"][:]

mapp = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
               resolution='i')
lon2, lat2 = np.meshgrid(lons, lats)
x, y = mapp(lon2, lat2)
plt.figure(figsize=(601 / 100, 700 / 100))
plt.gca().set_axis_off()
plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                    hspace=0, wspace=0)
plt.margins(0, 0)
cmap = plt.get_cmap('gist_rainbow')
cmapr = plt.get_cmap('gist_rainbow_r')


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    new_cmap.set_under('white')  # 1.0 represents not transparent
    new_cmap.set_bad('white')
    return new_cmap


cmap2 = truncate_colormap(cmap, 0.0, .85)
cmap3 = truncate_colormap(cmapr, 0.15, 1.0)
mapp.pcolormesh(x, y, precip[0, 1, :, :], cmap=cmap2, vmin=0, vmax=100)
plt.title("Percentage of Days with Precipitation Less than 0.5 mm/day")
plt.colorbar(label="Percent")
plt.savefig("precip_amnt_freq_month_2055_2064_cat0_maps/"
            "precip_amnt_freq_month_2055_2064_0_KEY.png", transparent='True',
            bbox_inches='tight', pad_inches=0)
plt.clf()
print('saved cat 1 key')
mapp.pcolormesh(x, y, precip[0, 1, :, :], cmap=cmap3, vmin=0, vmax=100)
plt.title("Percentage of Days with Precipitation Less than 0.5 mm/day")
plt.colorbar(label="Percent")
plt.savefig("precip_amnt_freq_month_2055_2064_cat0_maps/reversed/"
            "precip_amnt_freq_month_2055_2064_0_KEY_R.png", transparent='True',
            bbox_inches='tight', pad_inches=0)
plt.clf()
print('saved cat 1 key reverse')

mapp.pcolormesh(x, y, precip[1, 1, :, :], cmap=cmap2, vmin=0, vmax=100)
plt.title("Percentage of Days with Precipitation Greater than 0.5 mm/day")
plt.colorbar(label="Percent")
plt.savefig("precip_amnt_freq_month_2055_2064_cat1_maps/"
            "precip_amnt_freq_month_2055_2064_1_KEY.png", transparent='True',
            bbox_inches='tight', pad_inches=0)
plt.clf()
print('saved cat 2 key')
mapp.pcolormesh(x, y, precip[2, 1, :, :], cmap=cmap2, vmin=0, vmax=100)
plt.title("Percentage of Days with Precipitation Greater than 5 mm/day")
plt.colorbar(label="Percent")
plt.savefig("precip_amnt_freq_month_2055_2064_cat2_maps/"
            "precip_amnt_freq_month_2055_2064_2_KEY.png", transparent='True',
            bbox_inches='tight', pad_inches=0)
plt.clf()
print('saved cat 3 key')
mapp.pcolormesh(x, y, precip[3, 1, :, :], cmap=cmap2, vmin=0, vmax=100)
plt.title("Percentage of Days with Precipitation Greater than 25 mm/day")
plt.colorbar(label="Percent")
plt.savefig("precip_amnt_freq_month_2055_2064_cat3_maps/"
            "precip_amnt_freq_month_2055_2064_3_KEY.png", transparent='True',
            bbox_inches='tight', pad_inches=0)
print('saved cat 4 key')
plt.clf()
# # plt.title('Daily Precip Mean over Month of X')
for c in range(0, 4):
    for b in range(0, 12):
        # plt.title('2m Temperature on %s' % datevar[b])
        if c == 0:
            mapp.pcolormesh(x, y, precip[c, b, :, :], cmap=cmap3, vmin=0, vmax=100)
            plt.savefig("precip_amnt_freq_month_2055_2064_cat%s_maps/reversed/"
                        "precip_amnt_freq_month_2055_2064_%s_%s_R.png" % (c, c, b + 1),
                        transparent='True',
                        bbox_inches='tight', pad_inches=0)
            print('saved cat %s month %s RE' % (c, b))
        mapp.pcolormesh(x, y, precip[c, b, :, :], cmap=cmap2, vmin=0, vmax=100)
        plt.savefig("precip_amnt_freq_month_2055_2064_cat%s_maps/"
                    "precip_amnt_freq_month_2055_2064_%s_%s.png" % (c, c, b+1),
                    transparent='True',
                    bbox_inches='tight', pad_inches=0)
        print('saved cat %s month %s' % (c, b))
    plt.clf()





