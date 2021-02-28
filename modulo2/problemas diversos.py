def vint_num(c):
    '''
    validar un entero

    Parameters
    ----------
    c=str
    Returns
    -------
    n=int
    '''
    while True:
        try:
            n=int(input(f"{c} "))
            return n
        except:
         print("error , ingrese de nuevo")

def vfloat_num(c):
    '''
    validar un flotante/racional

    Parameters
    ----------
    c=str
    Returns
    -------
    n=float
    '''
    while True:
        try:
            n=float(input(f"{c} "))
            return n
        except:
         print("error , ingrese de nuevo")


#numero 1
def alumnos(f,g,h):
  D="numeros de alumnos="
  d=vint_num(D)

  for i in range(d):
      a=input(f"nombre del {1+i} alumno=  ")
      f.append(a)

  for i in f:
      print(f[f.index(i)])
      for j in range(3):
       B=f"{j + 1} nota del  alumno="
       b =vfloat_num(B)

       while True:
           if 0 <= b <= 10:
              g.append(b)
              break
           else:
              print()
              print("valor invalido ingrese de nuevo")
              print(f[f.index(i)])
              b=float(input(f"{j + 1} nota del  alumno= "))

  for i in range(0, len(g), 3):
      h.append(g[i:i+3])
  print()
  print(f)
  print(h)
f=[]
g=[]
h=[]

alumnos(f,g,h)

#numero 2
def evalua(g,a):
  t=0
  u=0
  for k in range(0, len(g), 3):
     a.append(round(sum(g[k:k+3])/3,4))
  print(a)
  for i in a:
     if 4<=i:
        t+=1
     if i<4:
        u+=1
  print(f"Desaprobaron {u}")
  print(f"Aprobaron {t}")

print()
a=[]
evalua(g,a)


#numero 3
def promedio(a):
 print("Promedio de nota del curso total= ",sum(a)/len(a))
 print()
promedio(a)

#numero 4
def pro_alto(a,nu):
  mayor=max(a)
  menor=min(a)

  gu=[i for i in range(len(a))]

  for i in gu:
      for j in a:
         nu[i]=j
         a.remove(j)
         break

  for i in nu:
      if nu[i]==mayor:
         print(f"La maxima nota es de {f[i]}")
      elif nu[i]==menor:
         print(f"La minima nota es de {f[i]}")
nu={}
pro_alto(a,nu)

#numero 5
def nombre(f,h,nu):
  ga=[i for i in range(len(f))]
  na={}
  for i in ga:
      for j in f:
         na[i]=j
         f.remove(j)
         break

  nombre=input("ingrese el nombre del alumno:")
  for i in na :
    if na[i]==nombre:
        print(nombre)
        print(f"Nota promedio: {nu[i]}\n Notas: {h[i]}")
    elif na[i]!=nombre:
        print()
print()
nombre(f,h,nu)






















"""

#numero 1

D="numeros de alumnos="
d=vint_num(D)
f=[]
for i in range(d):
    a=input(f"nombre del {1+i} alumno=  ")
    f.append(a)
g=[]
for i in f:
    print(f[f.index(i)])
    for j in range(3):
     B=f"{j + 1} nota del  alumno="
     b =vfloat_num(B)

     while True:
         if 0 <= b <= 10:
            g.append(b)
            break
         else:
            print()
            print("valor invalido ingrese de nuevo")
            print(f[f.index(i)])
            b=float(input(f"{j + 1} nota del  alumno= "))
h=[]
for i in range(0, len(g), 3):
    h.append(g[i:i+3])
print()
print(f)
print(h)

print()
#numero 2
t=0
u=0
a=[]
for k in range(0, len(g), 3):
   a.append(round(sum(g[k:k+3])/3,4))
print(a)
for i in a:
   if 4<=i:
      t+=1
   if i<4:
      u+=1
print(f"Desaprobaron {u}")
print(f"Aprobaron {t}")

print()
#numero 3
print("Promedio de nota del curso total= ",sum(a)/len(a))
print()
#numero 4
mayor=max(a)
menor=min(a)

gu=[i for i in range(len(a))]
nu={}
for i in gu:
    for j in a:
       nu[i]=j
       a.remove(j)
       break

for i in nu:
    if nu[i]==mayor:
       print(f"La maxima nota es de {f[i]}")
    elif nu[i]==menor:
       print(f"La minima nota es de {f[i]}")

#numero 5
print()
ga=[i for i in range(len(f))]
na={}
for i in ga:
    for j in f:
       na[i]=j
       f.remove(j)
       break

nombre=input("ingrese el nombre del alumno:")
for i in na :
  if na[i]==nombre:
      print(nombre)
      print(f"Nota promedio: {nu[i]}\n Notas: {h[i]}")
  elif na[i]!=nombre:
      print()





"""



