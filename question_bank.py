#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
                ('what is a predator?','eats prey'),
                ('what is a herbivore?: ','eats non meat'),
                ('what is a carnivore?: ','eats meat')
        

    ],
}

hints = {
    "Science": [('what is a predator?','hint: has something to do with what it eats'),
                ('what is a herbivore?: ','hint: a sheep is a herbivore'),
                ('what is a carnivore?: ','hint: a lion is a carnivore')

        # Pair each question with a corresponding hint.
    ],
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    g = random.randint(1,3)
    print(category['Science'][g])
    #------------------------
    

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    if player_answer==correct_answer:
        return True
    else:
        return False
    #------------------------
    
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    category['Science'].pop(question)
    #------------------------
    
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    print(hints['Science'][question])
    answer = input('enter your answer: ')
    print(answer)


    #------------------------
    
    #------------------------

#---------------------------------------

def provide_hint(hints, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    print(hints['Science'][question])
    #------------------------
    
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:                                                  
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # USE CHECK ANSWER FUNCTION BEFORE DISPLAY
    #------------------------
    answer= input('enter answer: ')
    if answer!=correct_answer:
        return correct_answer
    #------------------------

#---------------------------------------




