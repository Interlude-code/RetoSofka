import json
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://interlude:Carlos15@cluster0.smza0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["banco_preguntas"]
collection= db["preguntas"]


class Juego():
    def __init__(self):
        self.jugadores=[]
        self.preguntas=[]


    def agregarJugador(self,nuevoJugador):
        self.jugadores.append(nuevoJugador)  


    def imprimirJugadores(self):
        for jugadores in self.jugadores:
            print(jugadores)

    def imprimirPreguntas(self):
        for preguntas in self.preguntas:
            print(preguntas)
    
    def agregarPregunta(self,pregunta):
#       self.preguntas.append(pregunta)
        preguntaDict={"nivel":pregunta.nivel,"categoria":pregunta.categoria,"enunciado":pregunta.enunciado,"opcion1":pregunta.opt1,"opcion2":pregunta.opt2,"opcion3":pregunta.opt3,"opcion4":pregunta.opt4,"correcta":pregunta.correcta}
        collection.insert_one(preguntaDict)
        

#    def listToDict(self):
#        col.insert_one(diccionarioPreguntas)
#        for pregunta in self.preguntas:
#            if(pregunta.nivel==1):
#                diccionarioPreguntas={
#                    pregunta.nivel:{
#                        pregunta.categoria:[
#                            {"enunciado":pregunta.enunciado,"opt1":pregunta.opt1,"opt2":pregunta.opt2,"opt3":pregunta.opt3,"opt4":pregunta.opt4,"correcta":pregunta.correcta}
#                       ]
#
#                    }
#                }
            
        
   