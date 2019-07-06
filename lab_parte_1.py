import hashlib
import math

clave = 0
largo = 0

def aplicarClave(bloqueDerecho,key):

	##print("La clave recibida es: " + str(key))
	##print("El bloque es: " + bloqueDerecho)
	##print("El bloque pasado a entero es: " + str(int(bloqueDerecho,2)))

	resul = key % len(bloqueDerecho)
	#print(str(int(bloqueDerecho,2) ))
	#print("Resul es: " + str(resul))

	return resul

def llenarBits(caracter,numLlenado):

	##print("El largo es: " + str(len(caracter)))
	while len(caracter) != numLlenado:
		caracter = '0' + caracter

	##print("El caracter que devuelvo es: " + str(caracter))
	return caracter

def llenarBitsDerecha(caracter,numLlenado):

	##print("El largo es: " + str(len(caracter)))
	while len(caracter) != numLlenado:
		caracter = caracter + '0' 

	##print("El caracter que devuelvo es: " + str(caracter))
	return caracter

def binario(palabra):

	texto = ""
	for caracter in palabra:
		##print("El caracter es: *" + caracter + "*")
		##print("El binario de la palabra es: " + format(ord(caracter),'b'))
		aux = format(ord(caracter),'b')
		aux = llenarBits(aux,8)
		texto = texto + aux
		##print("El caracter original es: " + chr(int(aux,2)))
		##print("\n")

	return texto

def funcionXor (aux1, aux2):

	result = ''.join('0' if i == j else '1' for i, j in zip(aux1,aux2))

	return result

def numToBin (numero,largo):

	binario = '{0:b}'.format(numero)
	binario = llenarBits(binario,largo)
	return binario

def decodificar(bloques):

	texto = ''
	textoFinal = ''

	for bloque in bloques:
		#print(bloque)
		texto = texto + bloque

	#print("El texto es: " + texto)

	contador = 0
	while contador < len(texto):
		#print("EL valor de contador es: " + str(contador))
		#print("La palabra a buscar es: " + texto[contador:(contador+8)])
		aux = chr(int(texto[contador:(contador+8)], 2))
		#print("La letra es: " + texto)
		textoFinal = textoFinal + aux
		contador = contador + 8
	
	#print("El texto en binario es: " + texto + " el texto en palabra es: " + textoFinal)

	return textoFinal

def separarPalabrasPorBloque(palabraBinario, cantXBloque):
	
	print("La cantidad x bloques es: " + str(cantXBloque) )
	print("El largo de la palabra es: " + str(len(palabraBinario)))
	
	cantBloque = math.ceil(len(palabraBinario)/cantXBloque)
	print("La cantidad de bloques es: " + str(cantBloque))
	#print("La palabra a separar es: " + palabraBinario)

	if (cantBloque < 1):
		cantBloque = 1
		palabraBinario = llenarBits(palabraBinario,cantXBloque)
		#print("Largo que pide bloque es: " + str(cantXBloque) + " El largo de mi palabra es: " + str(len(palabraBinario)))

	bloques = []

	for aux in range(0,cantBloque):
		##print("Indice: " + str((aux*cantXBloque)) + " Superior es: " + str(((aux*cantXBloque)+cantXBloque)))
		binAux = palabraBinario[(aux*cantXBloque):((aux*cantXBloque)+cantXBloque)]
		print("Esto es:" + binAux)
		binAux = llenarBitsDerecha(binAux,cantXBloque)
		print("LO nuevo es: " + binAux)
		bloques.append(binAux)
		##print(bloques[aux])

	return bloques

