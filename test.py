
    #     equipos.append(name) # Agrega los nombres de los equipos
    # time.sleep(1)
    # print("\nPresentando a los siguientes equipos:\n")
    # for e in equipos:
    #     time.sleep(1)
    #     print(figlet_format(e))
    #     # print(random.choices(emoticons, k=4))
    #     print(murci() * 4)
    # return equipos

    # emoticons = ["⊂(◉‿◉)つ", "(ㆆ _ ㆆ)", "☜(⌒▽⌒)☞", "•`_´•", "⤜(ⱺ ʖ̯ⱺ)⤏", "(‿|‿)", "•͡˘㇁•͡˘", "/|\ ^._.^ /|\\", "ʕ·͡ᴥ·ʔ", "ʕノ•ᴥ•ʔノ ︵ ┻━┻", "ʕっ•ᴥ•ʔっ", "0__#", "( 0 _ 0 )", "(˵ ͡° ͜ʖ ͡°˵)", "┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿", "( •͡˘ _•͡˘)ノð", "(-_-)", "( ˘ ³˘)ノ°ﾟº❍｡", "(= ФェФ=)", "( ͡° ᴥ ͡°)", "※\(^o^)/※", "╭(ʘ̆~◞౪◟~ʘ̆)╮", "ヽ༼ ຈل͜ຈ༼ ▀̿̿Ĺ̯̿̿▀̿ ̿༽Ɵ͆ل͜Ɵ͆ ༽ﾉ", "ԅ(≖‿≖ԅ)", "( ╥﹏╥) ノシ"]


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