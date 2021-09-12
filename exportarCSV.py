import csv
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://interlude:Carlos15@cluster0.smza0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["banco_preguntas"]
collection= db["preguntas"]
players=db["record_jugadores"]

class exportToCsv():
    def __init__(self):
        self.bancoPreguntas=[["Id","Categoria","Enunciado","opcion1","opcion2","opcion3","opcion4","Correcta"]]
        self.bancoJugadores=[["Id","Nombre","NivelAlcanzado","PremioLogrado"]]


    def exportarPreguntasCsv(self):
         
        results=collection.find({}) 
        for preguntas in results:
            self.bancoPreguntas.append([preguntas["_id"],preguntas["categoria"],preguntas["enunciado"],preguntas["opcion1"],preguntas["opcion2"],preguntas["opcion3"],preguntas["opcion4"],preguntas["correcta"]])
            
        with open('preguntas.csv','w',newline="") as resultCSV:
            writer = csv.writer(resultCSV,delimiter=",")
            for fila in self.bancoPreguntas:
                writer.writerow(fila)
        
    def exportarJugadoresCsv(self):
        results=players.find({}) 
        for jugadores in results:
            self.bancoJugadores.append([jugadores["_id"],jugadores["nombre"],jugadores["nivelAlcanzado"],jugadores["premioLogrado"]])
            
        with open('jugadores.csv','w',newline="") as resultCSV:
            writer = csv.writer(resultCSV,delimiter=",")
            for fila in self.bancoJugadores:
                writer.writerow(fila)

    

            



