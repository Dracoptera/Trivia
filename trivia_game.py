import random
from collections import defaultdict
from time import sleep
from csv import reader, DictReader
from pyfiglet import figlet_format
from trivia import *

# // TODO Importar archivo con preguntas y respuestas
# // TODO  Asignar preguntas, respuesta y categorías a diccionario  //  ! Agregadas a una lista en forma de objetos
# TODO Variables de puntuación y equipos, asegurar INT de ser necesario.
# // TODO Opciones de equipos o jugadores
# // TODO Crear funciones para realizar preguntas con categoría o random // ! Solo con categoría
# TODO Realizar pregunta:
#     Timer
#     Pregunta correcta o incorrecta 
#     Sumar puntaje o restar
#     Opciones durante pregunta 
# TODO Crear funciones para añadir preguntas, remover preguntas (maybe)
# TODO  Mostrar mensajes de inicio 

def theme():
    # Busca un buen Ascii para añadir en https://www.asciiart.eu/
    print("""
    .___,_______,___Halloween edition.
| ./(       )\.        |             |
| )  \/\_/\/  (        |             |
| `)  (^Y^)  (`      \(|)/           |
|  `),-(~)-,(`      --(")--          |
|      '"'      \\    /`\            |
|          .-'```^```'-.    ,     ,  |
|         /   (\ __ /)  \   )\___/(  |
|         |    ` \/ `   |  {(@)v(@)} |
|         \    \____/   /   {|~~~|}  |
|          `'-.......-'`    {/^^^\}  |
.___ldb______________________`m-m`___.
""")

def murci():
    """Un adorable murciélago para decorar."""
    return "/|\ ^._.^ /|\\"

def timer_3():
    """Timer simple de 3 segundos."""
    print("Prepárense en 3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)

def timer_60():
    """Timer de 60 segundos para cada pregunta. Interrumpirlo con CTRL + C"""
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
            break
        except KeyboardInterrupt:
            break

def adivinaron():
    """Función para confirmar si el equipo adivinó la respuesta"""
    print("\n¿Adivinaron?")
    response = ''
    while response.lower() not in {"s", "n"}:
        response = input('Solo ingresa "s" o "n": ')
    return response

def leer_preguntas(archivo):
    """Función para leer archivo CSV"""
    with open(archivo, "r", encoding="utf-8") as file:
        trivia_dict = DictReader(file)
        return list(trivia_dict)


def cantidad_equipos():
    """Función para crear equipos y presentarlos"""
    while True:
        try:
            n_equipos = int(input("\n¿Cuántos equipos jugarán? "))
            break
        except ValueError:
            print("\nIngresa un número válido.\n")
    sleep(1)
    print("\nBien, serán entonces...\n")
    sleep(1)
    print(f"¡{n_equipos} equipos! \(^-^)/")
    sleep(1)
    equipos = [] # Lista con nombres de los equipos 
    for i in range(1, n_equipos+1):
        name = input(f"\nIngresa el nombre del equipo {i}: ")
        nuevo_equipo = Team(name, i)
        equipos.append(nuevo_equipo)
        sleep(1)
    print("\nPresentando los siguientes equipos:\n")
    for e in equipos:
        sleep(1)
        print(figlet_format(e.nombre))
        print(murci() * 4)
    return equipos


def mostrar_categorias(preguntas):
    """Función para contar las categorías disponibles"""
    categorias = defaultdict(int)
    for cat in preguntas:
        categorias[cat['CATEGORIA']] += 1
    return categorias


def crear_lista_preguntas(questions):
    """Función para ordenar preguntas en una lista"""
    lista_preguntas = []
    for q in questions:
        nueva_pregunta = Question(q["PREGUNTAS"], q["RESPUESTAS"], q["CATEGORIA"])
        lista_preguntas.append(nueva_pregunta)
    return lista_preguntas

def ronda_preguntas(teams, questions, q_archive):
    """Función del juego"""
    categories = mostrar_categorias(q_archive)
    while len(questions) > 0: # loop infinito, borrar preguntas conforme avanza
        for t in teams:
            # código del juego
            sleep(1)
            print(f"\nEs el turno de: {t}\n")
            print("Estas son las categorías disponibles:\n")
            print(murci())
            for cat, num in categories.items():
                print(f"\n{cat} (preguntas: {num})")
            print(murci())
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
            # pregunta = random.choice(lista_actual)
            pregunta = lista_actual[0]
            print(f"\n{pregunta.pregunta}\n")
            timer_60()
            print(f"\nLa respuesta correcta es: {pregunta.respuesta}")
            guess = adivinaron()
            if guess == "s":
                t.add_points(pregunta.puntos)
                print(f"\n¡Bien ahí, {t.nombre}! Ganaron {pregunta.puntos} puntos. =^_^=")
            elif guess == "n": 
                print("\nSuerte para la próxima. @^@")
            questions.remove(pregunta)
            categories[chosen] -= 1
            if categories[chosen] == 0:
                del categories[chosen]
            if len(questions) == 0:
                break
    # código de finalización, no más preguntas
    print("Se terminaron las preguntas.")
    team_list = sorted(teams, key=lambda x: x.puntos)
    print("	[¬º-°]¬ Resultado final:\n")
    for t in team_list:
        print(f"{t.nombre}, puntos totales: {t.puntos}\n")
    print(f"*\(^o^)/* ¡Felicidades, {team_list[0].nombre}! *\(^o^)/* \n")
    print(murci() * 4)
    print(figlet_format(team_list[0].nombre))
    print(murci() * 4)
    theme()

    

preguntas = leer_preguntas("preguntas.csv")

print(figlet_format("Trivia 7000"))
theme()

equipos = cantidad_equipos()

lista_preguntas = crear_lista_preguntas(preguntas)

ronda_preguntas(equipos, lista_preguntas, preguntas)