import arcpy

# define feature class locations
pointssShapefile = "../ExampleData/points.shp"
pointsInMemory = "in_memory//points"

# copy in shapefile to in_memory feature class
arcpy.CopyFeatures_management (pointssShapefile, pointsInMemory)

# create spatial reference object
sr = arcpy.SpatialReference(4236)

##### #1 Cursor based reprojection da.UpdateCursor (fastest)
with arcpy.da.UpdateCursor(pointsInMemory, 'SHAPE@WKT', spatial_reference=sr) as cursor:
    for row in cursor:
        print row[0]
        cursor.updateRow(row)

##### #2 Cursor based reprojection da.SearchCursor (fastest)
with arcpy.da.SearchCursor(pointsInMemory, 'SHAPE@WKT', spatial_reference=sr) as cursor:
    for row in cursor:
        print row[0]


##### #3 Cursor based reprojection arcpy.SearchCursor (slower than using da cursors, only use for ArcGIS 10)
cursor = arcpy.UpdateCursor(pointsInMemory, spatial_reference=sr)
for row in cursor:
    print row
    cursor.updateRow(row)

##### #4 Cursor based reprojection arcpy.UpdateCursor (slower than using da cursors, only use for ArcGIS 10)
cursor = arcpy.SearchCursor(pointsInMemory, spatial_reference=sr)
for row in cursor:
    print row
