def Falsi(f,a,b,tol=1e-6,itertion =100):
    if f(a)*f(b)>0:
        return None,0
    c=None
    prev_c = None
    iter = 0
    for i in range (itertion):
        iter+=1
        c= b-f(b)*((b-a)) / (f(b) - f(a))
        if c == prev_c or abs(f(c))<tol:
            break
        prev_c = c
        if f(a)*f(c)>0:
            a=c
        else:
            b=c
    return c , iter

def f1(x):
    return x**2 - 4




r,i = Falsi(f1,0,3)
print(f"{r:.6f}")
print(i)
print(f"({r:.6f}) : {f1(r):.10f}")