# APC
valores = input().split()
a= int(valores[0])
b= int(valores[1])
d= int(valores[2])

x = input().split()
e = int(x[0])
f = int(x[1])
g = int(x[2])

y = input().split()
h = int(y[0])
i = int(y[1])
j = int(y[2])

def resto(a,b,d):
  coisa= (a+b)%d
  print(coisa)

resto(a,b,d)
resto(e, f, g)
resto(h, i, j)
