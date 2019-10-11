class Team: 
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.puntos = 0

    def add_points(self, points):
        self.puntos =+ points

    def __repr__(self):
        return f"Equipo # {self.numero}: {self.nombre}, con un puntaje actual de {self.puntaje}."

class Question:
    def __init__(self, pregunta, respuesta, categoria):
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.categoria = categoria
        self.puntos = 100 

    def adivinar(self):
        pass

    def fallar(self):
        pass

    def borrar(self):
        pass