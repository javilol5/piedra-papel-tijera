import random
from enum import IntEnum
from statistics import mode


class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Spock = 3
    Lizard = 4

    @classmethod
    def minus(cls, *actions_excluded):
        return [ action for action in GameAction if action not in actions_excluded ]


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


class Game:

    def __init__(self):
        self.game_history = []
        self.user_actions_history = []

        self.victories = {
            GameAction.Rock: GameAction.minus(GameAction.Scissors, GameAction.Lizard),
            GameAction.Paper: GameAction.minus(GameAction.Spock, GameAction.Rock),
            GameAction.Scissors: GameAction.minus(GameAction.Paper, GameAction.Lizard),
            GameAction.Spock: GameAction.minus(GameAction.Scissors, GameAction.Rock),
            GameAction.Lizard: GameAction.minus(GameAction.Spock, GameAction.Paper)
        }

    def user_actions_history_append(self, action):
        self.user_actions_history.append(action)

    def game_history_append(self, game_result):
        self.game_history.append(game_result)

    def assess_game(self, user_action, computer_action):
        game_result = None

        if user_action == computer_action:
            print(f"User and computer picked {user_action.name}. Draw game!")
            game_result = GameResult.Tie

        elif computer_action in self.victories[user_action]:
            print(f"{computer_action.name} wins {user_action.name}. You lost!")
            game_result = GameResult.Defeat

        else:
            print(f"{user_action.name} wins {computer_action.name}. You win!")
            game_result = GameResult.Victory

        return game_result


    def get_computer_action(self):

        NUMBER_RECENT_ACTIONS = 5

        # No previous user actions => random computer choice
        if not self.user_actions_history or not self.game_history:
            computer_action = self.get_random_computer_action(GameAction)
        # Alternative AI functionality
        # Choice that would beat the user's most frequent recent choice
        else:
            most_frequent_recent_computer_action = GameAction(mode(self.user_actions_history[-NUMBER_RECENT_ACTIONS:]))
            computer_action = self.get_winner_action(most_frequent_recent_computer_action)

        print(f"Computer picked {computer_action.name}.")

        return computer_action


    def get_user_action(self):
        # Scalable to more options (beyond rock, paper and scissors...)
        game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
        game_choices_str = ", ".join(game_choices)
        user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
        user_action = GameAction(user_selection)

        return user_action


    def get_random_computer_action(self, actions):
        computer_selection = random.randint(0, len(actions) - 1)
        try:
            computer_action = actions(computer_selection)
        except TypeError:
            computer_action = actions[computer_selection]

        return computer_action


    def get_winner_action(self, game_action):
        winner_actions = self.victories[game_action]
        return self.get_random_computer_action(winner_actions)


    def play_another_round(self):
        another_round = input("\nAnother round? (y/n): ")
        return another_round.lower() == 'y'


    def play(self):
        while True:
            computer_action = self.get_computer_action()
            try:
                user_action = self.get_user_action()
                self.user_actions_history_append(user_action)
            except ValueError:
                range_str = f"[0, {len(GameAction) - 1}]"
                print(f"Invalid selection. Pick a choice in range {range_str}!")
                continue

            game_result = self.assess_game(user_action, computer_action)
            self.game_history_append(game_result)

            if not self.play_another_round():
                break


if __name__ == "__main__":

    game = Game()
    game.play()
