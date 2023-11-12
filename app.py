import random

elementos = ["piedra", "papel", "tijeras"]

# Pedir al usuario que elija un elemento
jugador = input("Elige piedra, papel o tijeras: ")

# Elegir un elemento aleatorio para el equipo
equipo = random.choice(elementos)

# Comparar los elementos y determinar el ganador
if jugador == equipo:
    resultado = "Empate"
elif jugador == "piedra" and equipo == "tijeras":
    resultado = "Ganaste"
elif jugador == "tijeras" and equipo == "papel":
    resultado = "Ganaste"
elif jugador == "papel" and equipo == "piedra":
    resultado = "Ganaste"
else:
    resultado = "Perdiste"

# Mostrar el resultado
print(f"Elegiste {jugador} y el equipo eligió {equipo}. {resultado}!")
