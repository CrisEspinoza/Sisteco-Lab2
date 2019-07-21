	# Librerias a utilizar 

import hashlib
from hashlib import blake2b
from funcionesAuxiliares import *
from time import time
from funciones import *

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

	# Orquestador

# Entrada: Entran la palabras, cantidad de bloques, rondas y clave.
# Procedimiento: Se realiza la incriptacion y desincriptacion del mensaje.
# Salida: Entrega el tiempo que se demora y la verificacion que el mensaje que recibe el receptor es el mismo.

def orquestador(palabra,cantXBloque,rondas,key):

	global palabraIncriptada

	inicio_tiempo_1 = time()
	palabraIncriptada = feistel(cantXBloque,key,palabra,rondas,0,-1)
	print(palabraIncriptada)
	fin_tiempo_1 = time() - inicio_tiempo_1
	print("Tiempo de ejecucion de incriptación es: %0.10f" %fin_tiempo_1)

	palabraIncriptadaOut = palabraIncriptada.replace(' ','')

	global palabraDesincriptado
	global clave

	inicio_tiempo_2 = time()
	palabraDesincriptado = feistel(cantXBloque,clave,palabraIncriptada,rondas,1,-1)
	fin_tiempo_2 = time() - inicio_tiempo_2
	print("Tiempo de ejecucion de desincriptación es: %0.10f" %fin_tiempo_2)

	print("Thou 1: " + str(fin_tiempo_1/rondas))
	print("Thou 2: " + str(fin_tiempo_2/rondas))

	print("La palabra desincriptada es: " + palabraDesincriptado + "\n")

	archivo = input("\n Desea escribir un archivo con le resultado (Si = 1 | No = 0): ")

	if (archivo == '1'):
		escribirSalida(palabra,palabraIncriptada,palabraDesincriptado,fin_tiempo_1,fin_tiempo_2)

	input("Presione una tecla para realizar el analisis del programa ... .. .")

	# Analisis de cantidad por bloque.

	analisisDeCantidadPorBloque(key)

	# Analisis de cantidad de rondas

	analisisDeCantidadDeRondasPar(key)
	analisisDeCantidadDeRondasImpar(key)

	# Analisis de largo de palabra

	analisisDeLargoDePalabra(key)

	# Analisis de largo de clave

	analisisDeLargoDeClave(key)

	# Analisis Avalancha

	analisisAvalancha(key,8,1)

	return 
	
	# Funcion de incriptación

# Entrada: Parametros necesarios para poder realizar la incriptación.
# Procedimiento: Se realiza la incriptacion del mensaje (Informe explicado el procedimiento)
# Salida: Entrega el mensaje incriptado 

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
				keyNumero = keyNumero + (ronda+len(str(keyNumero)))
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

# Entrada: Parametros necesarios para poder realizar la desincriptar.
# Procedimiento: Se realiza la desincriptar del mensaje (Informe explicado el procedimiento)
# Salida: Entrega el mensaje desincriptar 

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
				keyNumero = keyNumero - (rondas - (ronda+len(str(keyNumero))))
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

# Entrada: Entra la cantidad de parametros necesarios par relaizar el proceso.
# Procedimiento: Se realiza la criptacion o desincriptacion del mensaje, segun sea solicitado,
# Salida: Entrega el mensaje obtenido

def feistel(cantXBloque,key,palabra,ronda,aux1,aux2):

	final = ''
	palabraBinario = binario(palabra)
	if (aux1 == 0):
		aux = bytes(key, encoding= 'utf-8')
		keyNumero = int(blake2b(key=aux,digest_size=7).hexdigest(),16)
	else:
		keyNumero = key
	bloques = separarPalabrasPorBloque(palabraBinario,cantXBloque)
	if (aux1 == 0):
		final = incriptacion(bloques,keyNumero,cantXBloque,ronda)
	else:
		final = desincriptar(bloques,keyNumero,cantXBloque,ronda)
	return decodificar(final)

	# Analisis

# Entrada: Ingresa la clave
# Procedimiento: Se encarga de realizar el analisis.
# Salida:  Se encarga de entregar los graficos que se obtiene al realizar el analisis.

