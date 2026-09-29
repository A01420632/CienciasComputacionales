N = int(input("Introduce la dimensión de las matrices: "))

x1 = []
print(f"Introduce las {N} filas de x1:")
for i in range(N):
    fila = [float(x) for x in input(f"Fila {i + 1}: ").split()]
    x1.append(fila)

x2 = []
print(f"Introduce las {N} filas de x2:")
for i in range(N):
    fila = [float(x) for x in input(f"Fila {i + 1}: ").split()]
    x2.append(fila)


#Transposicion

m1 = []
for fila in x1:
    for valor in fila:
        m1.append(-1.0 if valor == 0 else 1.0)

m2 = []
for fila in x2:
    for valor in fila:
        m2.append(-1.0 if valor == 0 else 1.0)


def productoC(m1, m2):
    cruz = []
    long = len(m1)
    for i in range(long):
        fila = []
        for j in range(long):
            fila.append(m1[i] * m2[j])
        cruz.append(fila)
    return cruz

r1 = productoC(m1, m1)
r2 = productoC(m2, m2)

#Paso: Suma de matrices

l = len(m1)
W = []
for i in range(l):
    fila = []
    for j in range(l):
        if i == j:
            fila.append(0.0)
        else:
            fila.append(r1[i][j] + r2[i][j])
    W.append(fila)

print("\nMatriz X1^T * X1")
for f in r1:
    print(f)

print("\nX2^T * X2")
for f in r2:
    print(f)

print("\nMatriz con diagonal:")
for f in W:
    print(f)


#Analisis de patron
entrada = input("\nIntroduce el patrón a evaluar: ")
A = [float(x) for x in entrada.split()]

MAX = 50
iter = 0
flag = False

while iter < MAX:
    iter += 1

    res = []
    for j in range(len(W)):
        suma = 0
        for i in range(len(A)):
            suma += A[i] * W[i][j]
        res.append(suma)

    #Formato de resultado segun la funcion f
    U1 = []
    for j in range(len(res)):
        x = res[j]
        if x > 0:
            U1.append(1.0)
        elif x < 0:
            U1.append(-1.0)
        else:
            U1.append(A[j])

    print(f"U({iter})= {U1}")

    if U1 == A:
        flag = True
        print(f"Iteracion {iter} y patron mas cercano: {U1}")
        break

    A = U1

if not flag:
    print("No se puede encontrar un patron concreto")