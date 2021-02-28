

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


def esca():
    C = "ingrese su numero="
    c = vint_num(C)
    if 0 < c < 9:
          for i in range(1, c + 1):
            print(" " * (c - i) + "#" * i)
    else:
       print("fuera de rango ,ingrese de nuevo")
       print()
       esca()

esca()

