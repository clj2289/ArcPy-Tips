```python
import arcpy
fc = 'c:/data/base.gdb/well'
sr = arcpy.SpatialReference(4236)
# Create update cursor for feature class 
with arcpy.da.UpdateCursor(fc, 'SHAPE@WKT', spatial_reference=sr) as cursor:
    for row in cursor:
        print row[0]
        cursor.updateRow(row)
```
