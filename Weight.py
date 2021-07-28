import csv 
import pandas as pd
import statistics
import plotly.figure_factory as ff

df=pd.read_csv("HeightWeight.csv")
weight=df["Weight(Pounds)"].to_list()

#weight data
mean= statistics.mean(weight)
median=statistics.median(weight)
stdDev=statistics.stdev(weight)
mode=statistics.mode(weight)

print("mean, meadian, mode, standard deviation of weight is {},{},{},{}".format(mean,median,mode,stdDev))

FirstStart,FirstEnd= mean-stdDev,mean+stdDev
SecondStart,SecondEnd= mean-(2*stdDev),mean+(2*stdDev)
ThirdStart,ThirdEnd= mean-(3*stdDev),mean+(3*stdDev)
listOf1stStdDev=[result for result in weight if result>FirstStart and result<FirstEnd]
listOf2ndStdDev=[result for result in weight if result>SecondStart and result<SecondEnd]
listOf3rdStdDev=[result for result in weight if result>ThirdStart and result<ThirdEnd]

print("{}% of data lies within 1 standard deviation".format(len(listOf1stStdDev)*100.0/len(weight)))
print("{}% of data lies within 2 standard deviation".format(len(listOf2ndStdDev)*100.0/len(weight)))
print("{}% of data lies within 3 standard deviation".format(len(listOf3rdStdDev)*100.0/len(weight)))

fig=ff.create_distplot([weight],["Weight"], show_hist=False)
fig.show()