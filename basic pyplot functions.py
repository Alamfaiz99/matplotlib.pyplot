import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[1,2,3,4]
plt.rcParams['figure.figsize']=[7.5,3.5]
plt.rcParams['figure.autolayout']=True
#only we have to write marker=""/'
'''
marker-are used to fepresnet points in a chart/graph
o-circle
s-square Sx-cross
D/d-diamond
P-pentagon
h-hexagon
.-point
*-star
+-plus
|-vline-->vertical line
-->Hline-->horizontal line
'''
plt.plot(x,y,marker="h",label='A')
plt.xlabel('x-axis-->')
plt.ylabel('y-axis-->')
plt.title('RANDOM GRAPH')
plt.legend(loc='upper center')
#we have to use legend after plotting the graph 
plt.show()
