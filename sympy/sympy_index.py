from  sympy import *

def title(str):
    print("##### ",str," #####")
def end():
    print("-" * 50)

# 分数
a = Rational(1,2)
title("分数 Rational")
print("a = Rational(1,2) --> ",a)
print("a*2 --> ",a*2)
end()

title("pi和e")
print("pi**2 --> ",pi**2)
print("pi.evalf() --> ",pi.evalf())
print("exp(1) --> ",exp(1))
print("exp(1).evalf() --> ",exp(1).evalf())
end()

title("无穷 oo")
print("oo > 9999 --> ",oo > 9999)
print("oo+1 --> ",oo+1)
end()

title("符号 Symbol")
x=Symbol('x')
y=symbols('y')
print("Symbol('x') --> ",x)
print("symbols('y') --> ",y)
print("x+y+x-y --> ",x+y+x-y)
print("(x+y)**2 --> ",(x+y)**2)
end()

title("展开 expand")
print("幂级数 expand((x+y)**3) --> ",expand((x+y)**3))
print("幂级数 3*x*y**2 + 3*y*x**2 + x**3 + y**3 --> ",3*x*y**2 + 3*y*x**2 + x**3 + y**3)
print("复数 expand(x + y, complex=True) --> ",expand(x + y, complex=True))
print("复数 I*im(x)+I*im(y)+re(x)+re(y) --> ",I*im(x)+I*im(y)+re(x)+re(y))
print("三角函数 expand(cos(x + y), trig=True) --> ",expand(cos(x + y), trig=True))
print("三角函数 expand(cos(x + y), trig=False) --> ",expand(cos(x + y), trig=False))
print("三角函数 cos(x)*cos(y) - sin(x)*sin(y) --> ",cos(x)*cos(y) - sin(x)*sin(y))
end()

title("化简 simplify &替换 subs")
print("化简 simplify( (x+x*y)/x ) --> ",simplify( (x+x*y)/x ))
print("替换 subs ")
expr=x+1
print("expr=x+1 --> ",expr)
new_expr=expr.subs(x,y**2)
print("new_expr=expr.subs(x,y**2) --> ",new_expr)
end()

title("极限 limit")
print("limit(sin(x)/x,x,0) --> ",limit(sin(x)/x,x,0))
print("limit(x, x, oo) --> ",limit(x, x, oo))
print("limit(1/x, x, oo) --> ",limit(1/x, x, oo))
print("limit(x**x,x,0) --> ",limit(x**x,x,0))
end()

title("微分法 diff")
print("diff(sin(x),x) --> ",diff(sin(x),x))
print("diff(sin(2*x),x) --> ",diff(sin(2*x),x))
print("diff(tan(x), x) --> ",diff(tan(x), x))
print("验证 limit((tan(x+y) - tan(x))/y, y, 0) --> ",limit((tan(x+y) - tan(x))/y, y, 0))
end()

title("导数 diff")
print("一阶导 diff(sin(2*x),x,1) --> ",diff(sin(2*x),x,1))
print("二阶导 diff(sin(2*x),x,2) --> ",diff(sin(2*x),x,2))
print("三阶导 diff(sin(2*x),x,3) --> ",diff(sin(2*x),x,3))
end()

title("泰勒级数展开 series")
print("series(cos(x), x) --> ",series(cos(x), x))
print("series(1/cos(x), x) --> ",series(1/cos(x), x))
end()

title("积分法 integrate")
print("不定积分 integrate(6*x**5, x) --> ",integrate(6*x**5, x))
print("不定积分 integrate(log(x), x) --> ",integrate(log(x), x))
print("不定积分 integrate(2*x + sinh(x), x) --> ",integrate(2*x + sinh(x), x))
print("定积分 integrate(x**3, (x, -1, 1)) --> ",integrate(x**3, (x, -1, 1)))
print("定积分 integrate(cos(x), (x, -pi/2, pi/2)) --> ",integrate(cos(x), (x, -pi/2, pi/2)))
print("定积分 integrate(exp(-x**2), (x, -oo, oo)) --> ",integrate(exp(-x**2), (x, -oo, oo)))
end()

title("解方程 solve")
print("solve(x**4 - 1, x) --> ",solve(x**4 - 1, x))
print("方程组 solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y]) --> ",
      solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y]))
print("satisfiable(x & y) --> ",satisfiable(x & y))
print("satisfiable(x & ~x) --> ",satisfiable(x & ~x))
end()

title("解微分方程 dsolve")
f=symbols('f',cls=Function)
print("先创建一个未定义的符号函数")
print("f=symbols('f',cls=Function) --> ",f)
print("f(x) --> ",f(x))
print("f(x).diff(x, x) + f(x) --> ",f(x).diff(x, x) + f(x))
print("dsolve(f(x).diff(x, x) + f(x), f(x)) --> ",dsolve(f(x).diff(x, x) + f(x), f(x)))
end()