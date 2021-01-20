import statistics;
import csv;
import pandas;
import plotly.graph_objects as go;
import plotly.figure_factory as ff;
df = pandas.read_csv("Data.csv")
math_score = df["reading score"]
mean = statistics.mean(math_score)
median = statistics.median(math_score)
mode = statistics.mode(math_score)
print("mean: ",mean)
print("median: ",median)
print("mode: ",mode)
std = statistics.stdev(math_score)
first_std_start,first_std_end = mean-std,mean+std
sec_std_start,sec_std_end = mean-(2*std),mean+(2*std)
th_std_start,th_std_end = mean-(3*std),mean+(3*std)
fig = ff.create_distplot([math_score],["reading score"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y=[0,0.17],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x = [first_std_start],y=[0,0.17],mode="lines",name="standard deviation"))
fig.add_trace(go.Scatter(x = [first_std_end],y=[0,0.17],mode="lines",name="standard deviation"))
fig.add_trace(go.Scatter(x = [sec_std_start],y=[0,0.17],mode="lines",name="standard deviation"))
fig.add_trace(go.Scatter(x = [sec_std_end],y=[0,0.17],mode="lines",name="standard deviation"))
fig.add_trace(go.Scatter(x = [th_std_start],y=[0,0.17],mode="lines",name="standard deviation"))
fig.add_trace(go.Scatter(x = [th_std_end],y=[0,0.17],mode="lines",name="standard deviation"))
# percentage calculating::
data_first_std = [result for result in math_score if result>first_std_start and result<first_std_end]
data_sec_std   = [result for result in math_score if result>sec_std_start and result<sec_std_end]
data_third_std = [result for result in math_score if result>th_std_start and result<th_std_end]
print("{}% of first std: ".format(len(data_first_std)*100.0/len(math_score)))
print("{}% of secod std: ".format(len(data_sec_std)*100.0/len(math_score)))
print("{}% of third std: ".format(len(data_third_std)*100.0/len(math_score)))
fig.show()