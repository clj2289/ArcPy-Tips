import arcpy
import glob
import os

# Lets do some clean up first
for shpFilePart in glob.glob("../ExampleData/out_points*"):
    os.remove(shpFilePart)

# define feature class locations
springsShapefile = "../ExampleData/points.shp"
springsInMemory = "in_memory//points"

# copy in shapefile to in_memory feature class
arcpy.CopyFeatures_management (springsShapefile, springsInMemory)

# copy in_memory feature class to shapefile
arcpy.CopyFeatures_management (springsInMemory, "../ExampleData/out_points.shp")
