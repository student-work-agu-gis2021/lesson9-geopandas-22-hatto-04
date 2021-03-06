#!/usr/bin/env python
# coding: utf-8

# ## Problem 2: Points to map
#  
# In this problem we continue to learn how to turn latitude and longitude coordinates in to geometries.
# 


import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
# YOUR CODE HERE 1 to read data
data = pd.read_csv('data/some_posts.csv')
data["geometry"]=""

for i,r in data.itterrows():
  x=Point(r["lat"],r["lon"])
  data.at[i,"geometry"]=x

# CODE FOR TESTING YOUR SOLUTION

# Check the result
print("Number of rows:", len(data))


# CODE FOR TESTING YOUR SOLUTION

# Check the result
print(data['geometry'].head())


# YOUR CODE HERE 2
import geopandas as gpd
from pyproj import CRS
geo=gpd.GeoDataFrame(data,geometry='geometry',crs=CRS.from_epsg(4326).to_wkt())
fp='Kruger_posts.shp'
geo.to_file(fp)
# Convert DataFrame into a GeoDataFrame
geo=None
# CODE FOR TESTING YOUR SOLUTION

# Check the geodataframe head
print("Number of rows:", len(geo))
print(geo.head())


# CODE FOR TESTING YOUR SOLUTION

# Check that the output file exists
import os
assert os.path.isfile(fp), "output shapefile does not exist"


# **Finally:** 
# - **Create a simple map of the points** using the `plot()` -funtion. 

# YOUR CODE HERE 3
geo.plot()
# Well done! Now you can move on to Exercise_9_problem_3.

def func5():
    return data

def func6():
    return geo


