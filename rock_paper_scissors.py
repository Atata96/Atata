import random

OPTIONS = ['piedra', 'papel', 'tijera']

def resultado(usuario, maquina):
    if usuario == maquina:
        return 'Empate'
    if (
        (usuario == 'piedra' and maquina == 'tijera') or
        (usuario == 'tijera' and maquina == 'papel') or
        (usuario == 'papel' and maquina == 'piedra')
    ):
        return '¡Ganaste!'
    return 'Perdiste :('

def jugar():
    while True:
        eleccion_usuario = input('Elige piedra, papel o tijera (o salir para terminar): ').lower()
        if eleccion_usuario == 'salir':
            print('Juego terminado.')
            break
        if eleccion_usuario not in OPTIONS:
            print('Opción no válida. Intenta de nuevo.')
            continue
        eleccion_maquina = random.choice(OPTIONS)
        print(f'La máquina eligió: {eleccion_maquina}')
        print(resultado(eleccion_usuario, eleccion_maquina))

if __name__ == '__main__':
    jugar()
