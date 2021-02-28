import string

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



palabra=input("ingrese su texto a cifrar=  ")
K="ingrese cuanto va a rotar="
k=vint_num(K)
alfa=string.ascii_lowercase

nuevo=""
for i in palabra:
    if i.lower() in alfa:
       p=alfa.find(i.lower())
       c = (p+k) % 26

       if i.isupper():
           nuevo+=nuevo.join(alfa[c].upper())
       else:
           nuevo+= nuevo.join(alfa[c])
    else:
        nuevo += nuevo.join(alfa[i])
print(f"texto cifrado es: {nuevo}")








