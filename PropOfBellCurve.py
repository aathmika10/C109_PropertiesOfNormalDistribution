import random
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

diceResult=[]
count=[]

for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceResult.append(dice1+dice2)
    count.append(i)

mean=sum(diceResult)/len(diceResult)
stdDev=statistics.stdev(diceResult)
median=statistics.median(diceResult)
mode=statistics.mode(diceResult)

print("mean: ",mean)
print(stdDev)
print(median)
print(mode)

FirstStart,FirstEnd= mean-stdDev,mean+stdDev
SecondStart,SecondEnd= mean-(2*stdDev),mean+(2*stdDev)
ThirdStart,ThirdEnd= mean-(3*stdDev),mean+(3*stdDev)

listOf1stStdDev=[result for result in diceResult if result>FirstStart and result<FirstEnd]
listOf2ndStdDev=[result for result in diceResult if result>SecondStart and result<SecondEnd]
listOf3rdStdDev=[result for result in diceResult if result>ThirdStart and result<ThirdEnd]

print("{}% of data lies within 1 standard deviation".format(len(listOf1stStdDev)*100.0/len(diceResult)))
print("{}% of data lies within 2 standard deviation".format(len(listOf2ndStdDev)*100.0/len(diceResult)))
print("{}% of data lies within 3 standard deviation".format(len(listOf3rdStdDev)*100.0/len(diceResult)))

fig=ff.create_distplot([diceResult],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[FirstStart, FirstStart],y=[0,0.17],mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[FirstEnd,FirstEnd],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[SecondStart, SecondStart],y=[0,0.17],mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[SecondEnd,SecondEnd],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))
fig.show()