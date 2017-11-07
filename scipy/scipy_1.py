import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

# 线性代数操作
# 行列式的值
arr1=np.array([[1,2],
             [3,4]])
arr1_value=linalg.det(arr1)
print("行列式 \n",arr1,"\n的值为 \n",arr1_value )
print('-'*20)

arr2=np.array([[1,2],
             [3,4]])
arr2_value=linalg.inv(arr2)
print("矩阵 \n",arr2,"\n的逆矩阵为 \n",arr2_value )
print('-'*20)

arr3=np.array([[5,6],
             [7,8]])
arr3_value=arr1.dot(arr3)
print("矩阵 \n",arr1,"\n 和矩阵 \n",arr3,"\n 的乘积为 \n",arr2_value )
print('-'*20)

