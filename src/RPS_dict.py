import random
from enum import IntEnum


class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2
    Lagarto = 3
    Spock = 4


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Paper: GameAction.Rock,
    GameAction.Paper: GameAction.Spock,
    GameAction.Scissors: GameAction.Paper, 
    GameAction.Scissors: GameAction.Lagarto,
    GameAction.Rock: GameAction.Scissors,
    GameAction.Rock: GameAction.Lagarto,
    GameAction.Lagarto: GameAction.Spock,
    GameAction.Lagarto: GameAction.Paper,
    GameAction.Spock: GameAction.Scissors,
    GameAction.Spock: GameAction.Rock
}



def assess_game(user_action, computer_action):

    game_result = None


    print(f"Tú elegiste: {user_action}")
    print(f"La máquina eligió: {computer_action}")

    if user_action not in GameAction:
        print(f"Elección no válida. Por favor, elige entre {', '.join(GameAction)}.")
    elif user_action == computer_action:
        print("¡Es un empate!")
        game_result = GameResult.Tie
    elif Victories[user_action] == computer_action:
        print("¡Ganaste!")
        game_result = GameResult.Victory
    else:
        print("Perdiste, mejor suerte la próxima vez.")
        game_result = GameResult.Defeat

    return game_result


def get_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)
    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():

    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action()
        assess_game(user_action, computer_action)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()
