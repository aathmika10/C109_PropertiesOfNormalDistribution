import csv 
import pandas as pd
import statistics
import plotly.figure_factory as ff

df=pd.read_csv("HeightWeight.csv")
height=df["Height(Inches)"].to_list()
weight=df["Weight(Pounds)"].to_list()

#height data
mean= statistics.mean(height)
median=statistics.median(height)
stdDev=statistics.stdev(height)
mode=statistics.mode(height)

print("mean, meadian, mode, standard deviation of height is {},{},{},{}".format(mean,median,mode,stdDev))

FirstStart,FirstEnd= mean-stdDev,mean+stdDev
SecondStart,SecondEnd= mean-(2*stdDev),mean+(2*stdDev)
ThirdStart,ThirdEnd= mean-(3*stdDev),mean+(3*stdDev)
listOf1stStdDev=[result for result in height if result>FirstStart and result<FirstEnd]
listOf2ndStdDev=[result for result in height if result>SecondStart and result<SecondEnd]
listOf3rdStdDev=[result for result in height if result>ThirdStart and result<ThirdEnd]

print("{}% of data lies within 1 standard deviation".format(len(listOf1stStdDev)*100.0/len(height)))
print("{}% of data lies within 2 standard deviation".format(len(listOf2ndStdDev)*100.0/len(height)))
print("{}% of data lies within 3 standard deviation".format(len(listOf3rdStdDev)*100.0/len(height)))