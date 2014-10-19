rem this guide assumes ArcGIS Server 10.2 running on windows
rem download ez_setup.py from http://peak.telecommunity.com/dist/ez_setup.py
rem open command prompt as administrator

rem install 64 bit version
c:\python27\ArcGISx6410.2\python ez_setup.py
cd c:\python27\ArcGISx6410.2\Scripts\
easy_install.exe install pip

rem install 32 bit version
c:\python27\ArcGIS10.2\python ez_setup.py
cd c:\python27\ArcGIS10.2\Scripts\
easy_install.exe install pip

rem pip is now ready
rem pip install <name_of_python_library>