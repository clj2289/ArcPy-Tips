Fast reprojection, works with "in_memory" feature sets

```python
import arcpy

sr = arcpy.SpatialReference(32145)

fc = 'c:/data/base.gdb/well'

# Create update cursor for feature class 
with arcpy.da.UpdateCursor(fc, '*', spatial_reference=sr) as cursor:
    for row in cursor:
        cursor.updateRow(row)
```
