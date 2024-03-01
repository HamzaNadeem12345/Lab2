# ---------------------------------------
#  Game Mechanics
#    Student A (team lead)
# ---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    # ------------------------
    # Add your code here
    # ------------------------
    print("WELCOME TO THE GAME")
    # ------------------------
    # ---------------------------------------


def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    # ------------------------
    # Add your code here
    # ------------------------
    print("Choose a quiz category:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    while True:
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= choice <= len(categories):
                chosen_category = categories[choice - 1]
                print(f"You've chosen '{chosen_category}' as the quiz category.")
                return chosen_category
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # ------------------------


# ---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    # ------------------------
    # Add your code here
    # ------------------------
    print(f"Round {round_number} - Current Score: {score}")

    # ------------------------


# ---------------------------------------

def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """

    # ------------------------
    # Add your code here
    # ------------------------
    def display_game_over(final_score):
        print("Game Over!")
        print(f"Your Final Score: {final_score}")

    # ------------------------


# ---------------------------------------

def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    # ------------------------
    # Add your code here
    # ------------------------


def choose_category(categories):
    print("Choose a quiz category:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    while True:
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= choice <= len(categories):
                chosen_category = categories[choice - 1]
                print(f"You've chosen '{chosen_category}' as the quiz category.")
                return chosen_category
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_score_and_round(score, round_number):
    print(f"Round {round_number} - Current Score: {score}")


def run_game_rounds(categories):
    total_rounds = 5
    current_score = 0

    for round_number in range(1, total_rounds + 1):
        chosen_category = choose_category(categories)

        current_score += 10
        display_score_and_round(current_score, round_number)

    print("Game Over!")
    print(f"Your Final Score: {current_score}")

    # ------------------------


# ---------------------------------------

def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    # ------------------------
    # Add your code here
    # ------------------------


    return player_answer.lower() == correct_answer.lower()


# ------------------------

# ---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    # ------------------------
    # Add your code here
    # ------------------------

    if correct:
        return score + 10
    else:
        return score

    # ------------------------


# ---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    # ------------------------
    # Add your code here
    # ------------------------

    return round_number + 1

    # ------------------------


# ---------------------------------------

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    # ------------------------
    # Add your code here
    # ------------------------
    return incorrect_answers >= 3


if check_game_over:
    print("Game Over! You've reached the maximum incorrect answers.")
else:
    print("Continue to the next question.")
    # ------------------------


# ---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    # ------------------------
    # Add your code here
    # ------------------------
    print("Game Over!")
    user_choice = input("Do you want to restart the game? (yes/no): ").lower()

    if user_choice == "yes":
        print("Restarting the game...")

    elif user_choice == "no":
        print("Exiting the game. Thank you for playing!")
        exit()
    else:
        print("Invalid choice. Please enter 'yes' to restart or 'no' to exit.")

    # ------------------------

# ---------------------------------------
