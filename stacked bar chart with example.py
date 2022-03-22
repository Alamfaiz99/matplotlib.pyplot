import matplotlib.pyplot as plt
import numpy as np
'''
what is stacked bar chart-->representing one category after anorther cateory


'''
years=['2017','2018','2019','2020']
placements=[150,120,158,147]

cse=[40,50,30,90]
it=[87,40,20,50]
ece=[65,70,76,20]
ece_start=[cse[i]+it[i] for i in range(len(cse))]

plt.title('Placement comparision')
plt.bar(years,placements,width=0.4)
plt.bar(years,cse,width=0.4,label='cse')
plt.bar(years,it,width=0.4,bottom=cse,label='it')
plt.bar(years,ece,width=0.4,bottom=ece_start,label='ece')
plt.ylim(0,300)
plt.legend(loc='upper center')
plt.show()
