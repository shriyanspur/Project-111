import plotly.figure_factory as pf
import plotly.graph_objects as go
import statistics as st
import random
import pandas as pd
import csv

df = pd.read_csv('studentMarks.csv')
data = df['Math_score'].tolist()

mean = st.mean(data)
stDev = st.stdev(data)

print('Mean:',mean)
print('Standard Deviation:', stDev)

def randSetofMeans(limit):
  dataSet = []
  for i in range(0, limit):
    randIndex = random.randint(0, len(data)-1)
    value = data[randIndex]
    dataSet.append(value)

  mean = st.mean(dataSet)

  return mean

meanList = []

for i in range(0, 1000):
  setofMean = randSetofMeans(100)
  meanList.append(setofMean)

stDevMeanList = st.stdev(meanList)
meanMeanList = st.mean(meanList)

print('Mean:', meanMeanList)
print('Standard Deviation:', stDevMeanList)

stDev1Start, stDev1End = mean - stDevMeanList, mean + stDevMeanList
stDev2Start, stDev2End = mean - (2*stDevMeanList), mean + (2*stDevMeanList)
stDev3Start, stDev3End = mean - (3*stDevMeanList), mean + (3*stDevMeanList)


df1 = pd.read_csv('School1.csv')
data1 = df1['Math_score'].tolist()
mean1 = st.mean(data1)
print('Mean of Sample 1:',mean1)

fig1 = pf.create_distplot([meanList], ['Student Marks'], show_hist=False)
fig1.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.1], mode = 'lines', name = 'Mean of students (tab)'))
fig1.add_trace(go.Scatter(x = [mean1, mean1], y = [0, 0.1], mode = 'lines', name = 'Mean of samplelist'))
fig1.add_trace(go.Scatter(x = [stDev1End, stDev1End], y = [0, 0.1], mode = 'lines', name = 'First Dev End'))
fig1.show()


df2 = pd.read_csv('School2.csv')
data2 = df2['Math_score'].tolist()
mean2 = st.mean(data2)
print('Mean of Sample 2:',mean2)

fig2 = pf.create_distplot([meanList], ['Student Marks'], show_hist=False)
fig2.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.1], mode = 'lines', name = 'Mean of students (extra classes)'))
fig2.add_trace(go.Scatter(x = [mean2, mean2], y = [0, 0.1], mode = 'lines', name = 'Mean of samplelist 2'))
fig2.add_trace(go.Scatter(x = [stDev2End, stDev2End], y = [0, 0.1], mode = 'lines', name = 'Second Dev End'))
fig2.show()


df3 = pd.read_csv('School3.csv')
data3 = df3['Math_score'].tolist()
mean3 = st.mean(data3)
print('Mean of Sample 3:',mean3)

fig3 = pf.create_distplot([meanList], ['Student Marks'], show_hist=False)
fig3.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.1], mode = 'lines', name = 'Mean of students (fun sheet)'))
fig3.add_trace(go.Scatter(x = [mean3, mean3], y = [0, 0.1], mode = 'lines', name = 'Mean of samplelist 3'))
fig3.add_trace(go.Scatter(x = [stDev3End, stDev3End], y = [0, 0.1], mode = 'lines', name = 'Third Dev End'))
fig3.show()


z_score1 = (mean1-mean)/stDev
print('Z_scoreOfSample1:',z_score1)

z_score2 = (mean2-mean)/stDev
print('Z_scoreOfSample2:',z_score2)

z_score3 = (mean3-mean)/stDev
print('Z_scoreOfSample3:',z_score3)