'''
El siguiente es un programa que simula el problema de Monty Hall. En el se muestra, a través
de la simulación de varias partidas, que la mejor estrategia a largo plazo es, para el participante, cambiar siempre de puerta.
La cantidad de partidas que se evalúan son 10.000, pero podría simularse con un mayor número.
'''

import random

partidas_cambio = 0
gana_cambio = 0
pierde_cambio = 0


while partidas_cambio <= 10000:
    #Definimos las posibles elecciones que se tienen
    puertas = [0,1,2]
    #Determinamos, al azar, cuál es la puerta ganadora
    puertaGanadora = random.randint(0,2)
    #Definimos, al azar, qué puerta seleccionaría el participante
    puertaSeleccionada = random.randint(0,2)

    #Quitamos la puerta seleccionada por el participante del arreglo
    del puertas[puertaSeleccionada]

    #Determinamos la puerta que abriría Monty para mostrar que es una puerta perdedora
    puertaAbierta = puertas[random.randint(0,1)]
    while puertaAbierta == puertaGanadora:
        puertaAbierta = puertas[random.randint(0, 1)]
    
    #Eliminamos del arreglo la puerta que abre Monty, ya que no es una elección posible
    puertas.remove(puertaAbierta)

    #Ahora el participante cambia su elección. Es decir, se queda con la puerta que queda en el arreglo
    puertaSeleccionada = puertas[0]

    #Comprobamos si el participante ganó
    if puertaSeleccionada == puertaGanadora:
        gana_cambio += 1
    else:
        pierde_cambio += 1

    partidas_cambio += 1

print("La cantidad de veces que ganó el participante cambiando de puerta es de: ",gana_cambio)
print("La cantidad de veces que perdió el participante cambiando de puerta es de: ",pierde_cambio)
print("El porcentaje de acierto es de ",int((gana_cambio*100)/10000),"%")

print("----------------")

partidas = 0
gana = 0
pierde = 0

while partidas <= 10000:
    # Definimos las posibles elecciones que se tienen
    puertas = [0, 1, 2]
    # Determinamos, al azar, cuál es la puerta ganadora
    puertaGanadora = random.randint(0, 2)
    # Definimos, al azar, qué puerta seleccionaría el participante
    puertaSeleccionada = random.randint(0, 2)

    # Quitamos la puerta seleccionada por el participante del arreglo
    del puertas[puertaSeleccionada]

    # Determinamos la puerta que abriría Monty para mostrar que es una puerta perdedora
    puertaAbierta = puertas[random.randint(0, 1)]
    while puertaAbierta == puertaGanadora:
        puertaAbierta = puertas[random.randint(0, 1)]

    # Comprobamos si el participante ganó
    if puertaSeleccionada == puertaGanadora:
        gana += 1
    else:
        pierde += 1

    partidas += 1

print("La cantidad de veces que ganó el participante SIN cambiar de puerta es de: ", gana)
print("La cantidad de veces que perdió el participante SIN cambiar de puerta es de: ", pierde)
print("El porcentaje de acierto es de ",int((gana*100)/10000),"%")