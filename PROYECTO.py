# menu
# las opciones se proponen por caracteres
opA = "0"
opcion = '0'

while not (opcion == '9'):
    print("/=======MENU PRINCIPAL=======\ ")
    print(' 1. Arreglo')
    print(' 2. Registro')
    print(' 3. Cadenas')
    print(' 4. Punteros')
    print(' 5. Ordenamiento')
    print(' 0. Salir')

    opcion = input('Que opcion desea ver---> ')

    if (opcion == '1'):
        while not (opA == "9"):
            print(' /=======menu Arreglos =======\ ')
            print("1. Arreglos Unidimensionales")
            print("2. Arreglos Bidimensionales")
            print("3. Arreglo N-Dimensionales")
            print("4. SALIR")

            opA = input(
                "Que arreglo desea mostrar ---> ")
            if (opA == "1"):
                print("==========EJEMPLOS DE ARREGLO UNIDIMENSIONAL==========")
                print("[1,5,8,3,30,9,13]")
                A = [1, 5, 8, 3, 30, 9, 13]
                B = []
                for i in A:
                    if i > 3 and i % 2 != 0:
                        B.append(i)
                print("Los valores impares mayor a 3 son-->", B)
                opcA = input("¿Desea ver otro ejemplo? SI[1] O NO[2]-->")
                if (opcA == "1"):
                    # Crear dos arreglos
                    print("Primer arreglo es --> [1, 2 , 3 ,4 ,5]")
                    print("Segundo arreglo es --> [6, 7 , 8 ,9 ,10]")

                    arreglo1 = [1, 2, 3, 4, 5]
                    arreglo2 = [6, 7, 8, 9, 10]

                    # Sumar elementos de dos arreglos
                    resultado_suma = [a + b for a,
                                      b in zip(arreglo1, arreglo2)]
                    print("Resultado de la suma de dos arreglos:", resultado_suma)

                    # Multiplicar cada elemento de un arreglo por 2
                    arreglo_multiplicado = [x * 2 for x in arreglo1]
                    print(" Primer arreglo multiplicado por 2",
                          arreglo_multiplicado)
                    arreglo_multi = [x * 2 for x in arreglo2]
                    print(" Segundo arreglo multiplicado por 2:", arreglo_multi)

                elif (opcA == "2"):
                    break
            elif (opA == "2"):
                print("==========EJEMPLOS DE ARREGLO BIDIMENSIONAL==========")
                arreglis = [
                    [4, 5, 2],
                    [3, 7, 8],
                ]
                print(arreglis[0][2])
                opcB = input("¿Desea ver otro ejemplo? SI[1] O NO[2]-->")
                if (opcB == "1"):
                    # Crear dos matrices
                    print("Primera matriz")
                    print("[5,2,2]")
                    print("[8,2,6]")
                    print("[3,7,9]")

                    print("Segunda matriz")
                    print("[9,3,7]")
                    print("[2,8,6]")
                    print("[5,5,9]")
                    matriz1 = [
                        [5, 2, 2],
                        [8, 2, 6],
                        [3, 7, 9]
                    ]

                    matriz2 = [
                        [9, 3, 7],
                        [2, 8, 6],
                        [5, 5, 2]
                    ]

                    # Sumar elementos de dos matrices
                    resultado_suma = [
                        [a + b for a, b in zip(fila1, fila2)]
                        for fila1, fila2 in zip(matriz1, matriz2)
                    ]

                    print("Resultado de la suma de dos matrices:")
                    for fila in resultado_suma:
                        print(fila)

                    # Multiplicar cada elemento de una matriz por 2
                    matriz_multiplicada = [[x * 2 for x in fila]
                                           for fila in matriz1]
                    print("Pimera Matriz multiplicada por 2:")
                    for fila in matriz_multiplicada:
                        print(fila)

                    matriz_multiplicada = [[x * 2 for x in fila]
                                           for fila in matriz2]
                    print("Segunda Matriz multiplicada por 2:")
                    for fila in matriz_multiplicada:
                        print(fila)
                elif (opcB == "2"):
                    break
            elif (opA == "3"):
                print("==========EJEMPLO DE ARREGLO N DIMENSIONAL==========")
                arregndim = [
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                    ],
                    [
                        [10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18],
                    ],
                    [
                        [19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27],
                    ]
                ]
                print(arregndim[1][0][2])
            elif (opA == "4"):
                break

    elif (opcion == '2'):
        print(' /======= Ejemplo Registro =======\ ')
        fruta = {}
        fruta["Fruta"] = input("Ingrese Nombre de la Fruta --> ")
        fruta["Cantidad"] = float(input("Ingrese la cantidad --> "))
        fruta["Estado"] = input("Estado de la fruta --> ")
        fruta["Precio"] = float(input("Ingrese valor de la fruta -->$"))
        print("==========================================================")
        for key, value in fruta.items():
            print(f"{key} : {value}")

    elif (opcion == '3'):
        print(' /======= Ejemplo Cadenas =======\ ')
        foro = """
        Erase una vez un león con mucha hambre que vivía en el bosque. Un buen día buscando ocasión para encontrar 
        presa fácil que llevarse al estomago se encontró con una oveja y le preguntó que le parecía su aliento.
        La oveja sin pensar mucho el riesgo o las consecuencias le respondió con sinceridad que era apestoso. 
        Entonces el león fingió sentirse ofendido, le dio un golpe y la mató a la vez que le decía: “Por haber 
        ofendido a tu rey, eso es lo que te has ganado” y se la comió. Tras un rato el león volvió a hacerle la misma pregunta 
        a una cabra que deambulaba por allí. La cabra que había visto lo que le había ocurrido a su amiga la oveja temió por su vida y le 
        respondió que su aliento era maravilloso. 
        El león se molestó, la mató y se la comió al tiempo que le decía “Por adularme con falsedades es lo que te mereces”.
        A continuación se dirigió a la zorra que también había observado las dos situaciones anteriores y le repitió la misma pregunta. 
        La zorra, algo más astuta viéndose venir que podía acabar como la oveja o la cabra, se alejó de él y desde la distancia le habló:
        “De buena fe, le informo que no puedo responder a su pregunta puesto que el resfriado que poseo me impide percibir su aliento”.
        Así se salvo la zorra de ser devorada por el león. 
        """
        print(foro)
        print("Numero de caracteres que se encuentran en el cuento son--> ", len(foro))
        print("En este ejemplo se utilizo el comando de cadena <len> el cual cuanta cuantos caracteres tiene el cuento ")
    elif (opcion == '4'):
        # En Python, no manejamos punteros directamente como en otros lenguajes
        # Pero podemos simular el concepto usando referencias a objetos (como mencionado anteriormente)
        # Ejemplo de referencia a objeto
        print("/=======Ejemplo de Puntero=======\ ")
        print("Los valores de y equivale a 0 pero sera cambiado con los valores que contenga X")
        x = [1, 2, 3]
        y = x  # y ahora referencia al mismo objeto que x
        y[0] = 10
        print("Valor de x después de modificar y:", x)
    elif (opcion == '5'):
        print("/=======Ejemplo de Ordenamiento=======\ ")
        print("Los valores a ordenar de este ejemplo son:")
        print("[3,1,4,1,5,9,2,6,5,3]")
        numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        for i in range(len(numeros)):
            min_index = i
            for j in range(i + 1, len(numeros)):
                if numeros[j] < numeros[min_index]:
                    min_index = j
            numeros[i], numeros[min_index] = numeros[min_index], numeros[i]
        print("Ordenamiento por selección:", numeros)
    elif (opcion == '0'):
        print(' **** Saliendo del menu  ****')
        break
    else:
        print('No existe la opcion en el menu')
