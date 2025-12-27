def forward_method(f,x,h):
    f_forward = f(x+h)
    f_current = f(x)

    d = (f_forward-f_current)/h
    return d
def f1(x):
    return x**2 -2
x_point =2
step_size = 0.01
true_value = 4

d1 = forward_method(f1,x_point,step_size)
print(d1)
print (f"{abs(d1-true_value):.10f}")
