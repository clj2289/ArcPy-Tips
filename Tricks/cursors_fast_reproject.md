```python
import arcpy

fc = 'c:/data/base.gdb/well'

sr = arcpy.SpatialReference(4236)

# Create update cursor for feature class 
with arcpy.da.UpdateCursor(fc, fields, spatial_reference=sr) as cursor:
    for row in cursor:
        cursor.updateRow(row)
```
