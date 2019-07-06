# Menu : 

def menu():

	opcion = 0

	do:
		switch:
			case: print("1")
	while(opcion != 3 );


	print(arreglo)
	print("\n")

	particion = int(len(arreglo)/2)
	print("La partición se tiene que realizar en la posicione " + str(particion) + " del arreglo \n")

	# Realizando pariticones

	bloqueDerecho = arreglo[:particion]
	bloqueIzquierdo = arreglo[particion:]

	# Mostramos las particiones realizadas

	print(bloqueDerecho)
	print(bloqueIzquierdo)

	print( str(bin(bloqueDerecho[0])) + " " + str(bin(bloqueDerecho[1])) + " " + str(bin(bloqueIzquierdo[0])) + " " + str(bin(bloqueIzquierdo[1])) + "\n" )

	# Aplicamos la llave al lado izquierda

	rPrima = aplicarClave(bloqueIzquierdo,7)

	print("R-prima es: " + str(rPrima))
	print("R-prima en binario es: " + str(bin(rPrima)) + "\n")

	# Juntando en un numero el bloque derecho

	num1 = int(bloqueDerecho[0])
	num2 = int(bloqueDerecho[1])

	print(bin(int(bloqueDerecho[0])))
	print(bin(int(bloqueDerecho[1])))

	numDerecho = bin( num1 and num2 )
	print("El numero binario del derecho es:  " + numDerecho + "\n")

	# Calculando el numero final:

	num1 = int(numDerecho,2)
	num2 = int(rPrima)

	print("Numero derecho es: " + str(num1))
	print("Numero izquierda (Despues de llave) es: " + str(num2))

	numDerechoFinal = bin(num1 | num2)
	
	print("El resultado final de derecho es: " + str(numDerechoFinal) + "\n")

	# Salida final 

	print( str(bin(bloqueDerecho[0])) + " " + str(bin(bloqueDerecho[1])) + " " + str(numDerechoFinal))

	print("La palabra era: " + str(bin(bloqueDerecho[0])) + " " + str(bin(bloqueDerecho[1])) + " " + str(bin(bloqueIzquierdo[0])) + " " + str(bin(bloqueIzquierdo[1])) + "\n")
	
	# Aca es donde no me calza, debido que si me quiero dvolver no podria ... (Tengo esa duda )