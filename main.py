	# Librerias a utilizar

import hashlib
import math
import os
from time import time
import matplotlib.pyplot as plt
import numpy as np

	# Variables Globales:

# Nos indica la clave con la cual se debe comenzar a desincriptar.
clave = 0

# Indica el largo que contiene la palabra ingresada para incriptar, esto nos permite, rellenar con los bits faltante 
# si es que no calza con un multiplo de la cantidad de bits por bloques que ingresen.
largo = 0

# Guarda el texto inscriptado
palabraIncriptada = ''

# Guarda el texto desincriptado
palabraDesincriptado = ''

# Tiempo de ejecución
tiempo = 0
arreglo = []

	# Funciones auxiliares:

# Entrada:
# Procedimiento:
# Salida: 

def llenarBits(caracter,numLlenado):

	while len(caracter) != numLlenado:
		caracter = '0' + caracter
	return caracter

# Entrada:
# Procedimiento:
# Salida: 

def llenarBitsDerecha(caracter,numLlenado):

	while len(caracter) != numLlenado:
		caracter = caracter + '0' 
	return caracter

# Entrada:
# Procedimiento:
# Salida: 

def binario(palabra):

	texto = ""
	for caracter in palabra:
		aux = format(ord(caracter),'b')
		aux = llenarBits(aux,8)
		texto = texto + aux
	return texto

# Entrada:
# Procedimiento:
# Salida: 

def funcionXor (aux1, aux2):

	result = ''.join('0' if i == j else '1' for i, j in zip(aux1,aux2))
	return result

# Entrada:
# Procedimiento:
# Salida: 

def numToBin (numero,largo):

	binario = '{0:b}'.format(numero)
	binario = llenarBits(binario,largo)
	return binario

# Entrada:
# Procedimiento:
# Salida: 

def decodificar(bloques):

	texto = ''
	textoFinal = ''
	contador = 0

	for bloque in bloques:
		texto = texto + bloque
	while contador < len(texto):
		aux = chr(int(texto[contador:(contador+8)], 2))
		textoFinal = textoFinal + aux
		contador = contador + 8
	return textoFinal

# Entrada:
# Procedimiento:
# Salida: 

def separarPalabrasPorBloque(palabraBinario, cantXBloque):
	
	cantBloque = math.ceil(len(palabraBinario)/cantXBloque)
	bloques = []

	if (cantBloque < 1):
		cantBloque = 1
		palabraBinario = llenarBits(palabraBinario,cantXBloque)
	for aux in range(0,cantBloque):
		binAux = palabraBinario[(aux*cantXBloque):((aux*cantXBloque)+cantXBloque)]
		binAux = llenarBitsDerecha(binAux,cantXBloque)
		bloques.append(binAux)
	return bloques
	
	# Funcion F():

# Entrada:
# Procedimiento:
# Salida: 

def aplicarClave(bloqueDerecho,key):

	resul = (key * (len(bloqueDerecho)+key)) % len(bloqueDerecho)
	return resul

# Entrada:
# Procedimiento:
# Salida: 

def separador():

	os.system ("clear") 
	print("\n")
	print("Ahora se esta realizando la desincriptacion del texto ... .. . ")
	print("\n")


# Entrada:
# Procedimiento:
# Salida: 

def pedirParametro():

	os.system ("clear") 
	palabra = input("Ingrese texto a inscriptar: ")
	cantXBloque = int(input("Ingrese la cantidad de bits por bloque (Considerar que debe ser multiplo de 2): "))
	rondas = int(input("Ingrese la cantidad de rondas que desea realizar: "))
	key = int(input("Ingrese la clave con la que desea trabajar: "))

	return palabra,cantXBloque,rondas,key


	# Funcion de incriptación

# Entrada:
# Procedimiento:
# Salida: 

