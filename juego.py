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
        self.seleccionJugador=''


    def agregarJugador(self,nuevoJugador):
        self.jugadores.append(nuevoJugador)  


    def imprimirJugadores(self):
        for jugadores in self.jugadores:
            print(jugadores)


    def imprimirPreguntas(self):
        results=collection.find({})
        for preguntas in results:
            print(preguntas["enunciado"])


    
    def agregarPregunta(self,pregunta):
#        self.preguntas.append(pregunta)
        preguntaDict={"categoria":pregunta.categoria,"enunciado":pregunta.enunciado,"opcion1":pregunta.opt1,"opcion2":pregunta.opt2,"opcion3":pregunta.opt3,"opcion4":pregunta.opt4,"correcta":pregunta.correcta}
        collection.insert_one(preguntaDict)


    def cargarDB(self):
        results=collection.find({}) 
        for preguntas in results:
            self.bancoPreguntas.append(preguntas)



    def rondas (self,jugador):
        preguntasDeNivel=[]
        selector=0
        for preguntas in self.bancoPreguntas:
            if(preguntas["categoria"] ==jugador.categoria):
                preguntasDeNivel.append(preguntas)          
                selector += 1
        selectorPregunta=random.randint(0,len(preguntasDeNivel)-1)
        seleccionJugador=int(input('''
        Pregunta # ''' + str(preguntasDeNivel[selectorPregunta]["categoria"]) + '''
''' + preguntasDeNivel[selectorPregunta]["enunciado"] + '''
1. ''' + preguntasDeNivel[selectorPregunta]["opcion1"]+ '''
2. ''' + preguntasDeNivel[selectorPregunta]["opcion2"] + '''
3. ''' + preguntasDeNivel[selectorPregunta]["opcion3"] + '''
4. ''' + preguntasDeNivel[selectorPregunta]["opcion4"] +'''
'''  ))
        if(seleccionJugador == preguntasDeNivel[selectorPregunta]["correcta"]):
            jugador.acomulado += 5000000*jugador.categoria
            print("Respuesta CORRECTA  Felicidades   Dinero ganado en esta ronda "+ str(500000*jugador.categoria) +
            " Acomulado total  : " + str(jugador.acomulado))
            jugador.categoria +=1
            self.rondas(jugador)
    







        




#for preguntas in preguntas2:
#    if(preguntas["categoria"] ==2):
#        print("hola")        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    






