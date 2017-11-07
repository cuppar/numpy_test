# 安装 pip install numpy
# 导入 import numpy as np
# 在高效大量计算前提下的list不方便，numpy某种意义上扩展Python的list
import numpy as np

def title(str):
    print("##### ",str," #####")
def end():
    print("-" * 50)

title("数据类型")
print("列表元素的数据类型可以不一致，数组不可以。")
print("列表 ",['a',1,2,3,"字符串"])
end()

# 手动生成一个数组,**数据类型必须一致！**
title("手动创建数组")
a1=np.array([0,1,2,3])
print("a1 = ",a1)
end()

a2=np.array([[[1],[2]],[[3],[4]]])
print("a2 = \n",a2)
print("a2.ndim = ",a2.ndim,"  --N尺寸，维度")
print("a2.shape = ",a2.shape,"  --外形（向量）")
print("len(a2) = ",len(a2),"  --最后一个维度的长")
end()

# 自动生成一个数组
title("arange()自动生成数组")
b1=np.arange(10)
print("b1 = \n",b1)
print("b1.ndim = ",b1.ndim,"  --N尺寸，维度")
print("b1.shape = ",b1.shape,"  --外形（向量）")
print("len(b1) = ",len(b1),"  --最后一个维度的长")
end()

b2=np.arange(1,9,2)
print("b2 = \n",b2)
end()

b3=np.linspace(0,1,6)
print("b3 = \n",b3)
end()

# 其他数组
title("常用数组")
c1=np.ones((3,3))
print("c1 = \n",c1)
end()

c2=np.zeros((2,2))
print("c2 = \n",c2)
end()

c3=np.eye(3)
print("c3 = \n",c3)
end()

c4=np.diag(np.array([1,2,3,4]))
print("c4 = \n",c4)
end()

# 随机数
title("随机")
# [0,1)伪随机，均匀分布
d1=np.random.rand(4)
print("d1 = \n",d1)
end()

# 高斯随机，正态分布随机
d2=np.random.randn(4)
print("d2 = \n",d2)
end()

# 设置随机种子
# np.random.seed(1234)

# 设置数据类型
e=np.array([1,2,3],dtype=int)
print("e = \n",e)
print("e.dtype = ",e.dtype)
end()






