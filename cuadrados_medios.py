def cuadrados_medios():
    try:
        # Solicitar la cantidad de corridas
        i = int(input("Ingrese la cantidad de corridas que se harán: "))
        # Solicitar el número de 4 cifras
        x = int(input("Ingrese el número de 4 cifras (El valor de Y): "))
        
        # Verificar que el número sea de 4 cifrasa
        if 1000 <= x <= 9999:
            for _ in range(i):
                # Calcular el cuadrado del número
                cuadrado = x * x
                # Convertir el cuadrado a cadena para manipularlo
                aux_cuad = str(cuadrado)
                longitud = len(aux_cuad)
                
                # Extraer los 4 números del centro
                if longitud % 2 == 0:
                    inicio = (longitud // 2) - 2
                    fin = inicio + 4
                    resultado = aux_cuad[inicio:fin]
                else:
                    # Si la longitud es impar, agregar un cero al inicio
                    aux_cuad = "0" + aux_cuad
                    inicio = (len(aux_cuad) // 2) - 2
                    fin = inicio + 4
                    resultado = aux_cuad[inicio:fin]
                
                # Actualizar el valor de x para la siguiente iteración
                x = int(resultado)
                # Mostrar resultados
                print(f"El número al cuadrado es: {cuadrado}")
                print(f"Los 4 números del centro son: {resultado}")
                print(f"El valor de R es 0.{resultado}\n")
        else:
            print("Error: El número debe ser de 4 cifras.")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

# Ejecutar la función principal
if __name__ == "__main__":
    cuadrados_medios()