# %%
#update
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt

api = SentinelAPI('user', 'password')
footprint = geojson_to_wkt(read_geojson('search_polygon.geojson'))
products = api.query(footprint,
                     producttype='SLC',
                     orbitdirection='ASCENDING',
                     limit=10)
api.download_all(products)

# %%


import folium
import os
import numpy as np

from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt 
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shapely.geometry import MultiPolygon, Polygon
import rasterio as rio
from rasterio.plot import show
import rasterio.mask
import fiona

#import rioxarray module
import rioxarray
from rasterio.crs import CRS



#Define ROI
#make a GeoJSON file of the ROI

# %%


m = folium.Map([50.6, -1.3], zoom_start=8)
conda install -c conda-forge shapely
# %%
boundsdata = r'/Users/petersinnott/Desktop/PY3/thermalWaters/thermalWaters/bounds_IOW.geojson'


#Download Imagery

#
# %%
user = 'funkmasterp2' ## change this!
password = 'PASSWORD!' ## change this!

api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')

footprint = geojson_to_wkt(read_geojson(boundsdata))

print (footprint)

products = api.query(footprint,
                     date = ('20230301', '20230502'),
                     platformname = 'Sentinel-2',
                     processinglevel = 'Level-2A',
                     cloudcoverpercentage = (0, 20))
# %%
print(products)
#view available scenes
# %%

areas = api.to_geodataframe(products)
areas.plot(column='uuid', cmap=None)
# %%

#Download Imagery
#Filter high NDWI for water
#Look at temporal anomolies of water pixels
#Anything with Topo?
#unity software


gdf2.plot(ax=ax)
plt.show()

# %%
api.download('a1ecc53d-71f7-4ddd-b402-0ee6d31b16d0')
# %%
product_odata = api.get_product_odata('a1ecc53d-71f7-4ddd-b402-0ee6d31b16d0')

# Get the filename from the metadata
filename = product_odata['title']

# Combine the filename with the download directory path to get the full path to the downloaded file
path_tozip = '/Users/petersinnott/Desktop/Python/testsBasic/' + filename + '.zip'

# Print the path to verify that it was obtained correctly
print(path_tozip)
# %%
zip_ref = zipfile.ZipFile(path_tozip, 'r')
zip_ref.extractall(r'/Users/petersinnott/Desktop/Python/testsBasic/')
zip_ref.close()
# %%

#display
#filter just for pixels of high valie
