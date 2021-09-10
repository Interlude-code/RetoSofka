import random
from jugador import Jugador
from juego import Juego
from pregunta import Pregunta



def ingresarPregunta():
    categoriasList=["arte","historia","ciencia","geografia","deporte"]
    nivel=int(input('''Ingresa el numero correspondiente al nivel de dificular de la pregunta
    1.Nivel 1
    2.Nivel 2
    3.Nivel 3
    4.Nivel 4
    5.Nivel 5
    '''))
    if (nivel >= 1 and nivel <=5):
        categoria=int(input('''Ingresa el numero correspondiente a la categoria de la pregunta
    1.Arte
    2.Historia
    3.Ciencia
    4.Geografia
    5.Deporte
     '''))
        if (categoria >= 1 and categoria <=5):
            enunciado=input("Ingresa la pregunta")
            opt1=input("Ingresa la opcion 1")
            opt2=input("Ingresa la opcion 2")
            opt3=input("Ingresa la opcion 3")
            opt4=input("Ingresa la opcion 4")
            correcta=input("Ingresa la opcion correcta")
            pregunta=Pregunta(nivel,categoriasList[categoria],enunciado,opt1,opt2,opt3,opt4,correcta)
            juego.agregarPregunta(pregunta)
            
        else:
            print("Categoria no existente ")
            return
    else:
        print("nivel no existente ")
        return
    

        




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
    elif opt== '3':
       ingresarPregunta()
    elif opt== '4':
       break