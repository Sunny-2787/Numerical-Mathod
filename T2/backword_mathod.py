def backword_method (f,x,h):
    f_backword = f(x-h)
    f_current = f(x)
    d = (f_current - f_backword)/h
    return d
def f1(x):
    return x**2 -2
x_point = 2
size = 0.01
true_value = 4
d1=backword_method(f1,x_point,size)
print(f" {d1:.10f}")
print(f"{abs(d1  - true_value):.10f}")

