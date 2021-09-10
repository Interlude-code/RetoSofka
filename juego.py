class Juego():
    def __init__(self):
        self.jugadores=[]
        self.preguntas=[]


    def agregarJugador(self,nuevoJugador):
        self.jugadores.append(nuevoJugador)  


    def imprimirJugadores(self):
        for jugadores in self.jugadores:
            print(jugadores)

   