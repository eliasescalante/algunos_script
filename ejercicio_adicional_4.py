"""
2)  Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso 
hasta que lo introduzca correctamente.

3) Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100:

🖐 Ayuda: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range
(inicio, fin, salto) indica un salto de números.

4) Escribe un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media 
aritmética.
"""

# asigno a una variable un menu en donde el usuario elige ingresando con una cadena de string la eleccion.
eleccion_de_programa_a_correr = input("""\telige que programa que quieres correr:...\n
                                           _____________
                                           ejercicio 1
                                           ejercicio 2
                                           ejercicio 3

                                           ______________\n\n :::""")
# realizo una multi-estructura condicional para comparar la eleccion con las diferentes elecciones
# uso el metodo lower() para minimizar el error en las comparaciones.
#aca inicia el primer programa
if eleccion_de_programa_a_correr.lower() == "ejercicio 1":
    #pido al usuario el ingreso del numero impar
    numero = input("\tpor favor ingrese un numero impar...")
    #evaluo si lo ingresado es un numero y si es impar
    if numero.isnumeric() and int(numero) % 2 != 0:
        print("el numero ingresado es impar...")
    # en caso de que no sea impar evalñuo si sigue siendo un numero y si es par.
    elif numero.isnumeric() and int(numero) % 2 == 0:
        # realizo un ciclo while donde corta el ciclo si el numero es impar en caso contrario se cicla hasta que se ingrese un numero impar
        while int(numero) % 2 == 0:
            #imprimo por consola el mensaje que el numero no cumple la condicion
            print("el numero ingresado no es impar...")
            #pido al usuario que ingrese nuevamente un numero
            numero = (input("\tpor favor ingrese un numero impar..."))
            #evaluo si el numero ingresado es un numero y lo convierto a valor entero
            if numero.isnumeric():
                numero = int(numero)
            #en caso contrario imprimo el mensaje de que ingrese un numero
            else:
                print("\npor favor ingrese un numero...")
        # al cortar el while es porque el numero ingresado es impar por lo tanto se imprime el mensaje de que es impar
        print("el numero ingresado es impar...")
    else:
        print("error al digitar solo se aceptan numeros")
#aca inicia el segundo programa.
elif eleccion_de_programa_a_correr.lower() == "ejercicio 2":
    #declaro una variable y la inicializo con 0
    suma = 0
    #realizo un ciclo for para iterar usando el metodo range 
    for numero in range(0, 100):
        #realizo una estructura condicional para evaluar cada numero que se itera para saber si es impar o no
        # si es impar se suma en caso contrario no hace nada y sigue iterando.
        if (int(numero))%2!= 0 :
             suma += numero
    # por ultimo al salir del for se imprime el mensaje concatenado al resultado de la suma
    print(f"la suma de los numeros impares de 0 a 100 es: {suma}")
#aca comienza el tercer programa
elif eleccion_de_programa_a_correr.lower() == "ejercicio 3":
    #asigno a una variable la cantidad de veces que se va a ciclar el ingreso de numeros a la lista
    cantidad_de_numeros = input("\tpor favor determine cuantos numeros va a ingresar...\n")
    # declaro la variable donde voy a pedir al usuario que ingrese los numeros a agregar a la lista
    numero_a_agregar = 0
    # declaro una variable para la lista y esta esta vacia
    lista_de_numeros = []
    # evaluo si lo que ingreso el usuario es un numero
    if cantidad_de_numeros.isnumeric():
        # si es un numero lo convierto a entero y le resto uno para poder ingresar si elige 4 numeros que sean 4 y no 5 porque empieza desde el 0
        cantidad_de_numeros = int(cantidad_de_numeros) - 1
        #realizo una repeticion condicional comparando la cantidad ingresada por el usuario, cuando llega a 0 se corta el ciclo.
        while cantidad_de_numeros >= 0:
            # en cada repeticion pido al usuario que ingrese un numero
            numero_a_agregar = input("\tpor favor ingrese un numero...\n")
            # evaluo si es un numero
            if numero_a_agregar.isnumeric():
                #si es numero convierto a entero el valor ingresado por el usuario
                numero_a_agregar = int(numero_a_agregar)
                # con el metodo append() voy agregando cada numero a la lista en  cada ciclo
                lista_de_numeros.append(numero_a_agregar)
                # y voy restando a la cantidad ingresada por el usuario (contador)
                cantidad_de_numeros -= 1
            else:
                # en caso de que no sea un numero imprimo mensaje y se repite el ciclo sin descontar al contador la vuelta
                print("\tpor favor ingrese un numero...\n")
        # imprimo la lista de numeros ingresada
        print(f"\t los numeros ingresados son: {lista_de_numeros}\n")
    else:
        # si lo que ingresa no es un numero imprime mensaje de error
        print("\tsolo puede ingresarse valores numericos\n")

