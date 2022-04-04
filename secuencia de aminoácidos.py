# DESCRIPCIÓN DEL PROGRAMA:
# Leer una secuencia de aminoácidos (nomenclatura una letra) y mostrar una
# secuencia putativa de ARN.

#                                           <~~ BLOQUE PRINCIPAL ~~>
#                                                   ENTRADA:

# A continuación le pediremos al usuario la cantidad de secuencias de aminoácidos a
# consultar con el programa:
consultas = int(input("Ingrese la cantidad de secuencias de ADN a consultar: "))

# Se definen variables para opción de la cantidad de secuencias para posteriormente
# sumar.
suma = 0 # correspondiente al total de la suma.
suma_a = 0 # correspondiente a la Alanina.
suma_r = 0 # correspondiente a la Arginina.
suma_n = 0 # correspondiente a la Asparagina.
suma_d = 0 # correspondiente al Aspártico.
suma_c = 0 # correspondiente a la Cisteina.
suma_e = 0 # correspondiente al Glutámico.
suma_q = 0 # correspondiente a la Glutamina.
suma_g = 0 # correspondiente a la Glicina.
suma_h = 0 # correspondiente a la Histidina.
suma_i = 0 # correspondiente a la Isoleucina.
suma_l = 0 # correspondiente a la Leucina.
suma_k = 0 # correspondiente a la Lisina.
suma_m = 0 # correspondiente a la Metionina.
suma_f = 0 # correspondiente a la Fenilalalina.
suma_p = 0 # correspondiente a la Prolina.
suma_s = 0 # correspondiente a la Serina.
suma_t = 0 # correspondiente a la Treonina.
suma_w = 0 # correspondiente al Triptófano.
suma_y = 0 # correspondiente a la Tirosina.
suma_v = 0 # correspondiente a la Valina.

# Definimos un ciclo while dependiendo de las veces que ocupará el usuario el
# programa.
i = 1
# Si el número de consultas es mayor o igual a uno, se ejecuta la siguiente acción:
while i <= consultas:
    # Lo que se ejecuta será un input pidiendo la secuencia de aminoácidos
    # para su posterior clasificación:
    secuencias = str(input("Ingrese la secuencia de aminoácidos a consultar: "))

#                                       PROCESAMIENTO:
# Existe un total de 20 aminoácidos, entre los cuales se encuentran:
    # Si se ingresa la Alanina, se ejecuta lo siguiente:
    if secuencias == "A":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_a
        # Aquí se suma y se almacena:
        suma_a = suma_a + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Alanina es GCU.")
    
    # Si se ingresa la Arginina se ejecuta lo siguiente:
    if secuencias == "R":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_r
        # Aquí se suma y se almacena:
        suma_r = suma_r + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Arginina es AGA.")
    
    if secuencias == "N":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_n
        # Aquí se suma y se almacena:
        suma_n = suma_n + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Asparagina es AAU.")
    
    if secuencias == "D":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:        
        suma = suma + suma_d
        # Aquí se suma y se almacena:
        suma_d = suma_d + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman el Aspártico es GAU.")
    
    if secuencias == "C":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:        
        suma = suma + suma_c
        # Aquí se suma y se almacena:
        suma_c = suma_c + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Cisteina es UGU.")
    
    if secuencias == "E":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:       
        suma = suma + suma_e
        # Aquí se suma y se almacena:
        suma_e = suma_e + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman el Glutámico es GAA.")
    
    if secuencias == "Q":
        suma = suma + suma_q
        # Aquí se suma y se almacena:
        suma_q = suma_q + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Glutamina es CAG.")
    
    if secuencias == "G":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_g
        # Aquí se suma y se almacena:
        suma_g = suma_g + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Glicina es GGG.")

    if secuencias == "H":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_h
        # Aquí se suma y se almacena:
        suma_h = suma_h + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Histidina es CAU.")
    
    if secuencias == "I":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_i
        # Aquí se suma y se almacena:
        suma_i = suma_i + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Isoleucina es AUU.")
    
    if secuencias == "L":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_l
        # Aquí se suma y se almacena:
        suma_l = suma_l + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Leucina es UUG.")
    
    if secuencias == "K":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_k
        # Aquí se suma y se almacena:
        suma_k = suma_k + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Lisina es AAA.")
    
    if secuencias == "M":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_m
        # Aquí se suma y se almacena:
        suma_m = suma_m + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Metionina es AUG.")
    
    if secuencias == "F":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_f
        # Aquí se suma y se almacena:
        suma_f = suma_f + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Fenilalalina es UUU.")
    
    if secuencias == "P":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_p
        # Aquí se suma y se almacena:
        suma_p = suma_p + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Prolina es CCC.")
    
    if secuencias == "S":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_s
        # Aquí se suma y se almacena:
        suma_s = suma_s + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Serina es UCU.")
    
    if secuencias == "T":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_t
        # Aquí se suma y se almacena:
        suma_t = suma_t + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Treonina es ACG.")
    
    if secuencias == "W":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_w
        # Aquí se suma y se almacena:
        suma_w = suma_w + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman el Triptófano es UGG.")
    
    if secuencias == "Y":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_y
        # Aquí se suma y se almacena:
        suma_y = suma_y + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Tirosina es UAU.")
    
    if secuencias == "V":
        # A continuación ocuparemos las variables anteriormente definidas para que
        # cada vez que se ejecute esta opción, se almacene y se sume una vez.
        # Aquí se define:
        suma = suma + suma_v
        # Aquí se suma y se almacena:
        suma_v = suma_v + 1
        # Finalmente mostramos por pantalla el tipo de clasificación.
        print("Uno de los tripletes que forman la Valina es GUA.")

    # Rompemos el ciclo while sumandole 1.
    i += 1
#                                   SALIDA:

# Finalmente solo nos resta la salida, donde imprimiremos una pequeña interfaz
# donde nos mostrará el total de veces consultado el programa, junto con cuantas
# veces se consultó una clasificación en específico.
        
print("********************************")
print("El total de los aminoácidos consultados es:",consultas,
", correspondiente a: ")
print("Alanina:",suma_a)
print("Arginina:",suma_r)
print("Asparagina:",suma_n)
print("Aspártico:",suma_d)
print("Cisteina:",suma_c)
print("Glutámico;",suma_e)
print("Glutamina:",suma_q)
print("Glicina:",suma_g)
print("Histidina:",suma_h)
print("Isoleucina:",suma_i)
print("Leucina",suma_l)
print("Lisina:",suma_k)
print("Metionina", suma_m)
print("Fenilalalina:",suma_f)
print("Prolina:",suma_p)
print("Serina:",suma_s)
print("Treonina:",suma_t)
print("Triptófano:",suma_w)
print("Tirosina:",suma_y)
print("Valina:",suma_v)
print("********************************")
print("Programa realizado por Cukidev.")
