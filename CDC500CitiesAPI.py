#!/usr/bin/env python

#This code produces descriptive statistics related to community demographics and community health for a given list of census tracts

#before running, make sure censustracts.py is stored in the same directory as this file
from censustracts import *

NYCHACensusTractsAnalysis = MyCensusTractList(createCensusTractArray("NYCHAQueensCensusTracts.txt")) #this creates an array of census tract objects, given a list of census tracts read in from a file
print("Summary of Descriptive Statistics for the Given " + str(NYCHACensusTractsAnalysis.censusTracyArrayLength) + " Census Tract(s):")
print("Percentage of older males age 65+ who received core preventive services: " + "{:.1f}".format(NYCHACensusTractsAnalysis.coreMenPercentage) + "%")  #print out with one decimal place
print("Percentage of older females age 65+ who received core preventive services: " + "{:.1f}".format(NYCHACensusTractsAnalysis.coreWomenPercentage) + "%")
print("Percentage of older adults age 50-75 who received a colon screening: " + "{:.1f}".format(NYCHACensusTractsAnalysis.colonScreenPercentage) + "%")
print("Percentage of older females age 50-74 who received a mammogram: " + "{:.1f}".format(NYCHACensusTractsAnalysis.mammoUsePercentage) + "%")
print("Percentage of older adults age 65+ who have all teeth lost: " + "{:.1f}".format(NYCHACensusTractsAnalysis.teethLostPercentage) + "%")
NYCHACensusTractsAnalysis.exportValues("NYCHA_Data2.csv") #output the data to a CSV file