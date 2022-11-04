#    2. You can use Cramer’s rule to solve the following 2 × 2 system of linear equation:
#ax + by = e
#cx + dy = f
#x = (ed - bf) / (ad - bc)
#y = (af -ec) / (ad - bc)2

def cramerRule(a,b,c,d,e,f)->None:
    if (a*d)-(b*c) == 0:
        print('The has no solution')
    else:
        t=(a*d)-(b*c)

        x=((e*d)-(b*f))/t
        y=((a*f)-(e*c))/t

        e = (a * x) + (b * y)
        f = (c * x) + (d * y)
        print('The value of x is ',round(x,1),'and y is',round(y,1))
a = eval(input('enter value of a:'))
b = eval(input('enter value of  b:'))
c = eval(input('enter value of c:'))
d = eval(input('enter value of d:'))
e = eval(input('enter value of e:'))
f = eval(input('enter value of f:'))
cramerRule(a,b,c,d,e,f)