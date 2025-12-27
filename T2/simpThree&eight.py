def simp_3_8(f,a,b,n):
    h = (b-a)/n
    acc_not_3 = 0
    acc_yes_3 = 0
    for i in range(1,n):
        xi = a+i*h
        if i%3 !=0:
            acc_not_3+=f(xi)
        else:
            acc_yes_3+=f(xi)

    integral = (3*h / 8) *(f(a)+f(b)+ 3*acc_not_3 + 2 *acc_yes_3)
    return integral
def f1(x):
    return x**2 +1
a,b = 0,2
n=6
exect_value = 14/3

result  = simp_3_8(f1,a,b,n)

print(f'{(b-a)/n}')
print(f"{result:.10f}")
print(f"{exect_value:.10f}")
print(f"{abs(result - exect_value):.10f}")
