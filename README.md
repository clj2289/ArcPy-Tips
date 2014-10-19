ArcPy-Tips
==========

ArcPy tips, tricks, best management practices and most of all...hacks!

## Best Management Practices
* Use [data access cursors (arcpy.da.*)](http://resources.arcgis.com/en/help/main/10.2/index.html#/What_is_the_data_access_module/018w00000008000000/) when possible.  Avoid using [legacy arcpy cursors](http://resources.arcgis.com/en/help/main/10.2/index.html#//018v0000002z000000) at all cost.
* Always use a scratch workspace if you _have_ to write data to disk
* Turn off archiving unless its required
* Use "with" keyword when possible

## Tips
* Call your python scripts from the command line and sent in parameters
* Use the built in python profiler to make your code faster (python -m cProfile -s tottime your.py cities.shp)
* Use PyPyODBC
* Always use in_memory feature classes when possible for high performance
* Use list comprehension
* [Install pip on Windows](Tips/install_pip.cmd)
* Working with and installing python libraries for 64 Bit python i.e. c:\python27\ArcGISx6410.2\python

## Tricks
* [Use arcpy.da.UpdateCursor and arcpy.da.SearchCursor for fast in memory reprojection](Tricks/cursors_fast_reproject.py)
* [Output in_memory feature classes to shapefiles for debugging](Tricks/create_shp_for_debugging.py)
* Output map documents to mxds for debugging
* All Geoprocessing services have a built-in file upload option that you can take advantage of
* For performance reasons, use synchronous tasks when possible
* Set logging level to "Info" in geoprocessing tasks to capture excution time of the task
* Set running instances to 0 for all GP and Mapservices in development to conserve memory on the ArcGIS server
* Access files on a windows file share in an arcpy script using win_unc
* Geoprocssing services are running 64bit (c:\PYTHON27\ArcGISx6410.2) python while scripts that are run via ArcCatalog are running under 32bit python (c:\PYTHON27\ArcGIS10.2) you must install both a 32bit and a 64bit python library to be able to publish a GP service

## Hacks
* sql server rowid 
