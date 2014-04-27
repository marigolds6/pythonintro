#Remarkable bird, the Norwegian ```arcpy.mapping```, beautiful cartography, innit?

## The 'boilerplate'
```
import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
```
Most "List" functions like ```ListDataFrames``` return Lists. (Watch for tuples though.)

## Refreshing
 * ```arcpy.RefreshTOC()```
 * ```arcpy.RefreshActiveView()```
 * ```arcpy.RefreshCatalog()``` and why it wants an argument

## Extents
 * ```df.extent```
 * ```arcpy.Extent``` objects
    - Layers (```arcpy.mapping.ListLayers(mxd)```)
    - Bookmarks (```arcpy.mapping.ListBookmarks(mxd)```)
    - Build your own (XMin, YMin, XMax, YMax)

## Layout Elements
[```arcpy.mapping.ListLayoutElements()```](http://resources.arcgis.com/en/help/main/10.2/index.html#/ListLayoutElements/00s30000003w000000/])  
```
arcpy.mapping.MapsurroundElement
arcpy.mapping.GraphicElement
arcpy.mapping.PictureElement
arcpy.mapping.LegendElement
```

## Symbology
You have to use existing .lyr files.
Can do some limited modification of [some symbology]((http://resources.arcgis.com/en/help/main/10.2/index.html#/UniqueValuesSymbology/00s30000005s000000/)):  
 * Graduated Color
 * Graduated Symbol
 * Raster Classified
 * Unique Values

## ```arcpy.mapping.ExportTo...```
[```arcpy.mapping.ExportToPDF```](http://resources.arcgis.com/en/help/main/10.2/index.html#/ExportToPDF/00s300000027000000/) is most commonly used
```
doc = arcpy.mapping.PDFDocumentCreate(<path>)
http://resources.arcgis.com/en/help/main/10.2/index.html#/PDFDocumentCreate/00s300000019000000/
doc.appendpages(<additional doc path>)
doc.saveAndClose()
```

## What you cannot do!
 * Cannot create an mxd!
 * Cannot create a .lyr!
 * Cannot create new date frames!
 * Cannot create new text elements!
(But can clone existing MapDocument or Layer with ```saveCCopy``` or TextElment with ```clone```.)
