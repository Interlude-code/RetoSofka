import json


class Juego():
    def __init__(self):
        self.jugadores=[]
        self.preguntas=[]


    def agregarJugador(self,nuevoJugador):
        self.jugadores.append(nuevoJugador)  


    def imprimirJugadores(self):
        for jugadores in self.jugadores:
            print(jugadores)
    
    def agregarPregunta(self,pregunta):
        self.preguntas.append(pregunta)
        self.listToDict()

    def listToDict(self):

        for pregunta in self.preguntas:
            diccionarioPreguntas={
                pregunta.nivel:{
                    pregunta.categoria:[
                        {"enunciado":pregunta.enunciado,"opt1":pregunta.opt1,"opt2":pregunta.opt2,"opt3":pregunta.opt3,"opt4":pregunta.opt4,"correcta":pregunta.correcta,}
                    ]

                }
            }
        with open('preguntas.json','w')as jsonFile:
            json.dump(diccionarioPreguntas,jsonFile)
            jsonFile.close()

   