def analisisDeCantidadPorBloque(key):

	print("\n realizando analisis de bits por bloque")

	# Palabra a utilizar:
	palabra = "abcdefghijklmnñopqrstuvwxyz" * 1000
	tiemposI = []
	tiemposD = []
	tiemposTho = []
	ejeY = []
	tiempoI = 0
	tiempoD = 0

	for aux in range (1,11):

		ejeY.append(potenciaDeDos(aux))
		print("Cantidad por bloque: " + str(potenciaDeDos(aux)))

		for repeticion in range (0,10):

			startTime1 = time()
			palabraIncriptada = feistel(potenciaDeDos(aux),key,palabra,8,0,-1)
			elapsedTime1 = time() - startTime1
			print("Tiempo de ronda " + str(aux) + " en I es: " + str(elapsedTime1))
			tiempoI = tiempoI + elapsedTime1

			startTime2 = time()
			palabraIncriptada = feistel(potenciaDeDos(aux),clave,palabraIncriptada,8,1,-1)
			elapsedTime2 = time() - startTime2
			print("Tiempo de ronda " + str(aux) + " en D es: " + str(elapsedTime2))
			tiempoD = tiempoD + elapsedTime2

		tiemposI.append((tiempoI/5))
		tiemposD.append((tiempoD/5))

		tiempoI = 0
		tiempoD = 0

	print(tiemposI)
	print(tiemposD)

	for aux in range(0,len(tiemposI)):
		tiemposTho.append((tiemposI[aux]/tiemposD[aux]))

	print("El tiempo es: ")
	print(tiemposTho)

	grafico("Tiempo v/s Cantidad de bits por bloques - (Incriptación)" , "Tiempo v/s Cantidad de bits por bloques - (Desincriptación)", ejeY, tiemposI,
	tiemposD,"Tiempo","Bits por bloques" , "/Salida/Tiempo_vs_Bits_por_Bloque")

	return 

# Entrada: Ingresa la clave
# Procedimiento: Se encarga de realizar el analisis.
# Salida:  Se encarga de entregar los graficos que se obtiene al realizar el analisis.

def analisisDeCantidadDeRondasImpar(key):

	print("\n realizando analisis de cantidad de rondas")

	# Palabra a utilizar:
	palabra = "abcdefghijklmnñopqrstuvwxyz" * 1000
	tiemposI = []
	tiemposD = []
	ejeY = []
	tiempoI = 0
	tiempoD = 0

	for aux in range (1,33,2):

		ejeY.append(aux)
		print("Cantidad de rondas : " + str(aux))

		for repeticion in range (0,10):

			startTime1 = time()
			palabraIncriptada = feistel(8,key,palabra,aux,0,-1)
			elapsedTime1 = time() - startTime1
			tiempoI = tiempoI + elapsedTime1

			startTime2 = time()
			palabraIncriptada = feistel(8,clave,palabraIncriptada,aux,1,-1)
			elapsedTime2 = time() - startTime2
			tiempoD = tiempoD + elapsedTime2

		tiemposI.append((tiempoI/5))
		tiemposD.append((tiempoD/5))

		tiempoI = 0
		tiempoD = 0

	grafico("Tiempo v/s Cantidad de rondas Impar - (Incriptación)" , "Tiempo v/s Cantidad de rondas Impar- (Desincriptación)", ejeY, tiemposI,
	tiemposD, "Tiempo" ,"Rondas Impar", "/Salida/Tiempo_vs_Cantidad_de_Rondas_Impar")

	return

# Entrada: Ingresa la clave
# Procedimiento: Se encarga de realizar el analisis.
# Salida:  Se encarga de entregar los graficos que se obtiene al realizar el analisis.

