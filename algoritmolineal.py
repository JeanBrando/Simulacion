

def generar_numeros_aleatorios(semilla, a, c, m, cantidad):
    numeros_aleatorios = []
    x = semilla
    
    for _ in range(cantidad):
        # Calcular el siguiente valor de X
        x = (a * x + c) % m
        # Calcular el número aleatorio r
        r = x / (m - 1)
        # Agregar el número aleatorio a la lista
        numeros_aleatorios.append(r)
    
    return numeros_aleatorios

# Solicitar parámetros al usuario
try:
    semilla = int(input("Ingrese la semilla inicial (X0): "))
    a = int(input("Ingrese el multiplicador (a): "))
    c = int(input("Ingrese el incremento (c): "))
    m = int(input("Ingrese el módulo (m): "))
    cantidad = int(input("Ingrese la cantidad de números aleatorios a generar: "))
    
    # Validar que el módulo sea mayor que 1
    if m <= 1:
        print("Error: El módulo (m) debe ser mayor que 1.")
    else:
        # Generar los números aleatorios
        numeros_aleatorios = generar_numeros_aleatorios(semilla, a, c, m, cantidad)
        
        # Mostrar los resultados
        print("\nNúmeros aleatorios generados:")
        for i, r in enumerate(numeros_aleatorios, start=1):
            print(f"r{i} = {r:.4f}")
except ValueError:
    print("Error: Por favor, ingrese valores enteros válidos.")