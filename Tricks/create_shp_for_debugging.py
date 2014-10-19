import arcpy

# define feature class locations
springsShapefile = "../ExampleData/springs_fdep_2011/springs_fdep_2011.shp"
springsInMemory = "in_memory//springs"

# copy in shapefile to in_memory feature class
arcpy.CopyFeatures_management (springsShapefile, springsInMemory)

# copy in_memory feature class to shapefile
arcpy.CopyFeatures_management (springsInMemory, "../ExampleData/springs_fdep_2011/out_springs_fdep_2011.shp")
