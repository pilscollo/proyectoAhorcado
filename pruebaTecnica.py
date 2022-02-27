# dar vuelta una secuencia de caracteres sin usar metodos propios

aux =  "WORK1"

#pasos:
#1. pasar de string a lista (para facilitar los)

lista = list(aux)
print (lista)
#2. contar los elementos de mi lista

cant = len(lista)

#3. hacer un bucle for que recorra mi lista y  ponga los elementos de una lista en una auxiliar


#3 bis. hacer un bucle que recorra mi lista y haga los intercambios con un aux

a = "x"
b= "y"
j= cant-1
i=0

while i!=j:

    a= lista[i]
    b=lista[j]

    lista[i]= b
    lista[j]= a
    i=i+1
    j=j-1


print(lista)

