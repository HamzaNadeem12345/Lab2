import random
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ('what is weight formula?','mass times gravity'),
        ('how do plants make food','photosynthesis'),
        

    ],
}




questions['Science'].pop(0)
print(questions)




def check_answer(player_answer=input('Enter: '),correct_answer=input('Enter: ')):
    if player_answer==correct_answer:
        return True

print(check_answer())


