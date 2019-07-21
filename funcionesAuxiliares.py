import math
import matplotlib.pyplot as plt
import os

	# Funciones auxiliares:

# Entrada: Entero a ver su numero a ver su potencia de dos.
# Procedimiento: Se encarga de realizar la potencia de dos.
# Salida: Entrega el numero elevado a su potencia de dos.

def potenciaDeDos(num):
	return 2 ** num

# Entrada: Entra el caracter y la cantidad de numeros que se desea llegar.
# Procedimiento: Se encarga de aumentar los bits del caracter ingresado, hasta la cantidad de numero que se solicita.
# Salida: Entrega el nuevo caracter con los bits correspodientes agregados.

def llenarBits(caracter,numLlenado):

	while len(caracter) != numLlenado:
		caracter = '0' + caracter
	return caracter

# Entrada: Entra el caracter y la cantidad de numeros que se desea llegar.
# Procedimiento: Se encarga de aumentar los bits del caracter ingresado, hasta la cantidad de numero que se solicita.
# Salida: Entrega el nuevo caracter con los bits correspodientes agregados hacia la derecha.

def llenarBitsDerecha(caracter,numLlenado):

	while len(caracter) != numLlenado:
		caracter = caracter + '0' 
	return caracter

# Entrada: Entra la palabra a convertir.
# Procedimiento: Se encarga de entregar la palabra ingresdo en formato de bits.
# Salida: Entrega la cadena de bits que describe a la palabra que se ingreso como parametro.

def binario(palabra):

	texto = ""
	for caracter in palabra:
		aux = format(ord(caracter),'b')
		aux = llenarBits(aux,8)
		texto = texto + aux
	return texto

# Entrada: Entran dos caracteres a ser operados.
# Procedimiento: Se encarga de realizar la operacion xor a los dos parametros ingresados.
# Salida: Entrega la salida luego de realizar la operación.

def funcionXor (aux1, aux2):

	result = ''.join('0' if i == j else '1' for i, j in zip(aux1,aux2))
	return result

# Entrada: Entra el numero y el largo que se desea tener.
# Procedimiento: Se encarga de entregar en formato de binario al numero ingresado segun el largo que se ingresa por parametro.
# Salida: Entrega el valor numerico obtenido luego de realizar la operación.

def numToBin (numero,largo):

	binario = '{0:b}'.format(numero)
	binario = llenarBits(binario,largo)
	return binario

# Entrada: Entra los bloques que contiene los bits de las palabras.
# Procedimiento: Se encarga de ir codificando los bloques, primero une de 8 en 8 y luego va decodifcando a que letra corresponde.
# Salida: Entrega el los bits ingresados en formato de texto, que corresponde al mensaje enviado por el emisor.

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

# Entrada: Ingresa la palabra y la cantidad ed bits que contiene cada bloque.
# Procedimiento: Se realiza la separación de las palabras por la cantidad de bloques correspondientes a cada uno, tener en cuenta que si faltan datos 
#				se colocan adionales hacia el lado faltante de bits.
# Salida: Se entrega la salida correspondientes a los blqoues formados segun la cantidad de palabra que contenia el mensaje.

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

# Entrada: Entra el bloque derecho y la clave
# Procedimiento: Se realiza el procedimiento que corresponde a la funcion F.
# Salida:  Entrega el reultado luego de haber realizado el procedimiento de la función F.

def aplicarClave(bloqueDerecho,key):

	#print("La clave es: " + str(key) + " el largo del bloque es: " + str(len(bloqueDerecho)))
	resul = (key + (key * len(bloqueDerecho))) % len(bloqueDerecho)
	return resul

# Entrada: Cantidad de bits por bloque
# Procedimiento: Se encarga de verificar si la cantidad ingresada es potencia de dos.
# Salida:  Entrega un valor booleano en caso que cumpla o no con la condicion mencionada.

def verificarPotenciaDeDos(cantXBloque):

	for aux in range(0,int(cantXBloque)+1):
		if (int(cantXBloque) == potenciaDeDos(aux)):
			return True
	return False

# Entrada: Entran los parametros de entrada.
# Procedimiento: Se encarga de verificar si los parametros cumplen con la condiciones necesarias para poder ser un parametro de entrada.
# Salida: Se encarga de entregar un valor booelano, si cumple con las condiciones necesarias.

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

# Entrada: Ingresa un valor numerico
# Procedimiento: Se encarga de limitar dicho decimal a la cantidad de 5 decimales.
# Salida:  Se encarga de entregar el valor con la cantidad de decimales correspondientes.
	
def limitarDecimal(x):

	contador = 0
	for num in x:
		x[contador] = round(num,5)
		contador = contador + 1
	return x

# Entrada: Entran los parametros que se van a escribir en el archivo.
# Procedimiento: Se encarga de generar el archivo y escribir los parametros correspondientes
# Salida: Entrega el archivo de salida con los parametros ingresados.

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

# Entrada: Entran dos lista de bits.
# Procedimiento: Se calcula la difrerencia que contiene las listas ingresadas.
# Salida: Entrega el numero de diferencia que contienen las listas.

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

# Entrada: Parametros necesaios para poder realizar el grafico.
# Procedimiento: Se encarga de realizar el grafico en conjunto y individual.
# Salida:  Entrega el grafico y su guardado del mismo.

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

# Entrada: Parametros necesaios para poder realizar el grafico.
# Procedimiento: Se encarga de realizar el grafico individual.
# Salida:  Entrega el grafico y su guardado del mismo. 

def graficoTiempo(titulo,x,y,xlabel,ylabel,imagen):

	y = limitarDecimal(y)
	plt.title(titulo, fontsize = 12, color = 'blue')
	plt.xlabel(xlabel, color = 'red')
	plt.ylabel(ylabel, color = 'orange')
	plt.plot(x,y,'o-')
	plt.xticks(x,rotation=20)
	plt.yticks(y,rotation=20)
	plt.savefig(os.getcwd() + imagen)


# Entrada: Parametros necesaios para poder realizar el grafico.
# Procedimiento: Se encarga de realizar el grafico individual.
# Salida:  Entrega el grafico y su guardado del mismo. 

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


# Entrada: Parametros necesaios para poder realizar el grafico.
# Procedimiento: Se encarga de realizar el grafico individual.
# Salida:  Entrega el grafico y su guardado del mismo. 

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