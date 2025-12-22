def Newton_rahpson(f,df,b,tol=1e-6,itertion =100):

    c=None
    prev_c = None
    iter = 0
    for i in range (itertion):
        iter+=1
        c= b-f(b)/df(b)
       
        if c == prev_c or abs(f(c))<tol:
            break
        prev_c = c
        b=c




    return c , iter

def f1(x):
    return x**2 - 4
def d1(x):
    return 2*x

r,i = Newton_rahpson(f1,d1,3)
print(f"{r:.6f}")
print(i)
print(f"({r:.6f}) : {f1(r):.10f}")