import json
from pymongo import MongoClient
import random
from pregunta import Pregunta

cluster=MongoClient("mongodb+srv://interlude:Carlos15@cluster0.smza0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["banco_preguntas"]
collection= db["preguntas"]
players=db["record_jugadores"]


class Juego():
    def __init__(self):
        self.jugadores=[]
        self.bancoPreguntas=[]
        self.seleccionJugador=''


    def imprimirPreguntas(self):
        results=collection.find({})
        for preguntas in results:
            print(preguntas["enunciado"])


    
    def agregarPregunta(self,pregunta):
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
       --------- Pregunta # ''' + str(preguntasDeNivel[selectorPregunta]["categoria"]) + '''---------
''' + preguntasDeNivel[selectorPregunta]["enunciado"] + '''
1. ''' + preguntasDeNivel[selectorPregunta]["opcion1"]+ '''
2. ''' + preguntasDeNivel[selectorPregunta]["opcion2"] + '''
3. ''' + preguntasDeNivel[selectorPregunta]["opcion3"] + '''
4. ''' + preguntasDeNivel[selectorPregunta]["opcion4"] +'''
'''  ))
        if(seleccionJugador == preguntasDeNivel[selectorPregunta]["correcta"]):
            jugador.acomulado += 500000*jugador.categoria
            print("RESPUESTA CORRECTA  FELICIDADES!!!!   Dinero ganado en esta ronda "+ str(500000*jugador.categoria) + '$'+
            " Acomulado total  : "+ str(jugador.acomulado)+ '$')
            if (jugador.categoria==5):
                print("FELICIDADES ALCANZASTE EL MAXINO NIVEL -------FIN DE LA PARTIDA -----")
                objToDic={"nombre": jugador.nombre, "nivelAlcanzado":jugador.categoria, "premioLogrado":jugador.acomulado}
                players.insert_one(objToDic)
                return
            seguir=int(input('''
            Deseas contiguar con la ronda # '''+ str(jugador.categoria) +''' o Retirar el acomulado de : ''' + str(jugador.acomulado) +'''$
            1.Seguir jugando  2.Retirarse       Recuerde que si continua y pierde perdera su acomulado5   
            ''' ))
            if (seguir == 1):
                jugador.categoria +=1
                self.rondas(jugador)
            else:
                print("-----------------------------Gracias por jugar---------------------------------------------- ")
                objToDic={"nombre": jugador.nombre, "nivelAlcanzado":jugador.categoria, "premioLogrado":jugador.acomulado}
                players.insert_one(objToDic)
        else:
            objToDic={"nombre": jugador.nombre, "nivelAlcanzado":jugador.categoria, "premioLogrado":jugador.acomulado*0}
            players.insert_one(objToDic)
            print("RESPUESTA ERRADA  ------FIN DE LA PARTIDA -------")
            return


    def recordJugadores(self):
        results=players.find({}) 
        for jugadores in results:
            print('''
Nombre: ''' + jugadores["nombre"]+'''
Premio Ganado: '''+ str(jugadores["premioLogrado"])+'''$
Nivel maximo alcanzado: '''+ str(jugadores["nivelAlcanzado"])
 )

 

    def ingresarPregunta(self):
        categoria=int(input('''
Ingresa el numero correspondiente a la categoria de la pregunta
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
            self.agregarPregunta(pregunta)
                
        else:
            print("Categoria no existente ")
            return








        



  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    






