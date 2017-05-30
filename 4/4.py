import arcpy
arcpy.env.workspace=r'C:\Users\S1mple\Desktop\Paper_14\4'
arcpy.CheckOutExtension("Spatial")
rasterlist = arcpy.ListRasters( )
print arcpy.Describe(rasterlist[0]).dataType
arcpy.RasterToPoint_conversion(r'C:\Users\S1mple\Desktop\Paper_14\4\Elevation','point.shp')
