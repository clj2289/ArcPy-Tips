ArcPy-Tips
==========

ArcPy tips, tricks, best management practices and most of all...hacks!

## Best Management Practices
* Use of data access cursors (arcpy.da.*)
* Always use a scratch workspace if you _have_ to write data to disk
* Turn of archiving unless its required

## Tips
* Call your python scripts from the command line and sent in parameters
* Use the built in python profiler to make your code faster (python -m cProfile -s tottime your.py cities.shp)
* Use PyPyODBC
* Always use in_memory feature classes when possible for high performance
* Use list comprehension 
* Install pip on windows

## Tricks
* Use arcpy old style cursors for reprojection
* Output in_memory feature classes to shapefiles for debugging
* Output map documents to mxds for debugging
* All Geoprocessing services have a built-in file upload option that you can take advantage of
* For performance reasons, use synchronous tasks when possible
* Set logging level to "Info" in geoprocessing tasks to capture excution time of the task
* Set running instances to 0 for all GP and Mapservices in development to conserve memory on the ArcGIS server
* Access files on a windows file share in an arcpy script using win_unc

## Hacks
* sql server rowid 
