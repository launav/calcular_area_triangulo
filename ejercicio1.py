# Función para comprobar que los datos introducidos son válidos
def entrada_valida(valor):
    try:
        valor_int = int(valor)  # Intenta convertir el valor a entero
        return valor_int
    except ValueError:
        return None # Devuelve none si no es válido


# Declaramos una variable para la base y comprobamos si el valor introducido en el input es válido
base = entrada_valida(input("introduce la base del triángulo: "))

# Si base es válida y es mayor a 0:
if base is not None and base > 0:

    # Declaramos la variable altura y comprobamos si el valor introducido es correcto
    altura = entrada_valida(input("introduce la altura del triángulo: "))

    # Si el valor de altura es válido y mayor que 0:
    if altura is not None and altura > 0:

        # Funcion para calcular el area del triangulo
        def calcular_area_triangulo(base, altura):

            # Cálculamos el área del triángulo
            area = (base * altura) / 2

            # Mostramos el mensaje en pantalla
            print(f"El área es igual a {area}")

            # Pasamos a entero el valor de área
            entero = int(area)

            # Comprobamos si es par o impar
            if entero % 2 == 0:
                print("El área del triángulo es par")
            else:
                print("El área del triángulo es impar")


        # Llamamos a la funcion
        calcular_area_triangulo(base, altura)
    else:
        # Mostramos un mensaje informando al usuario que el valor de altura no es válido
        print("El valor de la altura no es válido")
else:
    # Mostramos un mensaje informando al usuario que el valor de base no es válido
    print("El valor introducido de la base no es válido")
