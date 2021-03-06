import random
from tkinter import Tk
import tkinter.filedialog
from time import gmtime, strftime

valoresADN = ['A', 'C', 'T', 'G']
valoresARN = ['A', 'C', 'U', 'G']

aminoacidosLargo = ['ÁcidoAspártico', "ÁcidoGlutámico", "Arginina", "Lisina", "Asparagina", "Histidina", "Glutamina", "Serina", "Treonina", "Alanina", "Glicina", "Valina", "Prolina", "Leucina", "Fenilalalina", "Tirosina", "Isoleucina", "Metionina", "Triptofano", "Cisteína", "STOP"]
aminoacidosMediano = ["Asp", "Glu", "Arg", "Lys", "Asn", "His", "Gln", "Ser", "Thr", "Ala", "Gly", "Val", "Pro", "Leu", "Phe", "Tyr", "Ile", "Met", "Trp", "Cys", "Stop"]
aminoacidosPequeno = ["D", "E", "R", "K", "N", "H", "Q", "S", "T", "A", "G", "V", "P", "L", "F", "Y", "I", "M", "W", "C", "Stop"]

aminoacidos = [["GAC","GAU"],["GAA", "GAG"], ["CGA", "CGC", "CGG", "CGU", "AGA", "AGG"], ["AAA", "AAG"], ["AAC", "AAU"], ["CAC", "CAU"], ["CAA", "CAG"], ["UCA", "UCC", "UCG", "UCU", "AGC", "AGU"], ["ACA", "ACC", "ACG", "ACU"], ["GCA", "GCC", "GCG", "GCU"], ["GGA", "GGC", "GGG", "GGU"], ["GUA", "GUC", "GUG", "GUU"], ["CCA", "CCC", "CCG", "CCU"], ["CUA", "CUC", "CUG", "CUU", "UUA", "UUG"], ["UUC", "UUU"], ["UAC", "UAU"], ["AUA", "AUC", "AUU"], ["AUG"], ["UGG"], ["UGC", "UGU"], ["UAA", "UAG", "UGA"]]

