class Team: 
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.puntos = 0

    def add_points(self, points):
        pass

    def __repr__(self):
        return f"Equipo # {self.numero}: {self.nombre}, con un puntaje actual de {self.puntaje}."