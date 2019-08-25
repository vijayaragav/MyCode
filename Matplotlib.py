import matplotlib.pyplot as plt
plt.plot([2,4,6,8], [5,6,9,12])
plt.xlabel('Road')
plt.ylabel('Cars')
plt.title('Pyplot')
plt.show()

import matplotlib.pyplot as plt
from matplotlib import style
plt.plot([2,4,6,8], [5,6,9,12],'r',label='Curve', linewidth='5')
plt.legend()
plt.grid(True, color='k')
plt.xlabel('Road')
plt.ylabel('Cars')
plt.title('Pyplot')
plt.show()

import matplotlib.pyplot as plt
from matplotlib import style
plt.bar([2,4,6,8], [5,6,9,12],color='r',label='Curve')
plt.legend()
plt.grid(True, color='k')
plt.xlabel('Road')
plt.ylabel('Cars')
plt.title('bar')
plt.show()

import matplotlib.pyplot as plt
from matplotlib import style
plt.hist([2,4,6,8,12,15,9,20,25,30], [5,6,9,12],color='r', histtype='bar', rwidth=0.11, label='Curve')
plt.legend()
plt.grid(True, color='k')
plt.xlabel('Road')
plt.ylabel('Cars')
plt.title('hist')
plt.show()

import matplotlib.pyplot as plt
from matplotlib import style
plt.scatter([2,4,6,8,12,15,19], [5,6,9,12,20,25,30],color='r', label='Curve')
plt.legend()
plt.grid(True, color='k')
plt.xlabel('Road')
plt.ylabel('Cars')
plt.title('Scatter')
plt.show()


import matplotlib.pyplot as plt
from matplotlib import style
plt.stackplot([2,4,6,8], [5,6,9,12], color='r')
plt.legend()
plt.grid(True, color='k')
plt.xlabel('Road')
plt.ylabel('Cars')
plt.title('area')
plt.show()

import matplotlib.pyplot as plt
from matplotlib import style
x = [2,4,6,8]
y = ['Eat', 'play', 'study', 'sleep']
cols = ['r', 'm', 'y', 'g']
plt.pie(x, labels=y, colors=cols, shadow=True, explode=(0,0.1,0,0), autopct='%1.0f%%')
plt.legend()
plt.grid(True, color='k')
plt.title('pie')
plt.show()