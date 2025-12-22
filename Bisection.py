def bisection(f,a,b,tol=1e-6,iteration=100):
   if f(a) * f(b) >0:
      return None,0
   
   c=None
   prev_c = None
   iter =0
   for i in range(iteration):
      iter+=1
      c=(a+b)/2
      if prev_c==c or abs(f(c))<tol:
         break
      prev_c = c
      if f(a) * f(c) > 0:
         
         a=c
      else:
    
         b=c

   return c , iter


def f1(x):
   return x**2 -4

# a1 = float(input("enter a: "))
# b1 = float(input("enter b: "))

r , i = bisection(f1,0,3)
print(f"Root found:{r:.6f}")
print(f"itertion:{i}")
print(f"f({r:.6f}) = {f1(r):.10f}")


          


   
         


