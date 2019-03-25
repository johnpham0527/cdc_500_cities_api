#!/usr/bin/env python

#This code produces descriptive statistics related to community demographics and community health for a given list of census tracts

#before running, make sure censustracts.py is stored in the same directory as this file
from censustracts import *
from counties import *

# Uncomment the below code to execute an analysis of Queens census tracts that contain a NYCHA campus
#NYCHACensusTractsAnalysis = MyCensusTractList(createCensusTractArray("NYCHAQueensCensusTracts.txt")) #this creates an array of census tract objects, given a list of census tracts read in from a file
#print("Summary of Descriptive Statistics for the Given " + str(NYCHACensusTractsAnalysis.censusTractArrayLength) + " Census Tract(s):")
#print("Percentage of older males age 65+ who received core preventive services: " + "{:.1f}".format(NYCHACensusTractsAnalysis.coreMenPercentage) + "%")  #print out with one decimal place
#print("Percentage of older females age 65+ who received core preventive services: " + "{:.1f}".format(NYCHACensusTractsAnalysis.coreWomenPercentage) + "%")
#print("Percentage of older adults age 50-75 who received a colon screening: " + "{:.1f}".format(NYCHACensusTractsAnalysis.colonScreenPercentage) + "%")
#print("Percentage of older females age 50-74 who received a mammogram: " + "{:.1f}".format(NYCHACensusTractsAnalysis.mammoUsePercentage) + "%")
#print("Percentage of older adults age 65+ who have all teeth lost: " + "{:.1f}".format(NYCHACensusTractsAnalysis.teethLostPercentage) + "%")
#NYCHACensusTractsAnalysis.exportValues("NYCHA_Data3.csv") #output the data to a CSV file

NYCCountyAnalysis = MyCountyList(createCountyArray("NYCCounties.txt")) #this creates an array of county objects, given a list of county numbers read in from a file
print("Summary of Descriptive Statistics for the Given " + str(NYCCountyAnalysis.countyArrayLength) + " Counties:")
print("Percentage of older males age 65+ who received core preventive services: " + "{:.1f}".format(NYCCountyAnalysis.coreMenPercentage) + "%")  #print out with one decimal place
print("Percentage of older females age 65+ who received core preventive services: " + "{:.1f}".format(NYCCountyAnalysis.coreWomenPercentage) + "%")
print("Percentage of older adults age 50-75 who received a colon screening: " + "{:.1f}".format(NYCCountyAnalysis.colonScreenPercentage) + "%")
print("Percentage of older females age 50-74 who received a mammogram: " + "{:.1f}".format(NYCCountyAnalysis.mammoUsePercentage) + "%")
print("Percentage of older adults age 65+ who have all teeth lost: " + "{:.1f}".format(NYCCountyAnalysis.teethLostPercentage) + "%")
NYCCountyAnalysis.exportValues("NYC_Data.csv") #output the data to a CSV file