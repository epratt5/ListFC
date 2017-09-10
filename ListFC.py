# Author: Emilie Pratt
# Date: 10 Sept 2017
# Purpose: GitHub Training

# Import ArcPy
import arcpy

# Set the workspace
arcpy.env.workspace = "C:/Users/erbre/Desktop/Programming 606/Data/Assignment 2/Newark.gdb"
path = arcpy.env.workspace

# List all of the feature classes in the Newark geodatabase 
newarkGDB = arcpy.ListFeatureClasses()

# Iterate through all the feature classes and print the name of each feature class 
for fc in newarkGDB:
    print fc

# Print "Complete"
print "Complete"

