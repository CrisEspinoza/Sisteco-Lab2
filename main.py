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

def validarParametros(palabra,cantXBloque,rondas,key):

	if (palabra.isalpha()):
		if(str(cantXBloque).isdigit()):
			if(str(rondas).isdigit()):
				if(str(key).isdigit()):
					return True
				else:
					return False
			else:
				return False
		else: 
			return False
	else:
		return False

# Entrada:
# Procedimiento:
# Salida: 

def pedirParametro():

	os.system ("clear") 
	opcion = True
	while opcion:

		palabra = input("Ingrese texto a inscriptar: ")
		cantXBloque = input("Ingrese la cantidad de bits por bloque (Considerar que debe ser multiplo de 2): ")
		rondas = input("Ingrese la cantidad de rondas que desea realizar: ")
		key = input("Ingrese la clave con la que desea trabajar (Debe ser numerica): ")

		if (validarParametros(palabra,cantXBloque,rondas,key)):
			opcion = False
			print("Parametros validos ... .. . \n ")
		else:
			print("Parametros no validos, reingresar parametros ... .. . \n ")

	return palabra,int(cantXBloque),int(rondas),int(key)

# Entrada:
# Procedimiento:
# Salida: 
	
def limitarDecimal(x):

	contador = 0
	for num in x:
		x[contador] = round(num,5)
		contador = contador + 1
	return x

# Entrada:
# Procedimiento:
# Salida: 

def escribirSalida(palabra, palabraIncriptada,palabraDesincriptado,time1,time2):

	nombre = input("\n Ingrese el nombre del archivo a escribir (Sin extensión): ")

	archivo = open("./Salida/" + nombre + ".txt" ,'a')

	archivo.write("*********************************************\n")
	archivo.write("\n")
	archivo.write("La palabra a inscriptar es: " + palabra + "\n")
	archivo.write("\n")
	archivo.write("La palabra inscriptada es: " + palabraIncriptada + "\n")
	archivo.write("\n")
	archivo.write("La palabra al desincriptar es: " + palabraDesincriptado +" \n")
	archivo.write("\n")
	archivo.write("*********************************************\n")

	print("\n Archivo creado con exito \n ")

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

	# Variando tamaño de bloque (Performas)

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
	plt.figure(figsize=(8.0, 5.0))
	plt.subplot(211)
	p1 = plt.plot(linewidth = 2)
	graficoTiempo(" Tiempo v/s Bits por Bloque - (Inscriptación)",[4,8,16,32,64],tiempos1I,"Bits por bloques","Tiempo")
	plt.subplot(212)
	p2 = plt.plot(linewidth = 2)
	graficoTiempo(" Tiempo v/s Bits por Bloque - (Desincriptación)",[4,8,16,32,64],tiempos1D,"Bits por bloques","Tiempo")
	plt.tight_layout()
	plt.savefig(os.getcwd() + "/Salida/Tiempo_vs_Bits_por_Bloque.png")
	plt.show()

	# Variando cantidad de rondas (Difusión / Confusión)
	
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
	plt.figure(2)
	plt.subplot(211)
	graficoTiempo(" Tiempo v/s Cantidad de rondas",[1,8,16,32,64],tiempos2I,"Cantidad de rondas","Tiempo")
	plt.subplot(212)
	graficoTiempo(" Tiempo v/s Cantidad de rondas",[1,8,16,32,64],tiempos2D,"Cantidad de rondas","Tiempo")
	plt.tight_layout()
	plt.savefig(os.getcwd() + "/Salida/Tiempo_vs_Cantidad_de_rondas.png")
	plt.show()

def graficoTiempo(titulo,x,y,xlabel,ylabel):

	y = limitarDecimal(y)
	plt.title(titulo, fontsize = 12, color = 'blue')
	plt.xlabel(xlabel, color = 'red')
	plt.ylabel(ylabel, color = 'orange')
	plt.plot(x,y,'o-')
	plt.xticks(x,rotation=20)
	plt.yticks(y,rotation=20)

