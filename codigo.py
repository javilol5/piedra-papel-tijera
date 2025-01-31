import random

opciones = ['piedra', 'papel', 'tijera']
#opciones = ['piedra', 'papel', 'tijera', 'lagarto', 'spock']


reglas = {
    'piedra': ['tijera'],
    'papel': ['piedra'],
    'tijera': ['papel'],
    }





#reglas = {
#    'piedra': ['tijera', 'lagarto'],
#    'papel': ['piedra', 'spock'],
#    'tijera': ['papel', 'lagarto'],
#    'lagarto': ['spock', 'papel'],
#    'spock': ['tijera', 'piedra']
#    }

persona = input(f"Elige entre {', '.join(opciones)}: ").lower()

maquina = random.choice(opciones)

print(f"Tú elegiste: {persona}")
print(f"La máquina eligió: {maquina}")

if persona not in opciones:
    print(f"Elección no válida. Por favor, elige entre {', '.join(opciones)}.")
elif persona == maquina:
    print("¡Es un empate!")
elif maquina in reglas[persona]:
    print("¡Ganaste!")
else:
    print("Perdiste, mejor suerte la próxima vez.")
