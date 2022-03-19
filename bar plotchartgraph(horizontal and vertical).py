import matplotlib.pyplot as plt
import numpy as np
'''
i ahve to create bar plot now
horizontal bar plot
vertical bar plot
bar()-->vertical plot
barh()-->horizontal plot
data is represented wityh the help of horizontal bar-->we have rectangular bars
'''
x=['A','B','C','D']
y=[10,20,30,40]
plt.bar(x,y,color='r',width=0.5)
#by default width=0.8
colors=['r','g','b','m']
plt.barh(x,y,color=colors,height=0.3)
plt.xlabel("x-axis-->")
plt.ylabel("y-axis-->")
plt.title("PALCEMENT")

plt.show()
