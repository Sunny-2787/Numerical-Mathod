def newtondivided(x_list,y_list,x):
    n = len(x_list)-1
    f=[]
    
   
    for i in range(n+1):
        f.append([0.0]  * (n+1))
    for i in range(n+1):
        f[i][0]=y_list[i]
    for j in range(1,n+1):
        for i in range(n-j+1):
            numerator = f[i+1][j-1]-f[i][j-1]
            dominator = x_list[i+j] - x_list[i]
            f[i][j] = numerator/dominator

    print("-"*75)
    for i in f:
        print([f"{val:0.6f}" for val in  i])
    print("-"*60)

    p=f[0][0]
    for i in range(1,n+1):
        pd = 1
        for j in range(i):
            pd*=(x-x_list[j])

        p =p +f[0][i]*pd

    return p


x_list = [2, 7, 10, 12]
y_list = [4, 49, 100, 144]

for i in range (len(x_list)):
    print(f"({x_list[i]} , {y_list[i]})")

x=9
y=newtondivided(x_list,y_list,x)

print({y})