def main():
    contArchivos = 0
    while True:
        print("MENÚ")
        print("============================================")
        print("1. Generador aleatorio de secuencias de ADN")
        print("2. Generador aleatorio de secuencias de ARN")
        print("3. Traductor de ADN a ARN")
        print("4. Traductor de ARN a ADN")
        print("5. Traductor de ADN a aminoácidos")
        print("6. Traductor de aminoácidos a ADN")
        print("7. Salir")
        print("============================================")
        opcion = input("Seleccione una opción: ")

        if(opcion == "1"):
            print("")
            longitud = int(input("Especifique la longitud de la secuencia: "))
            secuencia = generador(longitud, valoresADN)

            nombreArchivo = "Secuencia" + str(contArchivos) + ".txt"
            contArchivos += 1

            nombreArchivo = strftime("%Y-%m-%d %H-%M-%S", gmtime()) + ".txt"
            
            archivo = open(nombreArchivo,"w")
            archivo.write(secuencia)
            archivo.close()

            print("Secuencia guardada en el archivo " + nombreArchivo)
            print("")
            
        if(opcion == "2"):
            print("")
            longitud = int(input("Especifique la longitud de la secuencia: "))
            secuencia = generador(longitud, valoresADN)

            nombreArchivo = "Secuencia" + str(contArchivos) + ".txt"
            contArchivos += 1

            nombreArchivo = strftime("%Y-%m-%d %H-%M-%S", gmtime()) + ".txt"
            
            archivo = open(nombreArchivo,"w")
            archivo.write(secuencia)
            archivo.close()

            print("Secuencia guardada en el archivo " + nombreArchivo)
            print("")

        if(opcion == "3"):
            Tk().withdraw()
            archivoLectura = tkinter.filedialog.askopenfilename()

            with open(archivoLectura, 'r') as archivo:
                secuencia = archivo.read().replace('\n', '')

            secuenciaNueva = ADNaARN(secuencia)
            print("")
            print("La nueva secuencia es: " + secuenciaNueva)
            nombreArchivo = "Secuencia" + str(contArchivos) + ".txt"
            contArchivos += 1

            nombreArchivo = strftime("%Y-%m-%d %H-%M-%S", gmtime()) + ".txt"
            
            archivo = open(nombreArchivo,"w")
            archivo.write(secuenciaNueva)
            archivo.close()

            print("Secuencia guardada en el archivo " + nombreArchivo)
            print("")

        if(opcion == "4"):
            Tk().withdraw()
            archivoLectura = tkinter.filedialog.askopenfilename()

            with open(archivoLectura, 'r') as archivo:
                secuencia = archivo.read().replace('\n', '')

            secuenciaNueva = ARNaADN(secuencia)
            print("")
            print("La nueva secuencia es: " + secuenciaNueva)
            nombreArchivo = "Secuencia" + str(contArchivos) + ".txt"
            contArchivos += 1

            nombreArchivo = strftime("%Y-%m-%d %H-%M-%S", gmtime()) + ".txt"
            
            archivo = open(nombreArchivo,"w")
            archivo.write(secuenciaNueva)
            archivo.close()

            print("Secuencia guardada en el archivo " + nombreArchivo)
            print("")

        if(opcion == "5"):
            print("")
            print("Formato de nombre de aminoácidos: ")
            print("1 - Nombre completo")
            print("2 - Abreviatura de 3 letras")
            print("3 - Abreviatura de 1 letra")

            opcionNombre = int(input("Seleccione la opción deseada: "))
            
            Tk().withdraw()
            archivoLectura = tkinter.filedialog.askopenfilename()

            with open(archivoLectura, 'r') as archivo:
                secuencia = archivo.read().replace('\n', '')

            print("La secuencia original es: " + secuencia)
            secuenciaNueva = AdnAAminoacidos(ADNaARN(secuencia), opcionNombre)
            print("La nueva secuencia es: " + secuenciaNueva)
            nombreArchivo = "Secuencia" + str(contArchivos) + ".txt"
            contArchivos += 1

            nombreArchivo = strftime("%Y-%m-%d %H-%M-%S", gmtime()) + ".txt"
            
            archivo = open(nombreArchivo,"w")
            archivo.write(secuenciaNueva)
            archivo.close()

            print("Secuencia guardada en el archivo " + nombreArchivo)
            print("")

        if(opcion == "6"):
            print("")
            print("Formato de nombre de aminoácidos: ")
            print("1 - Nombre completo")
            print("2 - Abreviatura de 3 letras")
            print("3 - Abreviatura de 1 letra")

            opcionNombre = int(input("Seleccione la opción deseada: "))
            
            Tk().withdraw()
            archivoLectura = tkinter.filedialog.askopenfilename()

            with open(archivoLectura, 'r') as archivo:
                secuencia = archivo.read().replace('\n', '')

            print("La secuencia original es: " + secuencia)
            secuenciaNueva = aminoacidosAAdn(secuencia, opcionNombre)
            print(len(secuenciaNueva[0]))
            
            nombreArchivo = "Secuencia" + str(contArchivos) + ".txt"
            contArchivos += 1

            nombreArchivo = strftime("%Y-%m-%d %H-%M-%S", gmtime()) + ".txt"

            archivo = open(nombreArchivo,"w")
            for item in secuenciaNueva[0]:
                archivo.write("%s\n" % ARNaADN(item))
            
            archivo.close()

            print("Secuencia guardada en el archivo " + nombreArchivo)
            print("")

        if(opcion == "7"):
            break

        else:
            print("Opcion inválida. Intente de nuevo. ")
            print("")
            
        
def generador(longitud, valores):
    i = 0
    secuencia = ""
    while(i < longitud):
        secuencia += valores[random.randint(0,3)]
        i += 1
    return secuencia

def verificadorADN(cadena):
    for valor in cadena:
        if valor not in valoresADN:
            return False
    return True

def verificadorARN(cadena):
    for valor in cadena:
        if valor not in valoresARN:
            return False
    return True

def ARNaADN(cadena):
    result = ""
    if(verificadorARN(cadena)):
        for valor in cadena:
            if(valor == "U"):
                result += "T"
            else:
                result += valor
    return result

def ADNaARN(cadena):
    result = ""
    if(verificadorADN(cadena)):
        for valor in cadena:
            if(valor == "T"):
                result += "U"
            else:
                result += valor
    return result

