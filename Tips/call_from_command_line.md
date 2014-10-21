Use [arcpy.GetParameterAsText()](http://resources.arcgis.com/en/help/main/10.2/index.html#//018v00000047000000) to read in commandline arguments as you would use [sys.argv](https://docs.python.org/2/library/sys.html) in non-arcpy python scripts.

[Example arcpy python code](call_from_command_line.py):

```python
import arcpy

input = arcpy.GetParameterAsText(0)
print input
```

Now call this from the commandline with an argument:

```
python call_from_command_line.py "Hello GetParameterAsText!"

Hello GetParameterAsText!
```
