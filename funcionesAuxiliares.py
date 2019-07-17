import math
import matplotlib.pyplot as plt
import os

	# Funciones auxiliares:

# Entrada:
# Procedimiento:
# Salida: 

def potenciaDeDos(num):
	return 2 ** num

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

	#print("La clave es: " + str(key) + " el largo del bloque es: " + str(len(bloqueDerecho)))
	resul = (key + (key * len(bloqueDerecho))) % len(bloqueDerecho)
	return resul

# Entrada:
# Procedimiento:
# Salida: 

def verificarPotenciaDeDos(cantXBloque):

	for aux in range(0,int(cantXBloque)+1):
		if (int(cantXBloque) == potenciaDeDos(aux)):
			return True
	return False

# Entrada:
# Procedimiento:
# Salida: 

def validarParametros(palabra,cantXBloque,rondas,key):

	if (palabra.replace(' ','').isalpha()):
		if(str(cantXBloque).isdigit() ):
			if(str(rondas).isdigit()):
				if (verificarPotenciaDeDos(cantXBloque)):
					return True
				else:
					#print("\n La cantidad de bloques no es potencia de dos \n")
					return False
			else:
				#print("\n No es numerico la cantidad de rondas \n")
				return False
		else: 
			#print("\n No es numerico la cantidad de bits por bloque \n")
			return False
	else:
		#print("\n Caracteres numericos en la palabra \n")
		return False

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

	nombre = input("\n Ingrese el nombre del archivo a escribir (Sin extension): ")

	archivo = open("./Salida/" + nombre + ".txt" ,'a')

	archivo.write("*********************************************\n")
	archivo.write("\n")
	archivo.write("La palabra a crifrar es: " + palabra + "\n")
	archivo.write("\n")
	archivo.write("La palabra crifrar es: " + palabraIncriptada + "\n")
	archivo.write("El tiempo ocupado fue de: " + str(time1) + "\n")
	archivo.write("\n")
	archivo.write("La palabra al decifrar es: " + palabraDesincriptado +" \n")
	archivo.write("El tiempo ocupado fue de: " + str(time2) + "\n")
	archivo.write("\n")
	archivo.write("*********************************************\n")

	#print("\n Archivo creado con exito \n ")

# Entrada:
# Procedimiento:
# Salida: 

def calcularDiferencia(listaBase, listaGenerada):

	auxDiferencia = 0
	print("lo que llega")
	print(listaGenerada)
	print("base")
	print(listaBase)
	for letra in range(0,len(listaBase)):
		for caracter in range(0,len(listaBase[0])):
			for bits in range(0,len(listaBase[0][0])):
				if (listaBase[letra][caracter][bits] != listaGenerada[letra][caracter][bits]):
					auxDiferencia = auxDiferencia + 1
	print("La diferencia agregar es: " + str(auxDiferencia))
	return auxDiferencia

# Entrada:
# Procedimiento:
# Salida: 

def grafico(titulo1, titulo2, ejeY , ejeX1, ejeX2, nombreY, nombreX, imagen) :

	# Graficos indivduales
	graficoTiempoIndividual(titulo1,ejeY,ejeX1,nombreX,nombreY,imagen + "_1.png")
	graficoTiempoIndividual(titulo2,ejeY,ejeX2,nombreX,nombreY,imagen + "_2.png")

	plt.figure(figsize=(8.0, 5.0))
	plt.subplot(211)
	p1 = plt.plot(linewidth = 2)
	graficoTiempo(titulo1,ejeY,ejeX1,nombreX,nombreY,imagen)
	plt.subplot(212)
	p2 = plt.plot(linewidth = 2)
	graficoTiempo(titulo2,ejeY,ejeX2,nombreX,nombreY,imagen)
	plt.tight_layout()
	plt.savefig(os.getcwd() + imagen + ".png")
	#plt.show() 

# Entrada:
# Procedimiento:
# Salida: 

def graficoTiempo(titulo,x,y,xlabel,ylabel,imagen):

	y = limitarDecimal(y)
	plt.title(titulo, fontsize = 12, color = 'blue')
	plt.xlabel(xlabel, color = 'red')
	plt.ylabel(ylabel, color = 'orange')
	plt.plot(x,y,'o-')
	plt.xticks(x,rotation=20)
	plt.yticks(y,rotation=20)
	plt.savefig(os.getcwd() + imagen)


# Entrada:
# Procedimiento:
# Salida: 

def graficoTiempoIndividual(titulo,x,y,xlabel,ylabel,imagen):

	plt.figure(figsize=(8.0, 5.0))
	y = limitarDecimal(y)
	plt.title(titulo, fontsize = 12, color = 'blue')
	plt.xlabel(xlabel, color = 'red')
	plt.ylabel(ylabel, color = 'orange')
	plt.plot(x,y,'o-')
	plt.xticks(x,rotation=20)
	plt.yticks(y,rotation=20)
	plt.savefig(os.getcwd() + imagen)


# Entrada:
# Procedimiento:
# Salida: 

def graficoAvalancha(titulo,x,y,xlabel,ylabel,imagen):

	y = limitarDecimal(y)
	plt.title(titulo, fontsize = 12, color = 'blue')
	plt.xlabel(xlabel, color = 'red')
	plt.ylabel(ylabel, color = 'orange')
	plt.plot(x,y,'o-')
	plt.xticks(x,rotation=20)
	plt.yticks(y,rotation=20)
	plt.tight_layout()
	plt.savefig(os.getcwd() + imagen)
	#plt.show() 