import os
from random import choice as random_choice


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


clear_screen()

print(
    """
    ¡Bienvenid@ al juego de Piedra, Papel, Tijeras, Lagarto, Spock!

    Tienes que elegir una opción y la máquina elegirá otra
    ¡¡¡Vamos a jugar al mejor de 15!!!
    """
)


OPTIONS = ("piedra", "papel", "tijeras", "lagarto", "spock")

WEAKNESSES = {
    "piedra": ("papel", "spock"),
    "papel": ("tijeras", "lagarto"),
    "tijeras": ("piedra", "spock"),
    "lagarto": ("piedra", "tijeras"),
    "spock": ("lagarto", "papel"),
}

MESSAGES = [
    ["el", "papel", "cubre la", "piedra"],
    ["las", "tijeras", "cortan el", "papel"],
    ["la", "piedra", "rompe las", "tijeras"],
    ["la", "piedra", "aplasta al", "lagarto"],
    ["el", "lagarto", "envenena a", "spock"],
    ["", "spock", "vaporiza la", "piedra"],
    ["el", "lagarto", "se come el", "papel"],
    ["", "spock", "rompe las", "tijeras"],
    ["las", "tijeras", "decapitan al", "lagarto"],
    ["el", "papel", "desaprueba a", "spock"],
]

user = ""
machine = ""
user_score = 0
machine_score = 0


def show_explanation_message(first_player_choice, second_player_choice):
    explanation_message = ""

    for message in MESSAGES:
        if first_player_choice == message[1] and second_player_choice == message[-1]:
            if second_player_choice == "spock":
                explanation_message = (
                    " ".join(message[0:-1]).lstrip().capitalize() + " Spock"
                )
            else:
                explanation_message = " ".join(message).lstrip().capitalize()
            break

    return explanation_message


def determine_defeated(user_choice, machine_choice):
    global user_score, machine_score
    clear_screen()

    print(
        f"\nElegiste: {user_choice.capitalize()} \tLa máquina eligió: {
          machine_choice.capitalize()}"
    )

    if machine_choice in WEAKNESSES[user_choice]:
        print(
            "¡PUNTO PARA LA MÁQUINA! - "
            + show_explanation_message(machine_choice, user_choice)
        )
        machine_score += 1
    elif user_choice in WEAKNESSES[machine_choice]:
        print(
            "¡PUNTO PARA TI! - " + show_explanation_message(user_choice, machine_choice)
        )
        user_score += 1
    else:
        print("\t\t¡EMPATE!")

    print(f"\nTú: {user_score} \nMáquina: {machine_score}")


while user_score < 8 and machine_score < 8:
    try:
        MENU = """
        Elige una opción:
            1. Piedra
            2. Papel
            3. Tijeras
            4. Lagarto
            5. Spock
            
        """

        user_option = int(input(MENU)) - 1
        user = OPTIONS[user_option]
        machine = random_choice(OPTIONS)

        determine_defeated(user, machine)
    except IndexError:
        print("\n\t¡OPCIÓN NO VÁLIDA!")
    except ValueError:
        print("\n\t¡DEBES INGRESAR UN NÚMERO!")


if user_score > machine_score:
    print("\n\t🎉 ¡GANASTE EL JUEGO! 🎉\n")
else:
    print("\n\t😭 ¡PERDISTE! 😭\n")
