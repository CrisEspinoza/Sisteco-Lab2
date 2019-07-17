import sys
import getopt
from funcionesAuxiliares import validarParametros
from funciones import orquestador

def main():
    
    palabra = ''
    bitsPorBloque = 0
    rondas = 0
    clave = ''

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "w:b:r:c:", ["palabra=", "bitsPorBloque=" , "rondas=" , "clave="])
    except getopt.GetoptError as err:
        print(err) 

    for opt, arg in opts:
        if opt in ["-w", "--palabra"]:
            palabra = arg
        elif opt in ["-b", "--bitsPorBloque"]:
            bitsPorBloque = arg
        elif opt in ["-r", "--rondas"]:
            rondas = arg
        elif opt in ["-c", "--clave"]:
            clave = arg

    print("palabra: " + palabra)
    print("bitsPorBloque : " + str(bitsPorBloque))
    print("rondas: " + str(rondas))
    print("clave: " + clave)

    if (validarParametros(palabra,bitsPorBloque,rondas,clave) == False):
        print("Parametros no validos")
        return 
        
    orquestador(palabra,int(bitsPorBloque),int(rondas),clave)

main()