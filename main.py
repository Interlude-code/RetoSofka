import random
from jugador import Jugador
from juego import Juego


juego=Juego()
while True:
    opt= input('''Ingrese el numero para la accion seleccionada :
1. Para iniciar una partida
2. Ver estadisticas de jugadores
3. Ingresar nuevas preguntas
4. Para salir
''')
    if opt== '1':
        nombre=input("Ingresa el nombre del participante: ")
        nuevoJugador=Jugador(nombre)
        juego.agregarJugador(nuevoJugador)
        
    elif opt== '2':
        juego.imprimirJugadores()