import cartopy.crs as ccrs
import cartopy.feature as cfeature  #for plotting land and sea
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from adjustText_ex import adjust_text    #package example here: https://stackoverflow.com/questions/19073683/matplotlib-overlapping-annotations-text

import cartopy.feature as cfeature
from matplotlib.offsetbox import AnchoredText


dataframe = pd.read_csv("scottish_hills.csv")

x = dataframe.Height
y = dataframe.Latitude

plt.figure(figsize=(20,10))
ax = plt.axes(projection=ccrs.Mercator())

ax.coastlines('10m')

ax.xaxis.set_visible(True)
ax.yaxis.set_visible(True)

ax.set_yticks([56,57,58,59], crs=ccrs.PlateCarree())
ax.set_xticks([-8, -6, -4, -2], crs=ccrs.PlateCarree())

lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()

ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)

ax.set_extent([-8, -1.5, 55.3, 59])

transform = ccrs.PlateCarree()._as_mpl_transform(ax)    #create a matplotlib transform for any catopy coordinate system

tall_threshold = 1250

low = dataframe[dataframe['Height'] <= tall_threshold]
high = dataframe[dataframe['Height'] > tall_threshold]

ax.scatter(low['Longitude'],low['Latitude'],
                    color='red', marker='.', transform=ccrs.PlateCarree())


ax.scatter(high['Longitude'],high['Latitude'],
                    color='blue', marker='*', transform=ccrs.PlateCarree())

# texts = []
for i, txt in enumerate(high['Hill Name']):
    print(high.iloc[i]['Longitude'], high.iloc[i]['Latitude'])
    print(txt)
    a = ax.annotate(txt, xy=(high.iloc[i]['Longitude'], high.iloc[i]['Latitude']),
                        xycoords = transform, xytext=(high.iloc[i]['Longitude'], high.iloc[i]['Latitude']),
                                arrowprops=dict(facecolor='gray',
                                arrowstyle="simple"),
                        ha='right', va ='top')





texts = []
for x, y, s in zip(high['Longitude'],high['Latitude'],high['Hill Name']):
    texts.append(plt.text(x, y, s))

#adjust_text(texts, arrowprops=dict(arrowstyle="->", color='r', lw=0.5), save_steps=False ,transform=transform)

plt.savefig("munros.png")