def complementoADN(cadena):
    result = ""
    if(verificadorADN(cadena)):
        for valor in cadena:
            if(valor == "A"):
                result += "T"
            elif(valor == "T"):
                result += "A"
            elif(valor == "C"):
                result += "G"
            else:
                result += "C"
    return result

def complementoARN(cadena):
    result = ""
    if(verificadorARN(cadena)):
        for valor in cadena:
            if(valor == "A"):
                result += "U"
            elif(valor == "U"):
                result += "A"
            elif(valor == "C"):
                result += "G"
            else:
                result += "C"
    return result

def palindromo(cadena):
    return (cadena == cadena[::-1])

def prefijo(cadena, secuencia):
    return (cadena[0:len(secuencia)] == secuencia)

def sufijo(cadena, secuencia):
    return (cadena[len(cadena)-len(secuencia):] == secuencia)


def largoHilera(hilera):
    return len(hilera)

def elementoIesimo(hilera,indice):
    if (indice< len(hilera) and indice>=0):
        return hilera[indice]

def subsecuencia(pSuperSecuencia,pSubSecuencia):
        if (pSubSecuencia == ""):
            return True
        largoSub = len(pSubSecuencia)
        largoSuper = len(pSuperSecuencia)
        if (largoSuper >= largoSub ):
            contWhile = 0
            while (contWhile < largoSub):
                if (pSuperSecuencia.count(pSubSecuencia[contWhile]) !=
                pSubSecuencia.count(pSubSecuencia[contWhile])) :
                    return False
                else:
                    contWhile+=1
            return True
        else:
            print ("Error")
            
def superSecuencia (pSuperSecuencia,pSubSecuencia):
    return subsecuencia(pSuperSecuencia,pSubSecuencia)

def subString (pSuperString, pSubString):
    if (pSubString in pSuperString):
        return True
    else:
        return False

def superString(pSuperString, pSubString):
    return subString (pSuperString, pSubString)

def intervalo (hilera, inicio, fin):
    result = hilera [inicio: fin]
    return result

def concatenacion (hilera1, hilera2):
    result = hilera1+hilera2
    return result

def prefijo(hilera, indice):
    result = hilera[0:indice]
    return result

def sufijo (hilera, indice):
    result = hilera[len(hilera) -indice:]
    return result

##def aminoacidosAAdn(hilera, opcion):
##    lista = []
##
##    if(opcion==1):
##        amino = aminoacidosLargo
##    elif(opcion==2):
##        amino = aminoacidosMediano
##    else:
##        amino = aminoacidosPequeno
##    
##    while(hilera != ""):
##        busqueda = hilera[:3]
##        hilera = hilera[3:]
##        preRes = aminoacidos[amino.index(busqueda)]
##        lista.append(preRes)
##    resultado = mezclar(lista)
##    return resultado        

def aminoacidosAAdn(hilera, opcion):
    lista = []
    tripletas = hilera.split(" ")

    if(opcion==1):
        amino = aminoacidosLargo
    elif(opcion==2):
        amino = aminoacidosMediano
    else:
        amino = aminoacidosPequeno
    
    while(len(tripletas) != 1):
        print(tripletas[0])
        busqueda = tripletas[0]
        tripletas = tripletas[1:]
        preRes = aminoacidos[amino.index(busqueda)]
        lista.append(preRes)
    resultado = mezclar(lista)
    return resultado 
   
def mezclar(lista):
    while (len(lista) !=1):
        primer = lista[0]
        segundo = lista[1]
        resul = []
        cont1 = 0
        while (cont1 != len(primer)):
            cont2 = 0
            while (cont2 != len(segundo)):
                resul.append(primer[cont1]+segundo[cont2])
                #resul += primer[cont1]+segundo[cont2]
                cont2+=1
            cont1+=1
        lista = [resul] + lista[2:]
    return lista
                
def AdnAAminoacidos (hilera, opcion):
    resultado = ""
    
    if(opcion==1):
        amino = aminoacidosLargo
    elif(opcion==2):
        amino = aminoacidosMediano
    else:
        amino = aminoacidosPequeno

    while (hilera!= ""):
        cont=0
        codon = hilera[:3]
        for i in aminoacidos:            
            if (codon in aminoacidos[cont]):
                resultado += amino[cont] + " "
                break
            else:
                cont+=1
        hilera = hilera[3:]
    return resultado
            
    
