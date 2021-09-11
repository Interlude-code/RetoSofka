import json
from pymongo import MongoClient
import random

cluster=MongoClient("mongodb+srv://interlude:Carlos15@cluster0.smza0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["banco_preguntas"]
collection= db["preguntas"]


class Juego():
    def __init__(self):
        self.jugadores=[]
        self.bancoPreguntas=[]


    def agregarJugador(self,nuevoJugador):
        self.jugadores.append(nuevoJugador)  


    def imprimirJugadores(self):
        for jugadores in self.jugadores:
            print(jugadores)

    def imprimirPreguntas(self):
        results=collection.find({})
        for preguntas in results:
            print(preguntas)
    
    def agregarPregunta(self,pregunta):
#        self.preguntas.append(pregunta)
        preguntaDict={"categoria":pregunta.categoria,"enunciado":pregunta.enunciado,"opcion1":pregunta.opt1,"opcion2":pregunta.opt2,"opcion3":pregunta.opt3,"opcion4":pregunta.opt4,"correcta":pregunta.correcta}
        collection.insert_one(preguntaDict)
    def cargarDB(self):
        results=collection.find({}) 
        for preguntas in results:
            self.bancoPreguntas.append(preguntas)
        




#for preguntas in preguntas2:
#    if(preguntas["categoria"] ==2):
#        print("hola")        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    






