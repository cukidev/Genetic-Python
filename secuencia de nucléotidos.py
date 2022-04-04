# DESCRIPCIÓN DEL PROGRAMA:
# Clasificar las bases nitrogenadas como purínicas y pirimidínicas.

#                                        <~~ BLOQUE PRINCIPAL ~~>
#                                               ENTRADA:

# A continuación, le pediremos al usuario la cantidad de veces a consultar
#el programa:
consultas = int(input("Ingrese la cantidad de consultas que realizará: "))

# Definimos variables para cada base nitrogenada:
# correspondiente al total de veces consultadas, lo definiré en otra variable para no alterarlo:
total = consultas 
suma = 0 # correspondiente al total de la suma.
bn_a = 0 # correspondiente a la suma de la base nitrogenada A.
bn_g = 0 # correspondiente a la suma de la base nitrogenada G.
bn_t = 0 # correspondiente a la suma de la base nitrogenada T.
bn_c = 0 # correspondiente a la suma de la base nitrogenada C.

# Definimos el ciclo while dependiendo de las veces que se ocupará el
# programa:
i = 1
# Si el número de consultas es mayor o igual a uno, se ejecuta la siguiente acción:
while i <= consultas:
    # Lo que se ejecuta es un input pidiendo las bases nitrogenadas
    base_nitrogenada = input("Ingrese las bases nitrogenadas a consultar: ")

#                                             PROCESAMIENTO:
# Dependiendo de la base nitrogenada ingresada, existirán distintas clasificaciones
# 1.- Base nitrogenada A, correspondiente a las purínicas.
# 2.- Base nitrogenada G, correspondiente a las purínicas.
# 3.- Base nitrogenada T, correspondiente a las pirimidínicas.
# 4.- Base nitrogenada C, correspondiente a las pirimidínicas.

    #Si la base corresponde a la primera clasificación, se ejecuta lo siguiente:
    if base_nitrogenada == "A":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + bn_a
        # Aquí se suma y se almacena:
        bn_a = bn_a + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Su base nitrogenada es purínica.")

        #Si la base corresponde a la segunda clasificación, se ejecuta lo siguiente:
    if base_nitrogenada == "G":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:       
        suma = suma + bn_g
        # Aquí se suma y se almacena:
        bn_g = bn_g + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Su base nitrogenada es purínica.")

    #Si la base corresponde a la tercera clasificación, se ejecuta lo siguiente:
    if base_nitrogenada == "T":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + bn_t
        # Aquí se suma y se almacena:
        bn_t = bn_t + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Su base nitrogenada es pirimidínica.")
        #Si la base corresponde a la cuarta clasificación, se ejecuta lo siguiente:
    if base_nitrogenada == "C":
        #A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + bn_c
        # Aquí se suma y se almacena:
        bn_c = bn_c + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Su base nitrogenada es pirimidínica.")
    # Rompemos el ciclo while.
    i += 1

# En el siguiente apartado, realizaremos los cálculos para sacar el porcentaje.

# Para las proporciones purínicas, sumamos el total de las bases que la componen:
# base nitrogenada A y base nitrogenada G,se divide por el total de veces consultadas
# Y finalemente se multiplica por 100 para sacar un porcentaje.
proporcion_purinicas = ((bn_a + bn_g)/ total) * 100
# Para las proporciones piriminídicas, sumamos el total de las bases que la componen:
# base nitrogenada T y base nitrogenada C,se divide por el total de veces consultadas
# Y finalemente se multiplica por 100 para sacar un porcentaje.
proporcion_pirimidinicas = ((bn_t + bn_c) / total) * 100
# Para la proporción de A, lo dividimos por el total de veces consultadas y se
# multiplica por 100 para sacar un porcentaje.
proporcion_a = (bn_a / total) * 100
# Para la proporción de G, lo dividimos por el total de veces consultadas y se
# multiplica por 100 para sacar un porcentaje.
proporcion_g = (bn_g / total) * 100
# Para la proporción de T, lo dividimos por el total de veces consultadas y se
# multiplica por 100 para sacar un porcentaje.
proporcion_t = (bn_t / total) * 100
# Para la proporción de C, lo dividimos por el total de veces consultadas y se
# multiplica por 100 para sacar un porcentaje.
proporcion_c = (bn_c / total) * 100

#                                                 SALIDA:
# Por último, solo nos falta la salida, donde imprimiremos una interfaz que
# nos mostrará las proporciones anteriormente calculadas junto con sus respectivos
# porcentajes.
print("****************************************************************")
print("Proporción bases purínicas sobre el total: ",proporcion_purinicas, "%")
print("Proporción bases pirimidínicas sobre el total: ",proporcion_pirimidinicas,"%")
print("****************************************************************")
print("Proporción de A sobre el total: ", proporcion_a,"%")
print("Proporción de G sobre el total: ", proporcion_g,"%")
print("Proporción de T sobre el total: ", proporcion_t,"%")
print("Proporción de C sobre el total: ", proporcion_c,"%")
print("****************************************************************")
print("Total bases nitrogenadas consultadas: ",total,)
print("****************************************************************")
print("Programa realizado por Cukidev.")