def incriptacion(bloques,keyNumero,cantXBloque,rondas):

	final = ''
	derechoFinal = ''
	izquierdoFinal = ''
	bloquesNuevos = []
	keyPrincipal = keyNumero
	for bloque in bloques:
		keyNumero = keyPrincipal
		for ronda in range(0,rondas):
			if (ronda != (rondas-1)):
				corte = int(len(bloque)/2)
				derecho = bloque[corte:]
				izquierdo = bloque[:corte]
				derechoAux = aplicarClave(derecho,keyNumero)
				keyNumero = keyNumero + (ronda+1)
				derechoAuxBin = numToBin(derechoAux,len(derecho))
				derechoAuxFinal = funcionXor(izquierdo,derechoAuxBin)
				izquierdoFinal = derecho
				derechoFinal = derechoAuxFinal
				final = izquierdoFinal + derechoFinal
				bloque = final
			else:
				corte = int(len(bloque)/2)
				derecho = bloque[corte:]
				izquierdo = bloque[:corte]
				derechoAux = aplicarClave(derecho,keyNumero)
				global clave 
				clave = keyNumero
				derechoAuxBin = numToBin(derechoAux,len(derecho))
				derechoAuxFinal = funcionXor(izquierdo,derechoAuxBin)
				izquierdoFinal = derechoAuxFinal
				derechoFinal = derecho
				final = izquierdoFinal + derechoFinal
				bloque = final
		bloquesNuevos.append(bloque)
	return bloquesNuevos

	# Funcion de desincriptación:

# Entrada:
# Procedimiento:
# Salida: 

def desincriptar(bloques,keyNumero,cantXBloque,rondas):

	final = ''
	derechoFinal = ''
	izquierdoFinal = ''
	bloquesNuevos = []
	keyPrincipal = keyNumero
	for bloque in bloques:
		keyNumero = keyPrincipal
		for ronda in range(0,rondas):
			if (ronda != (rondas-1)):
				corte = int(len(bloque)/2)
				derecho = bloque[corte:]
				izquierdo = bloque[:corte]
				derechoAux = aplicarClave(derecho,keyNumero)
				keyNumero = keyNumero - (rondas - (ronda+1))
				derechoAuxBin = numToBin(derechoAux,len(derecho))
				derechoAuxFinal = funcionXor(izquierdo,derechoAuxBin)
				izquierdoFinal = derecho
				derechoFinal = derechoAuxFinal
				final = izquierdoFinal + derechoFinal
				bloque = final
			else:
				corte = int(len(bloque)/2)
				derecho = bloque[corte:]
				izquierdo = bloque[:corte]
				derechoAux = aplicarClave(derecho,keyNumero)
				derechoAuxBin = numToBin(derechoAux,len(derecho))
				derechoAuxFinal = funcionXor(izquierdo,derechoAuxBin)
				izquierdoFinal = derechoAuxFinal
				derechoFinal = derecho
				final = izquierdoFinal + derechoFinal
				bloque = final
		bloquesNuevos.append(bloque)
	return bloquesNuevos

	# Función de Feistel:

# Entrada:
# Procedimiento:
# Salida: 

def feistel(cantXBloque,key,palabra,ronda,aux1):

	final = ''
	palabraBinario = binario(palabra)
	if (aux1 == 0):
		keyNumero = hash(key*10**-1)
	else:
		keyNumero = key
	bloques = separarPalabrasPorBloque(palabraBinario,cantXBloque)
	if (aux1 == 0):
		final = incriptacion(bloques,keyNumero,cantXBloque,ronda)
	else:
		final = desincriptar(bloques,keyNumero,cantXBloque,ronda)
	return decodificar(final)

	# Analisis

