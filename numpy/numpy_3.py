#可看做扩展Python的list
import numpy as np
#画图工具
import matplotlib.pyplot as plt
#随机生成一个30*30的[0,1)的随机数表
image = np.random.rand(30, 30)
#把该数表显示为一个热量图
plt.imshow(image, cmap=plt.cm.rainbow)
#显示热力指示条
plt.colorbar()
#显示画布
plt.show()
