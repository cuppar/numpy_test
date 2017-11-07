import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(12,20)
y = np.random.randn(12,20)
mark = ['s','o','^','v','>','<','d','p','h','8','+','*']
for i in range(0,12):
    plt.scatter(x[i],y[i],marker = mark[i],color =(np.random.rand(1,3)),s=100,label = str(i+1))
    plt.show()
plt.legend()
# plt.show()