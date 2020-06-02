
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def primeNumbers(N):
    
    intersects=[0]*N
    index = [0]*N
    for i in range(1,N):
        count=1
        index[i]=i
        while i*count<N:
            intersects[i*count]+=1
            count+=1
    print(intersects)
    print(index)
    plt.plot(index,intersects)
    plt.show()
    # plt.bar(len(intersects), np.array(intersects) )
primeNumbers(200)



# from numpy import *
# import numpy as np
# import math
# import matplotlib.pyplot as plt
# x = np.linspace(1,30,1000)

# # the function, which is y = sin(x) here
# y = np.sin(np.pi*x)
# i = np.linspace(2,30,1000)
# y2 = np.sin(np.pi*x*(1/2))
# y3 = np.sin(np.pi*x*(1/3))
# y4 = np.sin(np.pi*x*(1/4))
# y5 = np.sin(np.pi*x*(1/5))
# # setting the axes at the centre
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['left']
# ax.spines['bottom'].set_position('center')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')

# # plot the function
# plt.plot(x,y, 'c-')
# plt.plot(x,y2, 'r-')
# plt.plot(x,y3, 'g-')
# plt.plot(x,y4, 'y-')
# plt.plot(x,y5, 'b-')
# # show the plot
# plt.show()
            
    