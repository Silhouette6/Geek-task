#Geek task1
print('该程序会根据您输入的 a值=3 以及你定义的 精度dx=0.001 输出该函数在（0，1）的函数值')
print('              y\'+y=0')
print('              y0=a')


x=0
fx=3
dx=0.001
step=int(1/dx)

for i in range(0,step):
    x=x+dx
    xn=str(x)
    fx=fx-fx*dx
    print('当x='+'{0:.4}'.format(xn)+'时，y='+'{0:.3}'.format(fx))