def analisisDeTiempo():

	palabra = 'abcde'
	tiemposI = []
	tiemposD = []
	tiempos1I = []
	tiempos1D = []
	tiempos2I = []
	tiempos2D = []

	# Variando Tamaño de palabra

	start_time = time()
	palabraIncriptada = feistel(8,357,(palabra*10),16,0)
	elapsed_time = time() - start_time
	tiemposI.append(elapsed_time)

	start_time = time()
	palabraDesincriptada = feistel(8,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiemposD.append(elapsed_time)

	#print("La palabra inscriptada es: " + palabraIncriptada + " La palabra desincriptada es: " + palabraDesincriptada + "\n")

	#

	start_time = time()
	palabraIncriptada = feistel(8,357,(palabra*25),16,0)
	elapsed_time = time() - start_time
	tiemposI.append(elapsed_time)

	start_time = time()
	palabraDesincriptada = feistel(8,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiemposD.append(elapsed_time)

	#print("La palabra inscriptada es: " + palabraIncriptada + " La palabra desincriptada es: " + palabraDesincriptada + "\n")

	#

	start_time = time()
	palabraIncriptada = feistel(8,357,(palabra*50),16,0)
	elapsed_time = time() - start_time
	tiemposI.append(elapsed_time)

	start_time = time()
	palabraDesincriptada = feistel(8,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiemposD.append(elapsed_time)

	#print("La palabra inscriptada es: " + palabraIncriptada + " La palabra desincriptada es: " + palabraDesincriptada + "\n")

	#

	start_time = time()
	palabraIncriptada = feistel(8,357,(palabra*75),16,0)
	elapsed_time = time() - start_time
	tiemposI.append(elapsed_time)

	start_time = time()
	palabraDesincriptada = feistel(8,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiemposD.append(elapsed_time)

	#print("La palabra inscriptada es: " + palabraIncriptada + " La palabra desincriptada es: " + palabraDesincriptada + "\n")

	#

	start_time = time()
	palabraIncriptada = feistel(8,357,(palabra*100),16,0)
	elapsed_time = time() - start_time
	tiemposI.append(elapsed_time)

	start_time = time()
	palabraDesincriptada = feistel(8,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiemposD.append(elapsed_time)

	#print("La palabra inscriptada es: " + palabraIncriptada + " La palabra desincriptada es: " + palabraDesincriptada + "\n")

	# Creación de grafico 
	plt.figure(1)
	plt.subplot(211)
	graficoTiempo(" Tiempo v/s Largo de la palabra (Inscriptación)",[10,25,50,75,100],tiemposI,"Largo Palabra", "Tiempo")
	plt.subplot(212)
	graficoTiempo(" Tiempo v/s Largo de la palabra (Desincriptación)",[10,25,50,75,100],tiemposD,"Largo Palabra", "Tiempo")
	plt.tight_layout()
	#plt.savefig(os.getcwd() + "/Salida/" + title + "_" + str(low_cutoff) + "_" + str(order) + ".png")
	plt.show()

	# Variando tamaño de bloque

	start_time = time()
	palabraIncriptada = feistel(4,357,(palabra*50),16,0)
	elapsed_time = time() - start_time
	tiempos1I.append(elapsed_time)

	start_time = time()
	palabraIncriptada = feistel(4,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiempos1D.append(elapsed_time)

	#

	start_time = time()
	palabraIncriptada = feistel(8,357,(palabra*50),16,0)
	elapsed_time = time() - start_time
	tiempos1I.append(elapsed_time)

	start_time = time()
	palabraIncriptada = feistel(8,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiempos1D.append(elapsed_time)

	#

	start_time = time()
	palabraIncriptada = feistel(16,357,(palabra*50),16,0)
	elapsed_time = time() - start_time
	tiempos1I.append(elapsed_time)
	
	start_time = time()
	palabraIncriptada = feistel(16,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiempos1D.append(elapsed_time)

	#

	start_time = time()
	palabraIncriptada = feistel(32,357,(palabra*50),16,0)
	elapsed_time = time() - start_time
	tiempos1I.append(elapsed_time)

	start_time = time()
	palabraIncriptada = feistel(32,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiempos1D.append(elapsed_time)

	#

	start_time = time()
	palabraIncriptada = feistel(64,357,(palabra*50),16,0)
	elapsed_time = time() - start_time
	tiempos1I.append(elapsed_time)

	start_time = time()
	palabraIncriptada = feistel(64,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiempos1D.append(elapsed_time)


	# Creación de grafico 
	plt.figure(2)
	plt.subplot(211)
	graficoTiempo(" Tiempo v/s Bits por Bloque - (Inscriptación)",[4,8,16,32,64],tiempos1I,"Bits por bloques","Tiempo")
	plt.subplot(212)
	graficoTiempo(" Tiempo v/s Bits por Bloque - (Desincriptación)",[4,8,16,32,64],tiempos1D,"Bits por bloques","Tiempo")
	plt.tight_layout()
	#plt.savefig(os.getcwd() + "/Salida/" + title + "_" + str(low_cutoff) + "_" + str(order) + ".png")
	plt.show()

	# Variando cantidad de rondas
	
	start_time = time()
	palabraIncriptada = feistel(8,357,(palabra*50),1,0)
	elapsed_time = time() - start_time
	tiempos2I.append(elapsed_time)

	start_time = time()
	palabraIncriptada = feistel(8,clave,palabraIncriptada,1,0)
	elapsed_time = time() - start_time
	tiempos2D.append(elapsed_time)

	#

	start_time = time()
	palabraIncriptada = feistel(8,357,(palabra*50),8,0)
	elapsed_time = time() - start_time
	tiempos2I.append(elapsed_time)

	start_time = time()
	palabraIncriptada = feistel(8,clave,palabraIncriptada,8,0)
	elapsed_time = time() - start_time
	tiempos2D.append(elapsed_time)

	#

	start_time = time()
	palabraIncriptada = feistel(8,357,(palabra*50),16,0)
	elapsed_time = time() - start_time
	tiempos2I.append(elapsed_time)

	start_time = time()
	palabraIncriptada = feistel(8,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiempos2D.append(elapsed_time)

	#

	start_time = time()
	palabraIncriptada = feistel(8,357,(palabra*50),32,0)
	elapsed_time = time() - start_time
	tiempos2I.append(elapsed_time)

	start_time = time()
	palabraIncriptada = feistel(8,clave,palabraIncriptada,32,0)
	elapsed_time = time() - start_time
	tiempos2D.append(elapsed_time)

	#

	start_time = time()
	palabraIncriptada = feistel(8,357,(palabra*50),64,0)
	elapsed_time = time() - start_time
	tiempos2I.append(elapsed_time)

	start_time = time()
	palabraIncriptada = feistel(8,clave,palabraIncriptada,64,0)
	elapsed_time = time() - start_time
	tiempos2D.append(elapsed_time)

	# Creación de grafico 
	plt.figure(3)
	plt.subplot(211)
	graficoTiempo(" Tiempo v/s Cantidad de rondas",[1,8,16,32,64],tiempos2I,"Cantidad de rondas","Tiempo")
	plt.subplot(212)
	graficoTiempo(" Tiempo v/s Cantidad de rondas",[1,8,16,32,64],tiempos2D,"Cantidad de rondas","Tiempo")
	plt.tight_layout()
	#plt.savefig(os.getcwd() + "/Salida/" + title + "_" + str(low_cutoff) + "_" + str(order) + ".png")
	plt.show()

	return 

def graficoTiempo(titulo,x,y,xlabel,ylabel):

    plt.title(titulo, fontsize = 12, color = 'blue')
    plt.xlabel(xlabel, color = 'red')
    plt.ylabel(ylabel, color = 'orange')
    plt.plot(x,y,'o-')
    plt.xticks(x)
    plt.yticks(y)
    #plt.show()
    #plt.savefig( os.getcwd() + "/Salida/" + title + "_" + str(low_cutoff) + "_" + str(order) + ".png")

	# Menu: 

# Entrada:
# Procedimiento:
# Salida: 

def menu():

	opcion = 0

	while opcion != '4':

		print("\n")
		print("	1. Realizar inscriptación")
		print("	2. Realizar analisis")
		print("	3. Inscribir archivo con resultado")
		print("	4. Salir")
		print("\n")

		opcion = input(" Ingrese la opcion a realizar: ")

		if (opcion == '1'):
			
			palabra,cantXBloque,rondas,key = pedirParametro()

			global palabraIncriptada

			start_time = time()
			palabraIncriptada = feistel(cantXBloque,key,palabra,rondas,0)
			elapsed_time = time() - start_time
			print("Tiempo de ejecucion de inscriptacion es: %0.10f" %elapsed_time)

			palabraIncriptadaOut = palabraIncriptada.replace(' ','')
			print("La palabra inscriptada es: " + palabraIncriptadaOut + "\n")
			
			input("Presione una tecla para realizar la desincriptación ... .. . \n")
			separador()

			global palabraDesincriptado

			start_time = time()
			palabraDesincriptado = feistel(cantXBloque,clave,palabraIncriptada,rondas,1)
			elapsed_time = time() - start_time
			print("Tiempo de ejecucion de desincriptación es: %0.10f" %elapsed_time)

			print("La palabra desincriptada es: " + palabraDesincriptado)

			input("Presione una tecla para continuar ... .. . \n")
			os.system ("clear")

		if (opcion == '2'):

			os.system ("clear")

			analisisDeTiempo()
			#analisisDeAvalancha()

			input("Presione una tecla para continuar ... .. . \n")
		
		if(opcion == '3'):

			os.system ("clear")
			print(" Exportando los resultados a un archivo plano. ")
			nombre = input("Ingrese el nombre del archivo: ")


		if(opcion == '4'):

			os.system ("clear")
			print("\n")
			print("Gracias por preferirnos")
			print("\n")

# Haciendo el llamado a la ejecución del programa.
menu()