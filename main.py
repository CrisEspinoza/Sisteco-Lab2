# Menu : 

def menu():

	opcion = 0

	while opcion != '3':

		print("\n")
		print("	1. Ingresar palabra a Incriptar")
		print("	2. Inscribir archivo con resultado")
		print("	3. Salir")
		print("\n")

		opcion = input(" Ingrese la opcion a realizar: ")

		if (opcion == '1'):
			print("Opcion 1")
			input("Presione una tecla para continuar ... .. . \n")

		if (opcion == '2'):
			print("Opcion 2")
			input("Presione una tecla para continuar ... .. . \n")
		
		if(opcion == '3'):
			print("\n")
			print("Gracias por preferirnos")
			print("\n")
menu()