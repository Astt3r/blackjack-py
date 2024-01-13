import random

def obtener_nombre():
    nombre = input("Ingrese su nombre: ")
    while nombre == '':
        nombre = input("Por favor, ingrese su nombre: ")
    return nombre.title()

def obtener_carta(mazo):
    return random.choice(mazo)

def calcular_puntaje(mano):
    puntos = sum(carta[0] for carta in mano)
    ases = sum(1 for carta in mano if carta[1] == 'As')
    
    while puntos > 21 and ases:
        puntos -= 10
        ases -= 1

    return puntos

def mostrar_cartas(mano, titulo):
    print(f'\n {titulo} ')
    print('*' * 20, '\n')
    
    for carta in mano:
        print(carta[1])

def jugar_otra_ronda():
    return input('\n¿Deseas jugar otra ronda? (s/n): ').lower() == 's'

def main():
    nombre_jugador = obtener_nombre()

    while True:
        mazo = [
            (1, 'As'), (2, 'Dos'), (3, 'Tres'), (4, 'Cuatro'),
            (5, 'Cinco'), (6, 'Seis'), (7, 'Siete'), (8, 'Ocho'),
            (9, 'Nueve'), (10, 'Diez'), (10, 'Jota'), (10, 'Reina'),
            (10, 'Rey')
        ]

        puntos_jugador = 0
        puntos_crupier = 0
        ases_en_mano_jugador = 0
        ases_en_mano_crupier = 0
        mano_jugador = []
        mano_crupier = []

        carta1 = obtener_carta(mazo)
        carta2 = obtener_carta(mazo)
        mano_jugador.extend([carta1, carta2])

        mostrar_cartas(mano_jugador, 'Tus cartas')
        
        carta3 = obtener_carta(mazo)
        carta4 = obtener_carta(mazo)
        mano_crupier.extend([carta3, carta4])

        puntos_jugador = calcular_puntaje(mano_jugador)
        puntos_crupier = calcular_puntaje(mano_crupier)

        print(f'\nTus puntos: {puntos_jugador}\n')
        
        print('\nCartas del crupier')
        print('*' * 20, '\n')
        print(carta3[1])

        opcion = int(input('\n¿Qué deseas hacer? 1. Plantarse | 2. Pedir carta: '))
        
        while opcion != 2 and opcion != 1:
            opcion = int(input('Opción invalida. Por favor, ingrese "1" si deseas plantarte o "2" para pedir una carta: '))

        while opcion == 2 and puntos_jugador < 21:
            carta5 = obtener_carta(mazo)
            mano_jugador.append(carta5)
            puntos_jugador = calcular_puntaje(mano_jugador)

            mostrar_cartas(mano_jugador, 'Tus cartas')
            
            print(f'\nTus puntos: {puntos_jugador}\n')

            if puntos_jugador < 21:
                opcion = int(input('\n¿Qué deseas hacer? 1. Plantarse | 2. Pedir carta: '))
                while opcion != 2 and opcion != 1:
                    opcion = int(input('Opción invalida. Por favor, ingrese "1" si deseas plantarte o "2" para pedir una carta: '))
            elif puntos_jugador > 21:
                print('¡Te pasaste de 21! Has perdido.')

        while puntos_crupier < 17:
            carta6 = obtener_carta(mazo)
            mano_crupier.append(carta6)
            puntos_crupier = calcular_puntaje(mano_crupier)

            while puntos_crupier > 21 and ases_en_mano_crupier:
                puntos_crupier -= 10
                ases_en_mano_crupier -= 1

        mostrar_cartas(mano_crupier, 'Cartas del crupier')
        print(f'\nPuntos del crupier: {puntos_crupier}\n')

        if puntos_crupier > 21:
            print(f'El crupier se ha pasado de 21. ¡Felicidades {nombre_jugador}! Has ganado.')
        elif puntos_crupier == 21:
            print('El crupier ha obtenido 21. ¡Lo siento! Has perdido.')
        elif puntos_jugador == puntos_crupier:
            print('¡Empate!')
        elif puntos_jugador > puntos_crupier and puntos_jugador < 21:
            print(f'¡Felicidades {nombre_jugador}! Has ganado.')
        elif puntos_crupier > puntos_jugador and puntos_crupier < 21:
            print('El crupier ha ganado por más puntos. ¡Lo siento!')
        else:
            print('El crupier ha ganado.')

        if not jugar_otra_ronda():
            print(f'\nGracias por jugar, {nombre_jugador} ¡Hasta luego!')
            break

if __name__ == "__main__":
    main()
