import time
import random
from csv import reader, DictReader
from pyfiglet import figlet_format
from termcolor import colored
import trivia

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

# emoticons = ["⊂(◉‿◉)つ", "(ㆆ _ ㆆ)", "☜(⌒▽⌒)☞", "•`_´•", "⤜(ⱺ ʖ̯ⱺ)⤏", "(‿|‿)", "•͡˘㇁•͡˘", "/|\ ^._.^ /|\\", "ʕ·͡ᴥ·ʔ", "ʕノ•ᴥ•ʔノ ︵ ┻━┻", "ʕっ•ᴥ•ʔっ", "0__#", "( 0 _ 0 )", "(˵ ͡° ͜ʖ ͡°˵)", "┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿", "( •͡˘ _•͡˘)ノð", "(-_-)", "( ˘ ³˘)ノ°ﾟº❍｡", "(= ФェФ=)", "( ͡° ᴥ ͡°)", "※\(^o^)/※", "╭(ʘ̆~◞౪◟~ʘ̆)╮", "ヽ༼ ຈل͜ຈ༼ ▀̿̿Ĺ̯̿̿▀̿ ̿༽Ɵ͆ل͜Ɵ͆ ༽ﾉ", "ԅ(≖‿≖ԅ)", "( ╥﹏╥) ノシ"]

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
    time.sleep(1)
    print("\nBien, serán entonces...\n")
    time.sleep(1)
    print(f"{n_equipos} equipos.")
    time.sleep(1)
    equipos = [] # Lista con nombres de los equipos 
    for i in range(1, n_equipos+1):
        name = input(f"\nIngresa el nombre del equipo {i}: ")
        equipos.append(name) # Agrega los nombres de los equipos
    time.sleep(1)
    print("\nPresentando a los siguientes equipos:\n")
    for e in equipos:
        time.sleep(1)
        print(figlet_format(e))
        # print(random.choices(emoticons, k=4))
        print(murci() * 4)
    return equipos

def mostrar_categorias(preguntas):
    print("Estas son las categorías disponibles:\n")
    categorias = []
    for cat in preguntas: 
        if cat["CATEGORIA"] not in categorias:
            categorias.append(cat["CATEGORIA"])
    print(', '.join(categorias))
    return categorias

def comenzar_juego(teams, categories):
    dict(teams)
    for team in teams: 



preguntas = leer_preguntas("preguntas.csv")

print(figlet_format("Trivia 7000"))

equipos = cantidad_equipos()

categorias = mostrar_categorias(preguntas)
