def productos_medios():
    # Solicitar la cantidad de corridas
    corridas = int(input("¿Cuántas corridas dará el programa? "))
    print()

    # Solicitar los valores de X e Y
    X = int(input("Introducir el valor de X: "))
    Y = int(input("Introducir el valor de Y: "))
    print()

    # Verificar que X e Y sean números de 4 dígitos
    if 999 < X < 10000 and 999 < Y < 10000:
        for _ in range(corridas):
            # Multiplicar X e Y
            producto = X * Y
            producto_str = str(producto)

            # Ajustar la longitud si es impar
            if len(producto_str) % 2 != 0:
                producto_str = "0" + producto_str

            # Extraer los 4 dígitos centrales
            mitad = len(producto_str) // 2
            inicio = mitad - 2
            fin = inicio + 4
            digitos_centrales = producto_str[inicio:fin]

            # Actualizar los valores de X e Y
            X = Y
            Y = int(digitos_centrales)

            # Mostrar resultados
            print("El número al cuadrado es:", producto)
            print("Los 4 números del centro son:", digitos_centrales)
            print("El valor de R es 0." + digitos_centrales)
            print()
    else:
        print("Error: X e Y deben ser números de 4 dígitos (1000 a 9999).")

# Llamar a la función para ejecutar el programa
productos_medios()