# DESCRIPCIÓN DEL PROGRAMA:
# Averiguar la clasificación de cada aminoácido según sus propiedades.

#                       <~~ BLOQUE PRINCIPAL ~~>

#                                   ENTRADA:

# A continuación le pediremos al usuario la cantidad de veces a consultar
# el programa.
consultas = int(input("Ingrese la cantidad de consultas que hará: "))

# Se definen variables para cada opción de aminoácido para posteriormente
# sumar.
suma = 0 # correspondiente al total de la suma.
suma_np = 0 # correspondiente a la suma de los neutro polares.
suma_nnp = 0 # correspondiente a la suma de los neutro no polares.
suma_ac = 0 # correspondiente a los ácidos.
suma_ba = 0 # correspondiente a los básicos.
suma_ar = 0 # correspondiente a los aromáticos.

# Definimos un ciclo while dependiendo de las veces que ocupará el usuario el
# programa.
i = 1
# Si el número de consultas es mayor o igual a uno, se ejecuta la siguiente acción:
while i <= consultas:
    # Lo que se ejecuta será un input pidiendo aminoácidos para su posterior clasificación.
    aminoacido = input("Ingrese la secuencia de aminoácidos: ")


#                                   PROCESAMIENTO:
# Existen distintos cinco tipos de clasificaciones para los aminoácidos:
# 1.- Neutro No Polares, Polares o Hidrófilos.
# 2.- Neutros no Polares, Apolares o Hidrófobos.
# 3.- Con carga negativa o ácidos.
# 4.- Con carga positiva o básicos.
# 5.- Aromáticos.

    # Si el aminoácido corresponde a la primera clasificación, se ejecutará lo siguiente:
    if aminoacido == "S" or aminoacido == "T" or aminoacido == "Q"\
        or aminoacido == "N" or aminoacido == "Y" or aminoacido == "C"\
            or aminoacido == "G":
            # A continuación ocuparemos las variables anteriormente definidas para que
            # cada vez que se ejecute esta opción, se almacene y se sume una vez.
            # Aquí se define:
            suma = suma + suma_np
            # Aquí se suma y se almacena:
            suma_np = suma_np + 1
            # Finalmente mostramos por pantalla el tipo de clasificación.
            print("Su aminoácido pertenece al grupo de los Neutro Polares, \
Polares o Hidrófilos.")

    # Si el aminoácido corresponde a la segunda clasificación, se ejecutará lo siguiente:
    if aminoacido == "A" or aminoacido == "V" or aminoacido == "L"\
        or aminoacido == "I" or aminoacido == "M" or aminoacido == "P"\
            or aminoacido == "F" or aminoacido == "W":
                # A continuación ocuparemos las variables anteriormente definidas para que
                # cada vez que se ejecute esta opción, se almacene y se sume una vez.
                # Aquí se define:
                suma = suma + suma_nnp
                # Aquí se suma y se almacena:
                suma_nnp = suma_nnp + 1
                # Finalmente mostramos por pantalla el tipo de clasificación.
                print("Su aminoácido pertenece al grupo de los Neutro no Polares, \
Apolares o Hidrófobos.")

    # Si el aminoácido corresponde a la tercera clasificación, se ejecutará lo siguiente:
    if aminoacido == "D" or aminoacido == "E":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_ac
        # Aquí se suma y se almacena:
        suma_ac = suma_ac + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Su aminoácido pertenece al grupo con carga negativa o ácidos.")

    # Si el aminoácido corresponde a la cuarta clasificación, se ejecutará lo siguiente:    
    if aminoacido == "K" or aminoacido == "R" or aminoacido == "H":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_ba
        # Aquí se suma y se almacena:
        suma_ba = suma_ba + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Su aminoácido pertenece al grupo con carga positiva o básicos.")

    # Si el aminoácido corresponde a la cuarta clasificación, se ejecutará lo siguiente:           
    if aminoacido == "F" or aminoacido == "Y" or aminoacido == "W":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_ar
        # Aquí se suma y se almacena:
        suma_ar = suma_ar + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Su aminoácido pertenece al grupo de los Aromáticos.")
    
    # Rompemos el ciclo while sumandole 1.
    i += 1
#                                   SALIDA:

# Finalmente solo nos resta la salida, donde imprimiremos una pequeña interfaz
# donde nos mostrará el total de veces consultado el programa, junto con cuantas
# veces se consultó una clasificación en específico.
print("******************************************")
print("El total de veces que ha consultado ha sido:", consultas, "veces. \
Correspondiente a: ")
print("Neutro polares, Polares o Hidrófilos: ",suma_np)
print("Neutro No Polares, Apolares o Hidrófobos: ",suma_nnp)
print("Carga Negativa o Ácidos:",suma_ac)
print("Carga Postiva o Básicos: ",suma_ba)
print("Aromáticos: ",suma_ar)
print("******************************************")
print("Programa realizado por Cukidev.")
