def Trapoziodal(f,a,b,n):
    h = (b-a)/n
    acc =   0
    for i in range(1,n):
        xi = a+i*h
        acc+=f(xi)
        
    integral = (h/2) * (f(a) + 2*acc +f(b))
    return integral

def f1(x):
    return x**2 +1
a,b = 0,2
n=30
exect_value = 4.6667

result  = Trapoziodal(f1,a,b,n)

print(f'{(b-a)/n}')
print(f"{result:.10f}")
print(f"{result - exect_value}")





