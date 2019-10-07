import random
from time import sleep
from csv import reader, DictReader
from pyfiglet import figlet_format
from termcolor import colored
from trivia import *

# // TODO Importar archivo con preguntas y respuestas
# TODO  Asignar preguntas, respuesta y categorías a diccionario 
# TODO Variables de puntuación y equipos, asegurar INT de ser necesario.
# // TODO Opciones de equipos o jugadores
# TODO Crear funciones para realizar preguntas con categoría o random 
# TODO Realizar pregunta:
#     Timer
#     Pregunta correcta o incorrecta 
#     Sumar puntaje o restar
#     Opciones durante pregunta 
# TODO Crear funciones para añadir preguntas, remover preguntas (maybe)
# TODO  Mostrar mensajes de inicio 

def murci():
    return "/|\ ^._.^ /|\\"

def leer_preguntas(archivo):
    with open(archivo, "r", encoding="utf-8") as file:
        trivia_dict = DictReader(file)
        return list(trivia_dict)

def cantidad_equipos():
    while True:
        try:
            n_equipos = int(input("\n¿Cuántos equipos jugarán? "))
            break
        except ValueError:
            print("\nIngresa un número válido.\n")
    sleep(1)
    print("\nBien, serán entonces...\n")
    sleep(1)
    print(f"¡{n_equipos} equipos!")
    sleep(1)
    equipos = [] # Lista con nombres de los equipos 
    for i in range(1, n_equipos+1):
        name = input(f"\nIngresa el nombre del equipo {i}: ")
        nuevo_equipo = Team(name, i)
        equipos.append(nuevo_equipo)
        time.sleep(1)
    for e in equipos:
        print("\nPresentando los siguientes equipos:\n")
        sleep(1)
        print(figlet_format(e.nombre))
        print(murci() * 4)
    return equipos


def mostrar_categorias(preguntas):
    # print("Estas son las categorías disponibles:\n")
    categorias = []
    for cat in preguntas: 
        if cat["CATEGORIA"] not in categorias:
            categorias.append(cat["CATEGORIA"])
    return categorias # Devuelve categorías únicas en una lista

def comenzar_juego(teams, question, questions, categories):
    def mensaje_inicial():
        print("Hora de comenzar el juego.")
        sleep(1)
        print("El equipo que consiga la mayor cantidad de puntos al finalizar las preguntas, será el ganador.")
        sleep(1)
        print("Para este juego, contamos con:")
        sleep(1)
        print(f"{len(questions)} preguntas.")
        sleep(1)
        print(f"{len(categories)} categorías, que son las siguientes:")
        print(', '.join(categories))


preguntas = leer_preguntas("preguntas.csv")

print(figlet_format("Trivia 7000"))

equipos = cantidad_equipos()

categorias = mostrar_categorias(preguntas)