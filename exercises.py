def exercise1():
    message = "Hello World!"
    print(type(message))

def exercise2():
    user_message = input("Enter a message for me to echo: ")
    print(user_message)

def exercise3():
    strlist = ["Penguin", "Hamster", "Parrot", "Hedgehog"]

def bugfix1():
    # answers = ['Yes', 'No', 'Yes', 'No', 'No'
    #
    # Solution: Place end bracket on code.
    answers = ['Yes', 'No', 'Yes', 'No', 'No']

def bugfix2():
    # my_answer = input("What is your answer?")
    # answers = ['Yes', 'No', 'Yes' 'No' my_answer]
    #
    # Solution: The last three elements are not separated. Place commas between them.
    my_answer = input("What is your answer?")
    answers = ['Yes', 'No', 'Yes', 'No', my_answer]

def bugfix3():
    # my_answer = input(What is your answer?)
    # answers = ['Yes', 'No', 'Yes', 'No', my_answer]
    #
    # Solution: Place quotes around string.
    my_answer = input("What is your answer?")
    answers = ['Yes', 'No', 'Yes', 'No', my_answer]

def bugfix4():
    # my_answer = input["What is your answer?"]
    # answers = ['Yes', 'No', 'Yes', 'No', my_answer]
    #
    # Solution: Replace square brackets in input with paranthesis.
    my_answer = input("What is your answer?")
    answers = ['Yes', 'No', 'Yes', 'No', my_answer]

if __name__ == '__main__':
    choose_exercise = input("Choose which exercise to execute (1-3, bug1-bug4): ")
    if choose_exercise == '1':
        exercise1()
    elif choose_exercise == '2':
        exercise2()
    elif choose_exercise == '3':
        exercise3()
    elif choose_exercise == 'bug1':
        bugfix1()
    elif choose_exercise == 'bug3':
        bugfix3()
    elif choose_exercise == 'bug4':
        bugfix4()
    else:
        print("Not a valid exercise.")