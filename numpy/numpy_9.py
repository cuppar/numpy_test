import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np

plt.axis('off') # 不显示坐标轴

lena = mpimg.imread('../images/lena.png') # 读取images目录下的 lena.png
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
print(lena.shape) # (512, 512, 3)

lena_r = lena[:,:,0]
plt.imshow(lena_r) # 显示图片
plt.savefig("lena_r") # 保存在lena_r.png中

lena_g = lena[:,:,1]
plt.imshow(lena_g) # 显示图片
plt.savefig("lena_g") # 保存在lena_g.png中

lena_b = lena[:,:,2]
plt.imshow(lena_b) # 显示图片
plt.savefig("lena_b") # 保存在lena_b.png中

def rgb2grey(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

lena_grey=rgb2grey(lena)
plt.imshow(lena_grey,cmap="Greys_r")
plt.savefig("lena_grey")

plt.imshow(lena_grey,cmap='hot')
plt.savefig("lena_hot")