def analisisDeCantidadDeRondasPar(key):

	print("\n realizando analisis de cantidad de rondas")

	# Palabra a utilizar:
	palabra = "abcdefghijklmnñopqrstuvwxyz" * 1000
	tiemposI = []
	tiemposD = []
	ejeY = []
	tiempoI = 0
	tiempoD = 0

	for aux in range (2,33,2):

		ejeY.append(aux)
		print("Cantidad de rondas : " + str(aux))

		for repeticion in range (0,10):

			startTime1 = time()
			palabraIncriptada = feistel(8,key,palabra,aux,0,-1)
			elapsedTime1 = time() - startTime1
			tiempoI = tiempoI + elapsedTime1

			startTime2 = time()
			palabraIncriptada = feistel(8,clave,palabraIncriptada,aux,1,-1)
			elapsedTime2 = time() - startTime2
			tiempoD = tiempoD + elapsedTime2

		tiemposI.append((tiempoI/5))
		tiemposD.append((tiempoD/5))

		tiempoI = 0
		tiempoD = 0

	grafico("Tiempo v/s Cantidad de rondas Par - (Incriptación)" , "Tiempo v/s Cantidad de rondas Par - (Desincriptación)", ejeY, tiemposI,
	tiemposD, "Tiempo", "Rondas Par" , "/Salida/Tiempo_vs_Cantidad_de_Rondas_Par")

	return

# Entrada: Ingresa la clave
# Procedimiento: Se encarga de realizar el analisis.
# Salida:  Se encarga de entregar los graficos que se obtiene al realizar el analisis.

def analisisDeLargoDePalabra(key):

	print("\n realizando analisis de cantidad de rondas")

	# Palabra a utilizar:
	palabra = "abcdefghijklmnñopqrstuvwxyz"
	tiemposI = []
	tiemposD = []
	ejeY = []
	tiempoI = 0
	tiempoD = 0
	aumento = 1

	for aux in range (1,6):

		print("Largo de la palabra es: " + str(len(palabra)*aumento))

		ejeY.append(len(palabra)*aumento*8)
		if (aux == 1):
			palabra = palabra * aumento
			aumento = 10

		else:
			palabra = palabra * aumento

		for repeticion in range (0,10):

			startTime1 = time()
			palabraIncriptada = feistel(8,key,palabra,8,0,-1)
			elapsedTime1 = time() - startTime1
			tiempoI = tiempoI + elapsedTime1

			startTime2 = time()
			palabraIncriptada = feistel(8,clave,palabraIncriptada,8,1,-1)
			elapsedTime2 = time() - startTime2
			tiempoD = tiempoD + elapsedTime2

		tiemposI.append((tiempoI/5))
		tiemposD.append((tiempoD/5))

		tiempoI = 0
		tiempoD = 0

	grafico("Tiempo v/s Largo de palabra en bits - (Incriptación)" , "Tiempo v/s Largo de palabra en bits - (Desincriptación)", ejeY, tiemposI,
	tiemposD, "Tiempo" ,"Largo de Palabra - (Bits)", "/Salida/Tiempo_vs_Largo_de_palabra_en_bits")

	return

# Entrada: Ingresa la clave
# Procedimiento: Se encarga de realizar el analisis.
# Salida:  Se encarga de entregar los graficos que se obtiene al realizar el analisis.

def analisisDeLargoDeClave(key):

	print("\n realizando analisis de largo de clave")

	# Palabra a utilizar:
	palabra = "abcdefghijklmnñopqrstuvwxyz" * 1000
	tiemposI = []
	tiemposD = []
	ejeY = []
	tiempoI = 0
	tiempoD = 0

	for aux in range (0,7):

		# Calculando largo de clave al aumentar en 1 el diges_size
		auxPalabra = bytes(key, encoding= 'utf-8')
		aux1 = str(int(blake2b(key=auxPalabra,digest_size=(7+aux)).hexdigest(),16))
		
		print("Vamos en largo de clave: " + str(len(aux1)))

		ejeY.append(str(len(aux1)))

		for repeticion in range (0,10):

			startTime1 = time()
			palabraIncriptada = feistel(8,key,palabra,8,0,aux)
			elapsedTime1 = time() - startTime1
			tiempoI = tiempoI + elapsedTime1

			startTime2 = time()
			palabraIncriptada = feistel(8,clave,palabraIncriptada,8,1,aux)
			elapsedTime2 = time() - startTime2
			tiempoD = tiempoD + elapsedTime2

		tiemposI.append((tiempoI/5))
		tiemposD.append((tiempoD/5))

		tiempoI = 0
		tiempoD = 0

	grafico("Tiempo v/s Largo de clave - (Incriptación)" , "Tiempo v/s Largo de clave - (Desincriptación)", ejeY, tiemposI,
	tiemposD, "Tiempo", "Largo de clave - (Bits)" , "/Salida/Tiempo_vs_Largo_de_clave")

	return