def mezclar(bloques,keyNumero,cantXBloque,rondas):

	final = ''
	derechoFinal = ''
	izquierdoFinal = ''
	bloquesNuevos = []
	keyPrincipal = keyNumero

	#print("Los bloques son: ")
	#print(bloques)
	#print("La llave es: " + str(keyNumero))
	#print("La cantidad de bloques es: " + str(cantXBloque))
	#print("La cantidad de rondas son: " + str(rondas))

	for bloque in bloques:

		#print("El bloques : " + bloque)
		keyNumero = keyPrincipal

		for ronda in range(0,rondas):

			if (ronda != (rondas-1)):

				#print("Ronda numero: " + str(ronda+1))
				corte = int(len(bloque)/2)
			
				derecho = bloque[corte:]
				izquierdo = bloque[:corte]
				##print("Espacio derecho: ")
				##print(derecho)
				##print("Espacio izquierdo: ")
				##print(izquierdo)
				##print("\n")

				print("La clave es: " + str(keyNumero) + "\n")
				derechoAux = aplicarClave(derecho,keyNumero)
				keyNumero = keyNumero + (len(bloque)*cantXBloque) + (ronda+1)
				#print("Despues de aplicar la llave queda como: ")
				derechoAuxBin = numToBin(derechoAux,len(derecho))
				#print(derecho + " - Despues: " + str(derechoAux) + " - En binario es: " + derechoAuxBin)
				derechoAuxFinal = funcionXor(izquierdo,derechoAuxBin)
				#print("Antes es: " + derechoAuxBin + " - Despues de xor es: " + derechoAuxFinal)

				izquierdoFinal = derecho
				derechoFinal = derechoAuxFinal
				
				#print("El derecho final es: " + derechoFinal)
				#print("El izquierdo final es: " + izquierdoFinal)
				final = izquierdoFinal + derechoFinal
				#print("Antes completo es: " + bloque + " - Ahora es: " + final)
				bloque = final
				#print("\n")

			else:
				#print("Ronda numero: " + str(ronda+1))
				corte = int(len(bloque)/2)
			
				derecho = bloque[corte:]
				izquierdo = bloque[:corte]
				##print("Espacio derecho: ")
				##print(derecho)
				##print("Espacio izquierdo: ")
				##print(izquierdo)
				##print("\n")

				print("La clave es: " + str(keyNumero) + "\n")
				derechoAux = aplicarClave(derecho,keyNumero)
				global clave 
				clave = keyNumero
				print("Clave a utilizar es:" + str(clave))
				#print("Despues de aplicar la llave queda como: ")
				derechoAuxBin = numToBin(derechoAux,len(derecho))
				#print(derecho + " - Despues: " + str(derechoAux) + " - En binario es: " + derechoAuxBin)
				derechoAuxFinal = funcionXor(izquierdo,derechoAuxBin)
				#print("Antes es: " + derechoAuxBin + " - Despues de xor es: " + derechoAuxFinal)

				izquierdoFinal = derechoAuxFinal
				derechoFinal = derecho
				
				#print("El derecho final es: " + derechoFinal)
				#print("El izquierdo final es: " + izquierdoFinal)
				final = izquierdoFinal + derechoFinal
				#print("Antes completo es: " + bloque + " - Ahora es: " + final)
				bloque = final
				#print("\n")

		bloquesNuevos.append(bloque)

	#print("Los bloques antiguos son: ")
	#print(bloques)
	#print("Los bloques nuevos son:")
	#print(bloquesNuevos)

	return bloquesNuevos

