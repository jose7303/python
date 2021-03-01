
def vdig():
 while True:

     a =["0","1","2","3","4","5","6","7","8","9"]
     n =input("ingrese su número de tarjeta= ")
     verificacion = True

     for i in n:
         if i not in a:
             print("Ingresa solo números")
             verificacion = False
             break
     if verificacion == True:
         return n



num=vdig()

l=[]
for i in list(num):
    l.append(i)

#ln=sublista de cada 2 digitos que empieza en el penultimo
ln=[]
for i in range(len(l)-2,-1,-2):
       ln.append(int(l[i]))

#lv=sublista de digitos que no estan en la anterior sublista
lv=[]
for i in range(len(l)-1,-1,-2):
       lv.append(int(l[i]))



g = [i for i in range(len(l))]
nu = {}
for i in g:
    for j in l:
        nu[i] = j
        l.remove(j)
        break


if len(num)==15:
    print("AMEX")
elif len(num)==16:
    if nu[0]=="4":
        print("Visa")
    else:
        print("MasterCard")
elif len(num)==13:
        print("Visa")
else:
    print("invalido")


#producto de cada digito de ln por 2
nuevo=[]
for i in ln:
    nuevo.append(i*2)
cadena=""
for i in nuevo:
    cadena+=str(i)


"""
lista=suma de todos los digitos de 'ln' 
"""
lista=[]
for i in cadena:
    lista.append(int(i))
final=[sum(lista)+sum(lv)]


"""
verificación del ultimo digito de final 

"""
cad=""
for i in final:
    cad+=str(i)

if cad[-1]=="0":
    print("Es legitima")
else:
    print("No es ligitima")









