def multiplicador_constante():
    # Solicitar la cantidad de veces que se correrá el programa
    i = int(input("¿Cuántas veces se correrá el programa? "))
    print()

    # Solicitar el valor de X
    X = int(input("Ingrese el valor de X: "))
    print()

    # Solicitar el valor de la constante C
    C = int(input("Ingrese el valor de la Constante: "))
    print()

    for _ in range(i):
        Multi = C * X
        AuxMulti = str(Multi)
        Longitud = len(AuxMulti)

        # Ajustar la longitud si es impar
        if Longitud % 2 != 0:
            AuxMulti = "0" + AuxMulti

        # Calcular los 4 números del centro
        inicio = (len(AuxMulti) // 2) - 2
        fin = inicio + 4
        resultado = AuxMulti[inicio:fin]

        # Actualizar el valor de X
        X = int(resultado)

        # Mostrar resultados
        print("El número al cuadrado es:", Multi)
        print("Los 4 números del centro son:", resultado)
        print("El valor de R es 0." + resultado)
        print()

# Llamar a la función para ejecutar el programa
multiplicador_constante()