import arcpy
arcpy.env.workspace = u'C:\\Assignment3\\'
arcpy.env.overwriteOutput = True
if not arcpy.Exists(u'districts.gdb'):
    arcpy.CreateFileGDB_management(arcpy.env.workspace,'districts.gdb')
else:
    print "File geodatabase 'districts.gdb' already exists.\nExisting output may be overwritten"
arcpy.env.workspace = u'C:\\Assignment3\\districts.gdb'
arcpy.Split_analysis(u'C:\\Assignment3\\PublicSchools.shp',u'C:\\Assignment3\\SchoolDistricts.shp',"SCHOOL_DIS",arcpy.env.workspace)
                     
