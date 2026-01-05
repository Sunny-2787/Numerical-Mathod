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

def isStrictlyDiagonallyDominant(A):
    n = len(A)
    domineance = True
    for i in range(n):
        diagonal = abs(A[i][i])
        sum_of_diagnal = 0
        for j in range(n):
            if j!=i:
                sum_of_diagnal+=abs(A[i][j])

        if diagonal<=sum_of_diagnal:
            domineance=False
       
    return domineance

def jacobiMethod(A,b,x0 ,tol = 1e-3,iteration =100):
    if isStrictlyDiagonallyDominant(A):
        print("Will coverage")
    else:
        print("Not coverge")
    
    n= len(A)
    if x0 is None:


        
        x = [0.0]*n
    else:
        x = x0.copy()
    x_new =[0.0]*n
    iter = 0
    for k in range(iteration):
        for i in range(n):
            sum_of_diagnal = 0
            for j in range(n):
                if j!=i:
                    sum_of_diagnal+=A[i][j] *x[j]
            x_new[i] = (b[i] - sum_of_diagnal) / A[i][i]

        conver = True
        for i in range(n):
            if abs(x_new[i]-x[i])>tol:
                conver = False
                break
        x=x_new.copy()
        iter+=1
        if conver:
            break
    return x,iter




def gausee_seidal(A,b,x0 ,tol = 1e-3,iteration =100):
    if isStrictlyDiagonallyDominant(A):
        print("Will coverage")
    else:
        print("Not coverge")
    n = len(A)
    if x0 is None:
        x=[0.0]*n
    else:
        x= x0.copy()

    iter = 0
    for k in range(iteration):
        x_old = x.copy()
        for i in range(n):
            sum_terms  = 0
            for j in range(i):
                sum_terms+=A[i][j] * x[j]
            
            for j in range(i+1,n):
                sum_terms+=A[i][j] * x_old[j]
            
            x[i] = (b[i]-sum_terms)/A[i][i]

        convergance = True
        for i in range(n):
            if abs(x[i]-x_old[i]>tol):
                convergance=False
                break
        iter+=1
        if convergance:
            break
    return x,iter

A = [
    [10, 1, 1],
    [1, 10, 1],
    [1, 1, 10]
]
b = [12, 12, 12]

x0 = [0, 0, 0]

x1 ,iter1  = jacobiMethod(A,b,x0)
x1 ,iter1  = gausee_seidal(A,b,x0)
print(x1)
print(iter1)




