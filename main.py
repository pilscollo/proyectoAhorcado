import random
# i juego ahorcado
#cosas que necesito: 1. que el programa elija una de las palabras para jugar
#2. programa que me haga tanta lineas como letras

def selectorPalabra(listaPalabra,cantidadPalabras):
      num= random.randint(0,cantidadPalabras-1)
      return  listaPalabra[num]

def encontrarLetra(palabra, letra):
    pos=-1
    i=0
    while i<len(palabra):
        if palabra[i]==letra:
            pos=i
            i= len(palabra)
        else:
            i= i+1
    return pos

def eliminarLetra(palabra,pos):
    palabra[pos]= "_"
    return palabra

def palabraIncognito(cantLetras):
    palabra=[]
    i=0
    while i<cantLetras:
        palabra.append("_")
        i = i + 1

    return palabra

def descubrirPalabra(palabraIncognito, letra,pos):
    palabraIncognito[pos]= letra
    return palabraIncognito
def imprimirLista(lista):
     for i in range(len(lista)):
         print(lista[i], end = ' ')

def resolucion(palabra):
    flag= encontrarLetra(palabra,'_')
    retorno= False
    if flag==-1:
        retorno= True
    return  retorno


def funcionGeneral(listaPalabra, listaLetras):
    cantPalabras= len(listaPalabra)
    aux= selectorPalabra(listaPalabra,cantPalabras)
    palabra= list(aux)
    r= False
    vida= 5
    listaInc= palabraIncognito(len(palabra))
    while vida>0 and  r == False:
        print("\nVida: " + str(vida))
        imprimirLista(listaInc)
        letra= input("\nSELECCIONE UNA LETRA: ")
        flag= encontrarLetra(listaLetras,letra)
        if flag != -1:
            listaLetras= eliminarLetra(listaLetras,flag)
            pos= encontrarLetra(palabra,letra)
            if pos==-1:
                vida= vida-1
                print("\n PERDIO UNA VIDA  LE QUEDAN: " + str(vida))
            else:
                while pos!=-1:
                    listaInc = descubrirPalabra(listaInc, letra,pos)
                    palabra= eliminarLetra(palabra, pos)
                    pos= encontrarLetra(palabra, letra)
        else:
            print("\nEsta letra ya fue seleccionada ")
        r = resolucion(listaInc)

    return r


#def agregarPosicionAlista(palabraIncognito,letra,palabra,pos)
#def lineas(listaPosicionesDescubiertas,palabra,cantidadLetras):
  ##  for i in cantidadLetras:

listaLetras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lista = ["zapato","libro","perro","argentina"]

rta= funcionGeneral(lista, listaLetras)
if  rta== True:
    print("\n FELICIDADES GANASTE :)")
else:
    print("\n PERDISTE : (")

