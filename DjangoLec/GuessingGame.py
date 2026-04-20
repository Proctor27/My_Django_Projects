import random
#Import Random !!!!!!!!!!!!!

#The computer will think of a 3 digit number that has no repeating digits
#You will then guess a 3 digit number
#The computer will then give back clues
#Based on these clues you will guess again untill you break the code with a match!

#Possible clues are 
#Close : You've guesses a correct number but in the wrong position
#Match: You've guessed a correct number in the correct position
#Nope:You haven't guess any of the numbers correctly

#solutions
#steps

#Get Guess
def get_guess():
    return list(input("What is your guess:"))
#Generate the computer code 123
def generate_code():
    #Use List Comprehension
    digits = [str(num) for num in range(10)]

    #shuffle the digits
     #Import Random
    random.shuffle(digits)
    #Then grab the first three
    return digits[:3]
#Generate the clues
#control Flow
def generate_clues(code,user_guess):
    if user_guess==code:
        return "CODE CRACKED!"
    
    clues = []
    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    if clues == []:
        return ['Nope']
    else:
        return clues
#Logic that runs the game
print("Welcome Code Breaker!")
secret_code = generate_code()

clue_Report = []

while clue_Report != "CODE CRACKED!":
    guess = get_guess()

    clue_Report = generate_clues(guess,secret_code)
    print("here is the result of your guess: ")
    for clue in clue_Report:
        print(clue)