# Entrada: Ingresa la clave, cantidad de rondas y la cantidad de bits que hay por bloque.
# Procedimiento: Se encarga de realizar el analisis.
# Salida:  Se encarga de entregar los graficos que se obtiene al realizar el analisis. 

def analisisAvalancha(key,cantXBloque,ronda):

	print("\n realizando analisis de variacion de incriptar con referencia al largo de clave")

	# Palabra a utilizar:
	palabra1 = "hola como"
	palabra2 = "hora como"
	palabra3 = "hura como"
	palabra4 = "hura cgmo"
	palabra5 = "hura cgmk"
	palabra6 = "qura cgmk"

	palabrasIncriptadas = []
	ejeX = [0]
	ejeY = [0,1,2,3,4,5]
	bloques = []
	lista = []

	passw = key

	# Separando palabra
	palabraBinario1 = binario(palabra1)
	bloques.append(separarPalabrasPorBloque(palabraBinario1,cantXBloque))
	palabraBinario2 = binario(palabra2)
	bloques.append(separarPalabrasPorBloque(palabraBinario2,cantXBloque))
	palabraBinario3 = binario(palabra3)
	bloques.append(separarPalabrasPorBloque(palabraBinario3,cantXBloque))
	palabraBinario4 = binario(palabra4)
	bloques.append(separarPalabrasPorBloque(palabraBinario4,cantXBloque))
	palabraBinario5 = binario(palabra5)
	bloques.append(separarPalabrasPorBloque(palabraBinario5,cantXBloque))
	palabraBinario6 = binario(palabra6)
	bloques.append(separarPalabrasPorBloque(palabraBinario6,cantXBloque))

	# Convirtiendo palabras
	auxPalabra = bytes(passw, encoding= 'utf-8')
	aux = int(blake2b(key=auxPalabra,digest_size=7).hexdigest(),16)

	print("\n")
	for i in range(0,6):
		lista.append(incriptacionAvalancha(bloques[i],aux,cantXBloque,ronda))
	
	for i in range(0,6):
		if (i <= 4 ):
			ejeX.append(calcularDiferencia(lista[0],lista[i+1]))

	print(ejeX)	

	graficoAvalancha("Modificando bits en entrada.png",ejeY,ejeX,"Bits modificados","Cantidad de cambios en bits","/Salida/Bits_Bits_modificados.png")

	return

# Entrada: Parametros necesarios para poder realizar la incriptación de formato avalancha.
# Procedimiento: Se realiza la incriptacion del mensaje (Informe explicado el procedimiento)
# Salida: Entrega el mensaje incriptado 

# Se debe tener en cuenta que se realiza esta función para poder cumplir con los requisitos que se solicitan en el lab, debido que la 
# implemetnacion que se realizo se complicaba la obtención de los parametros que se necesitaban para poder realizar los graficos 
# correspondientes por el enunciado.

def incriptacionAvalancha(bloques,keyNumero,cantXBloque,rondas):

	final = ''
	derechoFinal = ''
	izquierdoFinal = ''
	bloquesNuevos = []
	keyPrincipal = keyNumero
	bloqueAux = []
	bloqueAuxFinal = []
	contador = 0
	for bloque in bloques:
		keyNumero = keyPrincipal
		for ronda in range(0,rondas):
			if (ronda != (rondas-1)):
				corte = int(len(bloque)/2)
				derecho = bloque[corte:]
				izquierdo = bloque[:corte]
				derechoAux = aplicarClave(derecho,keyNumero)
				# cambio de clave para la siguiente ronda
				keyNumero = keyNumero + (ronda+len(str(keyNumero)))
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
			#print(bloque)
			bloqueAux.append(bloque)
		bloqueAuxFinal.append(bloqueAux)
		bloqueAux = []
	return bloqueAuxFinal