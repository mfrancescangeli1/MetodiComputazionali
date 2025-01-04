import somme as sm
n=input('scrivi numero naturale ')
n=int(n)
s=sm.sum(n)
sq=sm.sumradq(n)
print(s,sq )
print("\n")
ss, pp=sm.sumprod(n)
print( ss, pp)

print("\n")
a=input("alfa= ")
a=float(a)
salfa=sm.sumalfa(n,a)
print(salfa)

