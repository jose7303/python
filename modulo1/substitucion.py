

import string
alfa=string.ascii_lowercase

def vlile():
 while True:

     a = list(alfa)
     n = input("ingrese su nuevo abecedario= ").lower()
     verificacion = True

     for i in n:
         if i not in a:
             print("Ingresa solo letras")
             verificacion = False
             break

     if verificacion == True:
         return n


def vnuevo():
  '''
     verificar que el abecedario nuevo
      cumpla que:
       -no sea mayor que 26
        caracteres.
       -no tener caracteres repetidos.
       -todos los caracteres deben ser
         letras.
    Parameters
    ----------
    c=str
    Returns
    -------
    n=str
  '''


  while True:
      try:
         n=vlile()
         if len(n) == 26:
           if len(n) == len(set(n)):
             return n
           else:
               print("error ,hay letras iguales")
         else:
             print("error ,ingrese de nuevo")
      except:
         print("error ,ingrese de nuevo")

v=vnuevo()

t=input("ingrese su texto a cifrar: ")
c=alfa.upper()
nuevo=""
for i in t:
    if c.find(i)!=-1:
      nuevo+=c[c.find(i)]
    elif alfa.find(i)!=-1:
      nuevo += v[alfa.find(i)]
    else:
      nuevo+=i
print(nuevo)












