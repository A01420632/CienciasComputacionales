ARCHIVOS_DATASET = [
    "torre.txt",
    "rey.txt",
    "peon.txt",
    "dama.txt",
    "caballo.txt",
    "alfil.txt",
]
ARCHIVO_PRUEBA = "prueba.txt"


def leer_archivo(ruta):
    matriz = []

    try:
        archivo = open(ruta, "r")
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")
        return []

    for linea in archivo:
        texto = linea.strip()
        if texto == "":
            continue

        valores = texto.split()
        if len(valores) == 1:
            fila = []
            for valor in valores[0]:
                fila.append(valor)
        else:
            fila = valores

        fila_numeros = []
        for valor in fila:
            if valor != "0" and valor != "1":
                print(f"El archivo {ruta} solo debe contener 0 y 1.")
                archivo.close()
                return []
            if valor == "0":
                fila_numeros.append(-1.0)
            else:
                fila_numeros.append(1.0)
        matriz.append(fila_numeros)

    archivo.close()
    return matriz


def matriz_a_vector(matriz):
    vector = []
    for fila in matriz:
        for valor in fila:
            vector.append(valor)
    return vector


def productoC(m1, m2):
    cruz = []
    longitud = len(m1)

    for i in range(longitud):
        fila = []
        for j in range(longitud):
            fila.append(m1[i] * m2[j])
        cruz.append(fila)

    return cruz


def construir_pesos(patrones):
    cantidad_neuronas = len(patrones[0])
    pesos = []

    for i in range(cantidad_neuronas):
        fila = []
        for j in range(cantidad_neuronas):
            suma = 0.0
            for patron in patrones:
                producto = productoC(patron, patron)
                suma += producto[i][j]

            if i == j:
                fila.append(0.0)
            else:
                fila.append(suma)
        pesos.append(fila)

    return pesos


def recordar(entrada, pesos):
    actual = entrada[:]
    iteracion = 0
    maximo = 50

    while iteracion < maximo:
        iteracion += 1
        siguiente = []

        for j in range(len(pesos)):
            suma = 0.0
            for i in range(len(actual)):
                suma += actual[i] * pesos[i][j]

            if suma > 0:
                siguiente.append(1.0)
            elif suma < 0:
                siguiente.append(-1.0)
            else:
                siguiente.append(actual[j])

        print(f"U({iteracion}) = {siguiente}")

        if siguiente == actual:
            return siguiente, iteracion

        actual = siguiente

    return actual, iteracion


def contar_iguales(patron1, patron2):
    iguales = 0
    for i in range(len(patron1)):
        if patron1[i] == patron2[i]:
            iguales += 1
    return iguales


def reconocer(patron, patrones, nombres):
    mejor_indice = 0
    mayor_cantidad = contar_iguales(patron, patrones[0])

    for i in range(1, len(patrones)):
        cantidad = contar_iguales(patron, patrones[i])
        if cantidad > mayor_cantidad:
            mejor_indice = i
            mayor_cantidad = cantidad

    return nombres[mejor_indice], mayor_cantidad


def main():
    patrones = []
    nombres = []
    filas = 0
    columnas = 0

    for nombre in ARCHIVOS_DATASET:
        matriz = leer_archivo("dataset/" + nombre)
        if len(matriz) == 0:
            return

        if filas == 0:
            filas = len(matriz)
            columnas = len(matriz[0])
        elif len(matriz) != filas or len(matriz[0]) != columnas:
            print("Todas las figuras del dataset deben tener el mismo tamaño.")
            return

        vector = matriz_a_vector(matriz)
        if len(vector) != filas * columnas:
            print("Todas las filas del dataset deben tener el mismo tamaño.")
            return

        patrones.append(vector)
        nombres.append(nombre.replace(".txt", ""))

    entrada_matriz = leer_archivo(ARCHIVO_PRUEBA)
    if len(entrada_matriz) == 0:
        print("El archivo prueba.txt está vacío o no es válido.")
        return

    if len(entrada_matriz) != filas:
        print(f"prueba.txt debe tener {filas} filas.")
        return

    entrada = matriz_a_vector(entrada_matriz)
    if len(entrada) != filas * columnas:
        print(f"Cada fila de prueba.txt debe tener {columnas} valores.")
        return

    print(f"Se cargaron {len(patrones)} patrones del dataset.")
    print(f"Cada patrón tiene {filas * columnas} neuronas.")

    pesos = construir_pesos(patrones)
    recuperado, iteraciones = recordar(entrada, pesos)
    nombre, cantidad = reconocer(entrada, patrones, nombres)

    print(f"\nLa red se estabilizó en {iteraciones} iteraciones.")
    print(f"prueba.txt se parece más a: {nombre}")
    print(f"Coinciden {cantidad} de {len(recuperado)} posiciones.")


main()
