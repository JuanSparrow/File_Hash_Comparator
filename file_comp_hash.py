import os.path
import time
import hashlib

'''Verificación de ficheros duplicados mediante el calculo de sus hashes. Cuando se pasa la ruta, poner un slash (/) 
al final para que funcione. Testeado en Windows 11 Pro contra una ruta de red y ruta local. '''

ver = "1.0.0"

# Para medir el tiempo de ejecución total del programa
inicio_tiempo = time.time()

# Pedimos ruta
ruta = input("Ruta: ")
files = os.listdir(ruta)

# Para calular cuantos registros se van a procesar
long = int()

# Lista donde se almacenan los registros procesados con su nombre de archivo y hash
lista = []

# Listas donde se almacenan los repetidos y no repetidos tras ser procesados
norep = []
repe = []


def md5hash(fichero):
    # Funcion de extracción del hash md5 por ser más rápido
    try:
        ruta_fichero = open(ruta + fichero, 'rb')
        md5 = hashlib.md5()
        md5.update(ruta_fichero.read())
        print("MD5: ", md5.hexdigest(), '\n')
        return md5.hexdigest()
    except Exception as error:
        print("Error al calcular el hash: ", error)


try:
    # Procesado de los registros en la ruta dada
    for a in files:
        long = len(files)

    print("Procesando ", long, " registros...")

    for archivo in files:
        long = len(files)
        print("Por favor, espere, procesando registro: ", archivo)
        # Se calcula el hash y se guarda en la lista junto con el nombre
        hashfile = md5hash(archivo)
        lista.append((archivo, hashfile))

        # Se hace la verificacion para encontrar los duplicados
        for hashed_f in lista:
            if hashed_f not in norep:
                norep.append(hashed_f)
            else:
                if hashed_f not in repe:
                    repe.append((archivo, hashed_f))
    # Se imprime la lista de repetidos
    print(repe)

except Exception as e:
    print("Error: ", e)

fin_tiempo = time.time()

# Se imprime lo que se ha tardado en realizar todos los calculos
print(round(fin_tiempo-inicio_tiempo), 3)
