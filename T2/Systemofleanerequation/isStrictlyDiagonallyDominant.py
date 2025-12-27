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