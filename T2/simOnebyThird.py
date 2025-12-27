def simpson_1_3(f,a,b,n):
    h = (b-a)/n

    acc_even = 0
    acc_odd = 0
    for i in range(1,n):
        xi = a+i*h
        if i % 2 ==0:
            acc_even+=f(xi)
        else:
            acc_odd+=f(xi)

    integral = (h/3) * (f(a)+f(b)+4*acc_odd + 2*acc_even)
    return integral

def f1(x):
    return x**2 +1
a,b = 0,2
n=6
exect_value = 4.6667

result  = simpson_1_3(f1,a,b,n)

print(f'{(b-a)/n}')
print(f"{result:.10f}")
print(f"{abs(result - exect_value):.10f}")