
import math

#problema 1
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

C="tu a monto a ingresar: "
c=vfloat_num(C)

T="tiempo: "
t=vfloat_num(T)


I="tasa de interes: "
i=vfloat_num(I)

j=i/100

if t==int(t):
    for i in range(1, int(t) + 1):
        A = c * j * i
        cf = c + A
        print(f"ahorro en el {i} año.- {cf: .2f}")
elif t!=int(t):
    for i in [*range(1, int(t) + 1), t]:
        A = c * j * i
        cf = c + A
        print(f"ahorro en el {i} año.- {cf: .2f}")




#problema 2
print("Ecuación cuadrática")
print("'ax²+bx+c'")

A="ingrese a="
a=vfloat_num(A)
B="ingrese b="
b=vfloat_num(B)
C="ingrese c="
c=vfloat_num(C)

d=(b**2)-(4*a*c)
print()
if d<0:
    print("No hay soluciones reales")
elif d==0:
    x = -(b) + (math.sqrt(d)) / 2 * a
    print(f"Hay dos soluciones repetidas\n x={x}")
elif d>0:
    x = (-(b) + (math.sqrt(d)) )/ (2*a)
    x2 =(-(b) - (math.sqrt(d)) )/ (2*a)
    print(f"Hay dos soluciones diferentes\n x1={x}\n x2={x2}")





