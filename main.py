import random


def word_pick():
    word_bank = (
        "python", "variable", "string", "boolean", "integer", "syntax", "program", "looping",
        "monkey", "penguin", "elephant", "giraffe", "dolphin", "kangaroo", "cheetah", "octopus",
        "pizza", "burger", "spaghetti", "chocolate", "pancake", "sandwich", "smoothie", "avocado",
        "galaxy", "astronaut", "planet", "asteroid", "spaceship", "universe", "eclipse", "nebula"
    )
    secret_word = random.choice(word_bank)
    return secret_word


def gamemode_input():
    print(
        "Please pick a difficulty: Hard - 1 life, Normal - 3 lives, "
        "Easy - 5 lives. Type in the difficulty you wish to play on."
    )
    answer = normalized_input()

    while answer not in ("hard", "normal", "easy"):
        print("Invalid input. Please pick between: hard, normal or easy.")
        answer = normalized_input()

    return answer


def yes_no_input():
    answer = normalized_input()

    while answer not in ("y", "n"):
        print("Invalid input. Please pick between 'y' or 'n'.")
        answer = normalized_input()

    return answer


def normalized_input():
    word = input().lower().strip()
    return word


def gamemode_choice():
    gamemode = {
        "hard": {
            "round_points": 200,
            "player_lives": 1,
            "points_deduction": 0
        },
        "normal": {
            "round_points": 100,
            "player_lives": 3,
            "points_deduction": 25
        },
        "easy": {
            "round_points": 50,
            "player_lives": 5,
            "points_deduction": 10
        }
    }

    answer = gamemode_input()

    return (
        gamemode[answer]["round_points"],
        gamemode[answer]["player_lives"],
        gamemode[answer]["points_deduction"]
    )


def word_scrambled():
    secret_word = word_pick()
    scrambled_word = list(secret_word)

    while "".join(scrambled_word) == secret_word:
        random.shuffle(scrambled_word)

    return "".join(scrambled_word), secret_word


def word_guess_loop(round_points, player_lives, points_deduction):
    guessed_correctly = False
    scrambled_word, secret_word = word_scrambled()

    while player_lives != 0 and not guessed_correctly:
        print(
            f"The scrambled word is: {scrambled_word}. "
            f"You have {player_lives} lives left. Place your guess: "
        )

        player_guess = normalized_input()

        if player_guess == secret_word:
            guessed_correctly = True
            print("You won")
        else:
            print("You are wrong")
            player_lives -= 1
            round_points -= points_deduction

    return secret_word, guessed_correctly, round_points


def main_game_loop():
    games_played = 0
    games_won = 0
    games_lost = 0
    keep_playing = True
    player_points = 0

    while keep_playing:
        secret_word, guessed_correctly, round_points = word_guess_loop(
            *gamemode_choice()
        )

        games_played += 1

        if not guessed_correctly:
            print(f"Total points: {player_points}")
            print(
                f"The correct word was {secret_word}. "
                "Would you like to try again? y/n"
            )
            games_lost += 1
            try_again = yes_no_input()

        else:
            games_won += 1
            player_points += round_points
            print(
                f"Congrats, you won the game and got {round_points} points. "
                f"You now have a total of {player_points} points. "
                "Would you like to play more? y/n"
            )
            try_again = yes_no_input()

        if try_again == "n":
            win_percentage = (games_won / games_played) * 100

            print(
                f"Games played: {games_played}\n"
                f"Games won: {games_won}\n"
                f"Games lost: {games_lost}\n"
                f"Total points: {player_points}\n"
                f"Win rate: {win_percentage:.1f}%"
            )

            keep_playing = False


main_game_loop()