def analisisDeAvalancha():

	palabra = 'abcde'
	tiemposI = []
	tiemposD = []
	tiempos1I = []
	tiempos1D = []

	# Variando Tamaño de palabra (Avalancha)

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
	plt.figure(3)
	plt.subplot(211)
	graficoTiempo(" Tiempo v/s Largo de la palabra (Inscriptación)",[10,25,50,75,100],tiemposI,"Largo Palabra", "Tiempo")
	plt.subplot(212)
	graficoTiempo(" Tiempo v/s Largo de la palabra (Desincriptación)",[10,25,50,75,100],tiemposD,"Largo Palabra", "Tiempo")
	plt.tight_layout()
	plt.savefig(os.getcwd() + "/Salida/Tiempo_vs_Largo_palabra.png")
	plt.show()

	# Variando Tamaño de clave (Avalancha)

	start_time = time()
	palabraIncriptada = feistel(8,357,(palabra*50),16,0)
	elapsed_time = time() - start_time
	tiempos1I.append(elapsed_time)

	start_time = time()
	palabraDesincriptada = feistel(8,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiempos1D.append(elapsed_time)

	#print("La palabra inscriptada es: " + palabraIncriptada + " La palabra desincriptada es: " + palabraDesincriptada + "\n")

	#

	start_time = time()
	palabraIncriptada = feistel(8,35744,(palabra*50),16,0)
	elapsed_time = time() - start_time
	tiempos1I.append(elapsed_time)

	start_time = time()
	palabraDesincriptada = feistel(8,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiempos1D.append(elapsed_time)

	#print("La palabra inscriptada es: " + palabraIncriptada + " La palabra desincriptada es: " + palabraDesincriptada + "\n")

	#

	start_time = time()
	palabraIncriptada = feistel(8,3574444,(palabra*50),16,0)
	elapsed_time = time() - start_time
	tiempos1I.append(elapsed_time)

	start_time = time()
	palabraDesincriptada = feistel(8,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiempos1D.append(elapsed_time)

	#print("La palabra inscriptada es: " + palabraIncriptada + " La palabra desincriptada es: " + palabraDesincriptada + "\n")

	#

	start_time = time()
	palabraIncriptada = feistel(8,357444444,(palabra*50),16,0)
	elapsed_time = time() - start_time
	tiempos1I.append(elapsed_time)

	start_time = time()
	palabraDesincriptada = feistel(8,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiempos1D.append(elapsed_time)

	#print("La palabra inscriptada es: " + palabraIncriptada + " La palabra desincriptada es: " + palabraDesincriptada + "\n")

	#

	start_time = time()
	palabraIncriptada = feistel(8,35744444444,(palabra*50),16,0)
	elapsed_time = time() - start_time
	tiempos1I.append(elapsed_time)

	start_time = time()
	palabraDesincriptada = feistel(8,clave,palabraIncriptada,16,0)
	elapsed_time = time() - start_time
	tiempos1D.append(elapsed_time)

	#print("La palabra inscriptada es: " + palabraIncriptada + " La palabra desincriptada es: " + palabraDesincriptada + "\n")

	# Creación de grafico 
	plt.figure(4)
	plt.subplot(211)
	graficoTiempo(" Tiempo v/s Largo de la clave (Inscriptación)",[3,5,7,9,11],tiemposI,"Largo clave", "Tiempo")
	plt.subplot(212)
	graficoTiempo(" Tiempo v/s Largo de la clave (Desincriptación)",[3,5,7,9,11],tiemposD,"Largo clave", "Tiempo")
	plt.tight_layout()
	plt.savefig(os.getcwd() + "/Salida/Tiempo_vs_Largo_clave.png")
	plt.show()

	return 

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

			start_time1 = time()
			palabraIncriptada = feistel(cantXBloque,key,palabra,rondas,0)
			elapsed_time1 = time() - start_time1
			print("Tiempo de ejecucion de inscriptacion es: %0.10f" %elapsed_time1)

			palabraIncriptadaOut = palabraIncriptada.replace(' ','')
			print("La palabra inscriptada es: " + palabraIncriptadaOut + "\n")
			
			input("Presione una tecla para realizar la desincriptación ... .. . \n")
			separador()

			global palabraDesincriptado

			start_time2 = time()
			palabraDesincriptado = feistel(cantXBloque,clave,palabraIncriptada,rondas,1)
			elapsed_time2 = time() - start_time2
			print("Tiempo de ejecucion de desincriptación es: %0.10f" %elapsed_time2)

			print("La palabra desincriptada es: " + palabraDesincriptado + "\n")

			input("Presione una tecla para continuar ... .. . \n")

			os.system ("clear")

			archivo = input("\n Desea escribir un archivo con le resultado (Si = 1 | No = 0): ")

			if (archivo == '1'):
				escribirSalida(palabra,palabraIncriptada,palabraDesincriptado,elapsed_time1,elapsed_time2)

			input("Presione una tecla para continuar ... .. .")
			os.system ("clear")

		if (opcion == '2'):

			os.system ("clear")

			analisisDeTiempo()
			analisisDeAvalancha()

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