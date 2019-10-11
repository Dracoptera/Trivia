import random
from time import sleep
from csv import reader, DictReader
from pyfiglet import figlet_format
from trivia import *

# // TODO Importar archivo con preguntas y respuestas
# // TODO  Asignar preguntas, respuesta y categorías a diccionario  //  ! Agregadas a una lista en forma de objetos
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

def timer_3():
    print("Prepárense en 3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)

def timer_60():
    while True:
        try:
            print("¡Comenzamos!")
            print("\nPresionen CTRL+C si adivinan o se rinden.")
            sleep(20)
            print("\nQuedan 40 segundos...")
            sleep(20)
            print("\nSolo 20 más...")
            sleep(10)
            print("\n10 segunditos...")
            sleep(3)
            print("\n7 segundos...")
            sleep(4)
            print("\n3...")
            sleep(1)
            print("\n2...")
            sleep(1)
            print("\n1...")
            sleep(1)
            print("\nSe terminó el tiempo.")
        except KeyboardInterrupt:
            break

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
        sleep(1)
    for e in equipos:
        print("\nPresentando los siguientes equipos:\n")
        sleep(1)
        print(figlet_format(e.nombre))
        print(murci() * 4)
    return equipos


def mostrar_categorias(preguntas):
    # print("Estas son las categorías disponibles:\n")
    # print(', '.join(categorias))
    categorias = []
    for cat in preguntas: 
        if cat["CATEGORIA"] not in categorias:
            categorias.append(cat["CATEGORIA"])
    return categorias # Devuelve categorías únicas en una lista


def crear_lista_preguntas(questions):
    lista_preguntas = []
    for q in questions:
        nueva_pregunta = Question(q["PREGUNTAS"], q["RESPUESTAS"], q["CATEGORIA"])
        lista_preguntas.append(nueva_pregunta)
    return lista_preguntas

def ronda_preguntas(teams, questions, categories):
    while len(questions) > 0: # loop infinito, borrar preguntas conforme avanza
        for t in teams:
            # código del juego
            sleep(1)
            print("Estas son las categorías disponibles:\n")
            print(', '.join(categories))
            print(f"\n{t.nombre}, elijan una categoría.\n")
            while True:
                chosen = input("Su elección: ").title().strip()
                if chosen in categories:
                    print (f"\n{t.nombre} ha elegido {chosen}. ._.)/\(._. \n")
                    break
                else: 
                    print("\n¡Elijan una categoría disponible! (=____=) \n")
            timer_3()
            lista_actual = [q for q in questions if q.categoria == chosen]
            pregunta = random.choice(lista_actual)
            print(f"\n{pregunta.pregunta}\n")
            timer_60()
        else: 
            # código de finalización, no más preguntas
            pass

    

preguntas = leer_preguntas("preguntas.csv")

print(figlet_format("Trivia 7000"))

equipos = cantidad_equipos()

categorias = mostrar_categorias(preguntas)

lista_preguntas = crear_lista_preguntas(preguntas)

ronda_preguntas(equipos, lista_preguntas, categorias)