def mezclar1(bloques,keyNumero,cantXBloque,rondas):

	final = ''
	derechoFinal = ''
	izquierdoFinal = ''
	bloquesNuevos = []
	keyPrincipal = keyNumero

	#print("Los bloques son: ")
	#print(bloques)
	#print("La llave es: " + str(keyNumero))
	#print("La cantidad de bloques es: " + str(cantXBloque))
	#print("La cantidad de rondas son: " + str(rondas))

	for bloque in bloques:

		#print("El bloques : " + bloque)
		keyNumero = keyPrincipal
		print("\n" + "La clave es: " + str(keyNumero) + "\n")

		for ronda in range(0,rondas):

			if (ronda != (rondas-1)):

				#print("Ronda numero: " + str(ronda+1))
				corte = int(len(bloque)/2)
			
				derecho = bloque[corte:]
				izquierdo = bloque[:corte]
				##print("Espacio derecho: ")
				##print(derecho)
				##print("Espacio izquierdo: ")
				##print(izquierdo)
				##print("\n")

				print("La clave es: " + str(keyNumero) )
				derechoAux = aplicarClave(derecho,keyNumero)
				keyNumero = keyNumero - (len(bloque)*cantXBloque) + (ronda+1)
				#print("Despues de aplicar la llave queda como: ")
				derechoAuxBin = numToBin(derechoAux,len(derecho))
				#print(derecho + " - Despues: " + str(derechoAux) + " - En binario es: " + derechoAuxBin)
				derechoAuxFinal = funcionXor(izquierdo,derechoAuxBin)
				#print("Antes es: " + derechoAuxBin + " - Despues de xor es: " + derechoAuxFinal)

				izquierdoFinal = derecho
				derechoFinal = derechoAuxFinal
				
				#print("El derecho final es: " + derechoFinal)
				#print("El izquierdo final es: " + izquierdoFinal)
				final = izquierdoFinal + derechoFinal
				#print("Antes completo es: " + bloque + " - Ahora es: " + final)
				bloque = final
				#print("\n")

			else:
				#print("Ronda numero: " + str(ronda+1))
				corte = int(len(bloque)/2)
			
				derecho = bloque[corte:]
				izquierdo = bloque[:corte]
				##print("Espacio derecho: ")
				##print(derecho)
				##print("Espacio izquierdo: ")
				##print(izquierdo)
				##print("\n")

				print("La clave es: " + str(keyNumero))
				derechoAux = aplicarClave(derecho,keyNumero)
				#print("Despues de aplicar la llave queda como: ")
				derechoAuxBin = numToBin(derechoAux,len(derecho))
				#print(derecho + " - Despues: " + str(derechoAux) + " - En binario es: " + derechoAuxBin)
				derechoAuxFinal = funcionXor(izquierdo,derechoAuxBin)
				#print("Antes es: " + derechoAuxBin + " - Despues de xor es: " + derechoAuxFinal)

				izquierdoFinal = derechoAuxFinal
				derechoFinal = derecho
				
				#print("El derecho final es: " + derechoFinal)
				#print("El izquierdo final es: " + izquierdoFinal)
				final = izquierdoFinal + derechoFinal
				#print("Antes completo es: " + bloque + " - Ahora es: " + final)
				bloque = final
				#print("\n")

		bloquesNuevos.append(bloque)

	#print("Los bloques antiguos son: ")
	#print(bloques)
	#print("Los bloques nuevos son:")
	#print(bloquesNuevos)

	return bloquesNuevos


def feistel(cantXBloque,key,palabra,ronda,aux1):

	#print("\n")
	#print("Comienza una nueva ronda\n")
	#print("\n")

	final = ''
	palabraBinario = binario(palabra)
	#print("El texto ingresado es binario es: \n" + palabraBinario)

	if (aux1 == 0):
		keyNumero = hash(key*10**-1)
	else:
		keyNumero = key
	#keyNumero = key
	#print("La key Numero es: " + str(keyNumero) + "\n")

	bloques = separarPalabrasPorBloque(palabraBinario,cantXBloque)
	#print("Se muestra las palabras por bloques \n")
	#print(bloques)

	if (aux1 == 0):
		final = mezclar(bloques,keyNumero,cantXBloque,ronda)
	else:
		final = mezclar1(bloques,keyNumero,cantXBloque,ronda)

	#print("El resultado a devolver es:")
	#print(final)

	return decodificar(final)

def menu(cantXBloque,key,cantRondas,aux,aux1):

	palabra = feistel(cantXBloque,key,aux,cantRondas,aux1)

	return palabra

a = menu(64,357,16,"hola soy el cristian jajajajajajajajajajajaja",0)
print(a.replace(' ',''))

#print("\n")
print("\n")
print("Ahora vamos a decodificar *" + a + "*")
print("\n")
#print("\n")

b = menu(64,clave,16,a,1)
print(b)