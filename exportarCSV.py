import csv
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://interlude:Carlos15@cluster0.smza0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["banco_preguntas"]
collection= db["preguntas"]
players=db["record_jugadores"]

class exportToCsv():
    def __init__(self):
        self.bancoPreguntas=[]
        self.bancoJugadores=[]


    def exportarPreguntasCsv(self):
         
        results=collection.find({}) 
        for preguntas in results:
            self.bancoPreguntas.append([preguntas["_id"],preguntas["categoria"],preguntas["enunciado"],preguntas["opcion1"],preguntas["opcion2"],preguntas["opcion3"],preguntas["opcion4"],preguntas["correcta"]])
            
        with open('jugadores.csv','w',newline="") as resultCSV:
            writer = csv.writer(resultCSV,delimiter=",")
            for fila in self.bancoPreguntas:
                writer.writerow(fila)

    

            



