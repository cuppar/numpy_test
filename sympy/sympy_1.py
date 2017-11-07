# 推导 球的体积公式
from sympy import *

x,y=symbols('x,y')
r=symbols('r',positive=True)
R=symbols('R',positive=True)
# 设球心在（0,0,0）

# 求圆的面积
# 半圆的面积*2
# 半圆面积：
# x**2+y**2=r**2 --> y=sqrt(r**2-x**2)
# x在-r到r做积分
circle_area=2*integrate(sqrt(r**2-x**2),(x,-r,r))
print("圆的面积公式 --> ",circle_area)

# 求球体的体积
# 对圆的面积在x轴上做二重积分
# 把圆的半径替换为与x有关
# 切面圆与XOY面交于m,n两点
# 连接圆心与球心，球心与m,圆心与m
# 根据勾股定理
# 圆的半径r=sqrt(球的半径R**2-x**2)
# 所以把圆半径r替换为sqrt(球的半径R**2-x**2)
circle_v=integrate(circle_area.subs(r,sqrt(R**2-x**2)),(x,-R,R))
print("球的体积公式 --> ",circle_v)
