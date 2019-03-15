#!/usr/bin/python
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


lats, lons, names, = [], [], []

with open('cordinates.txt','r') as f:
    line = f.readline()
    while line:
        split_list = line.split(",")
        lats.append(split_list[1])
        lons.append(split_list[0])
        names.append(split_list[2])
        line = f.readline()


zoom_scale = 0

bbox = [np.min(lats) - zoom_scale, np.max(lats) + zoom_scale, \
        np.min(lons) - zoom_scale, np.max(lons) + zoom_scale]

plt.figure(figsize=(12, 6))
# Define the projection, scale, the corners of the map, and the resolution.
m = Basemap(projection='merc', llcrnrlat=bbox[0], urcrnrlat=bbox[1], \
            llcrnrlon=bbox[2], urcrnrlon=bbox[3], lat_ts=10, resolution='i')

# Draw coastlines and fill continents and water with color
m.drawcoastlines()
m.fillcontinents(color='peru', lake_color='dodgerblue')

# draw parallels, meridians, and color boundaries
m.drawparallels(np.arange(bbox[0], bbox[1], (bbox[1] - bbox[0]) / 5), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(bbox[2], bbox[3], (bbox[3] - bbox[2]) / 5), labels=[0, 0, 0, 1], rotation=45)
m.drawmapboundary(fill_color='dodgerblue')

# build and plot coordinates onto map
x, y = m(lons, lats)
m.plot(x, y, 'r*', markersize=5)
plt.title("Crop Cordinates")
plt.savefig('crop_map.png', format='png', dpi=500)
plt.show()
