def lagrange(x_list,y_list,x):
    n= len(x_list)
    result = 0
    for i in range(0,n):
        L=1
        for j in range(0,n):
            if i!=j:
                L*=(x-x_list[j])/(x_list[i]-x_list[j])
        result+=y_list[i]*L
    return result
x_list = [2, 7, 10, 12]
y_list = [4, 49, 100, 144]
for i  in range(len(x_list)):
    print(f"({x_list[i]},{y_list[i]})")
x=5
y = lagrange(x_list,y_list,x)
print({y})