#Geek task1
print('该程序会根据您输入的 a值 以及你定义的 精度 输出该函数在（0，1）的函数值')
print('              y\'+y=0')
print('              y0=a')


x=0
fx=float(input('请输入a的值:'))
dx=float(input('请输入精度:'))
step=int(1/dx)

for i in range(0,step):
    x=x+dx
    xn=str(x)
    fx=fx-fx*dx
    print('当x='+'{0:.4}'.format(xn)+'时，y='+'{0:.3}'.format(fx))