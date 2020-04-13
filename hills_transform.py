import cartopy.crs as ccrs
import cartopy.feature as cfeature  #for plotting land and sea
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter


dataframe = pd.read_csv("scottish_hills.csv")

fig = plt.figure(figsize=(20,10))
ax = plt.axes(projection=ccrs.Mercator())
plt.title("Scottish Munros",fontdict={'fontsize': 20})
map_transform = ccrs.PlateCarree()._as_mpl_transform(ax)

##  Create a transform of type below, to be applied to coordinate systems.
##  type(transform)
##  <class 'matplotlib.transforms.CompositeGenericTransform'>
##

ax.coastlines('10m')

ax.xaxis.set_visible(True)
ax.yaxis.set_visible(True)

ax.set_yticks([56,57,58,59], crs=ccrs.PlateCarree())
ax.set_xticks([-8, -6, -4, -2], crs=ccrs.PlateCarree())

ax.set_extent([-8, -1.5, 55.3, 59])

lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()

ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)

nevis = dataframe[dataframe['Hill Name'] =="Ben Nevis"].values.tolist()
nevis = nevis[0]
[name, height, lat, lon, grid] = nevis


bbox = dict(boxstyle="round", fc="0.8")
arrowprops = dict(
    arrowstyle = "->",
    connectionstyle="angle,angleA=0,angleB=90,rad=10")



stats = ('Hill: %s \nHeight: %.1fm' % (name,height))



ax.plot(lon,lat, 'bx', transform=ccrs.PlateCarree(),
        label = "Tallest Mountain")

tall_threshold = 1250

low = dataframe[dataframe['Height'] <= tall_threshold]
high = dataframe[dataframe['Height'] > tall_threshold]
high = high[high['Hill Name'] != "Ben Nevis"]


ax.scatter(high['Longitude'],high['Latitude'],
                    color='blue', marker='*', transform=ccrs.PlateCarree(),
           label = ('Mountains > %.0fm' % tall_threshold))

ax.scatter(low['Longitude'],low['Latitude'],
                    color='red', marker='.',alpha=0.2, transform=ccrs.PlateCarree(),
           label = ('Mountains < %.0fm' % tall_threshold))

ax.legend(loc='lower right',shadow = True)

#ax.annotate(stats, xy=(lon,lat), )

## Utilise map_transform to change lon, lat points into display points.
xdisplay, ydisplay = map_transform.transform_point((lon, lat))
xaxes,yaxes = ax.transAxes.transform_point((xdisplay, ydisplay))

ax.plot(xdisplay,ydisplay, 'go')
ax.plot(xaxes,yaxes,'r*')

# disp = ax.annotate(stats,
#                    xy=(xdisplay,ydisplay), xytext=(0.5*offset,-offset),
#                    xycoords='figure pixels',
#                     textcoords='offset points',
#                    bbox=bbox, arrowprops=arrowprops)
offset = 150

disp = ax.annotate(stats,
                   xy=(lon,lat), xytext=(0.5*offset,-offset),
                   xycoords=map_transform,      ##xycoords are based on the transform defined above!
                    textcoords='offset points',
                   bbox=bbox, arrowprops=arrowprops)

plt.show()

