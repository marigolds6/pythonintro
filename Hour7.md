#Arcpy Geoprocessing: My hovercraft is full of eels.  
  
## Licensing and ```arcpy```

### Version and product
```
arcpy.GetInstallInfo() #Information about installation
(main,minor,sub) = arcpy.GetInstallInfo()['Version'].split('.')
arcpy.CheckProduct(u'arcinfo')
arcpy.SetProduct(u'arcinfo')
arcpy.ProductInfo()
```

### Extension demo
```
arcpy.CheckExtension(u'3D')
arcpy.AddZInformation_3d()
arcpy.CheckOutExtension(u'3D')
arcpy.AddZInformation_3d()
arcpy.CheckInExtension(u'3D')
arcpy.AddZInformation_3d()

```

## Geoprocessing
[Sample files on dropbox](https://www.dropbox.com/s/ewanlg0vhm9rkv7/Assignment3.zip)  
Our plan: Take only the public schools and divide them up into feature classes by school district
 1. Test for the existence of our file geodatabase using ```arcpy.Exists()```
    If absent, create with ```CreateFileGDB_management (out_folder_path, out_name, {out_version})```
 2. If the file geodatabase existed, check for existing output using ```arcpy.Exists()``` and warn user of overwrite.
 3. Create a feature class of public schools
    - Use ```arcpy.CreateScratchName()``` for our temp file name
    - Can use ```arcpy.Select_analysis()```  
      *or*  
      ```arcpy.SelectLayerByAttribute_management()``` + ```arcpy.CopyFeatures_management()```
 4. Divide the schools up by district with ```arcpy.Split_analysis()```  
  
