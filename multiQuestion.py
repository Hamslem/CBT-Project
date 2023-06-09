import pyttsx4
import threading, random, string
from Questions import Question
from datetime import datetime
from time import *

engine = pyttsx4.init()
engine.setProperty('rate', 150)

quiz_on = True #alias for game_on

#list of questions to ask users 
question_prompt = [
    "Where is Lamborghini made? (a) Germany\n (b) Italy\n (c) Nigeria\n\n", # question_prompt[0]
    "Who is the first man to travel to space? (a) Neil Armstrong\n (b) Yuri Gagarin\n (c) Micheal Jackson\n\n", # question_prompt[1]
    "Who is the first man to land on the moon? (a) Neil Armstrong\n (b) Yuri Gagarin\n (c) Micheal Jackson\n\n", #question_prompt[2]
    "Who is the founder of Apple Inc.? (a) Mark Zuckerberg\n (b) Steve Jobs\n (c) Sergery Brin\n",
    "What is Google Inc parent? (a) Alphabet\n (b) Sun Microsoft\n (c) Amazon\n\n",
    "Who is the founder of Globaltech\n (a) Paul Smith\n (b) G.O Asogbon\n (c) Praise Jah\n\n",
    "Who is the president of Germany?\n (a) Angela Merkel (b) Buhari Jones\n (c) Nana Addo\n\n",
    "What is the full meaning of YCMA?\n (a) Young Men Clubbing Activity\n (b) Young Church Movement Action\n (c) Young Men Christain Association\n (d) Young Men Chest Arm\n\n",
    "Which of the following is a name of a continent? (a) South America\n (b) Niger\n (c) Spain\n\n",
    "_____ is the name of a continent and a country? (a) United States\n (b) Australia\n (c) Europe\n\n"
]

# List that contains instances of Question class and question prompt and the answer
mult_question = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "a"),
    Question(question_prompt[3], "b"),
    Question(question_prompt[4], "a"),
    Question(question_prompt[5], "b"),
    Question(question_prompt[6], "a"),
    Question(question_prompt[7], "c"),
    Question(question_prompt[8], "a"),
    Question(question_prompt[9], "b")
]

# run_test takes questions as input. Note it is not the same question array as before
def run_test(questions):
    question_number = 1
    score = 0
    for each_question in questions:
        if not quiz_on:
            break
        engine.say(each_question.prompt)
        engine.runAndWait()
        answer = input(each_question.prompt)
        if answer == each_question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")
    if score == 0:
        print("\nYour Grade: F")
    elif (score >= 1) and (score <= 4):
        print("\nYour Grade: D")
    elif (score >= 5) and (score <= 6):
        print("\nYour Grade: C")
    elif (score >= 6) and (score < 8):
        print("\nYour Grade: B")
    elif (score > 8) and (score <= 9):
        print("\nYour Grade: B+")
    else:
        print("\nYour Grade: A")

# Function to end quiz
def end_quiz():
    print('Time up')
    global quiz_on
    quiz_on = False
    exit()

# pass our questions array into run_test function
trials = 3
alloted_time = 600 # 10 mins

'''
Alloted time can only be updated by test administrator.
It uses seconds by default.

'''


now = datetime.now()
current_time = now. strftime("%H:%M:%S %p")
print("You started the CBT at ", current_time, "\n\n")
print(f'You will use {alloted_time} seconds for this test\n\n')


# Ask for username
name = str(("Enter your name\n"))
while not name:
    name = str(input("Please enter your name\n"))

#Ask for branch
branch = str(input("Where is your branch?\n"))
while not branch:
    branch = str(input("Where is your branch?\n"))


# Ask for token number
token_number = ''
token_list = [random.choice(list(string.ascii_letters)) for _ in range(10)] + list(str(random.randint(1111, 9999)))
random.shuffle(token_list)
token_number = "".join(token_list)
print(f'Your test token is {token_number}')
print('\t Do not share with anyone\n')
num = input("Enter Test Token Number\n")

# To check if the user entered any value
while not num:
    trials -= 1
    print(f'You have {trials} trials left')
    if trials == 0:
        print('You cannot participate in this exam again. You exceeded maximum trials')
        exit()
    num = input("Enter Test Token Number\n")

# To check if user input is equal to the token number
while num != token_number:
    trials -= 1
    print(f'You entered the wrong token number. {trials} trials left')
    if trials == 0:
        print('You cannot participate in this exam again. You exceeded maximum trials')
        exit()
    num = input("Enter Test Token Number\n")

# Begin Timer
timer = threading.Timer(alloted_time, end_quiz)
timer.start()
start = time()


# Run Application
run_test(mult_question)
timer.cancel()
stop = time()
end = datetime.now()
end_time = end.strftime("%H:%M:%S %p")
print("\n\nYou ended the test at ", end_time)
print("You used ", stop - start, " seconds.")
