#求解一元二次方程

print('解ax²+bx+c=0')
co = 'abc'
ls = [0,0,0]
for i in range(3):
    z = str(co[i])
    ls[i] = eval(input("请输入{0:}的值:".format(z)))
a,b,c = ls[0],ls[1],ls[2]
det = pow(b,2)-4*a*c
def solve():
    if det<0:
        print('方程无实数根')
    else:
        x1 = (-b+pow(det,1/2))/(2*a)
        x2 = (-b-pow(det,1/2))/(2*a)
        if det==0:
            print('x1=x2={0:.6f}'.format(x1))
        else:
            print('x1={0:.6f},x2={1:.6f}'.format(x1,x2))

def main():
    if a==0:
        if b==0:
            print('这不是方程！')
        else:
            print('x={0:}'.format(-c/b))
    else:
        solve()
main()
