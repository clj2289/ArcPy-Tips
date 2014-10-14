import arcpy


springsShapefile = "../ExampleData/springs_fdep_2011/springs_fdep_2011.shp"
springsInMemory = "in_memory//springs"

arcpy.CopyFeatures_management (springsShapefile, springsInMemory)

sr = arcpy.SpatialReference(4236)

##### #1 Cursor based reprojection da.UpdateCursor (fastest)
with arcpy.da.UpdateCursor(springsInMemory, 'SHAPE@WKT', spatial_reference=sr) as cursor:
    for row in cursor:
        print row[0]
        cursor.updateRow(row)

##### #2 Cursor based reprojection da.SearchCursor (fastest)
with arcpy.da.SearchCursor(springsInMemory, 'SHAPE@WKT', spatial_reference=sr) as cursor:
    for row in cursor:
        print row[0]


##### #3 Cursor based reprojection arcpy.SearchCursor (slower than using da cursors, only use for ArcGIS 10)
cursor = arcpy.UpdateCursor(springsInMemory, "Shape@", spatial_reference=sr)
for row in cursor:
	print row[0]
    cursor.updateRow(row)

##### #4 Cursor based reprojection arcpy.UpdateCursor (slower than using da cursors, only use for ArcGIS 10)
cursor = arcpy.SearchCursor(springsInMemory, "Shape@", spatial_reference=sr)
for row in cursor:
    print(row.getValue("Shape@"))

##### #5 Project_management (can not output in_memory feature classes, very, very slow)
projectedShapefile = "springs_projected.shp"
arcpy.Project_management(springsInMemory, projectedShapefile, sr)
