#可看做扩展Python的list
import numpy as np
#画图工具
import matplotlib.pyplot as plt
#[0,3]之间的19等分点数组
x=np.linspace(start=0,stop=3,num=20,dtype=float)
#[0,9]之间的19等分点数组
y=np.linspace(start=0,stop=9,num=20,dtype=float)
#画在画布上,点图
plt.plot(x,y,'v')
#显示画布
plt.show()