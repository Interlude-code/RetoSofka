
from jugador import Jugador
from juego import Juego
from pregunta import Pregunta




def ingresarPregunta():
    categoria=int(input('''Ingresa el numero correspondiente a la categoria de la pregunta
    1.Categoria 1
    2.Categoria 2
    3.Categoria 3
    4.Categoria 4
    5.Categoria 5
    '''))
    if (categoria >= 1 and categoria <=5):
        enunciado=input("Ingresa la pregunta ")
        opt1=input("Ingresa la opcion 1 ")
        opt2=input("Ingresa la opcion 2 ")
        opt3=input("Ingresa la opcion 3 ")
        opt4=input("Ingresa la opcion 4 ")
        correcta=int(input("Ingresa el numero de la opción correcta "))
        pregunta=Pregunta(categoria,enunciado,opt1,opt2,opt3,opt4,correcta)
        juego.agregarPregunta(pregunta)
            
    else:
        print("Categoria no existente ")
        return

juego=Juego()
while True:
    juego.cargarDB()
    opt= input('''Ingrese el numero para la accion seleccionada :
1. Para iniciar una partida
2. Ver estadisticas de jugadores
3. Ingresar nuevas preguntas
4. Imprimir preguntas
5. Para salir
''')
    if opt== '1':
        nombre=input("Ingresa el nombre del participante: ")
        nuevoJugador=Jugador(nombre)
        juego.rondas(nuevoJugador)

        
    elif opt== '2':
        juego.imprimirJugadores()
    elif opt== '3':
       ingresarPregunta()
    elif opt== '4':
       juego.imprimirPreguntas()
    elif opt== '5':
       break