def exercise1():
    message = "Hello World!"
    print(type(message))

def exercise2():
    user_message = input("Enter a message for me to echo: ")
    print(user_message)

def exercise3():
    strlist = ["Penguin", "Hamster", "Parrot", "Hedgehog"]

if __name__ == '__main__':
    choose_exercise = input("Choose which exercise to execute (1-3): ")
    if choose_exercise == '1':
        exercise1()
    elif choose_exercise == '2':
        exercise2()
    elif choose_exercise == '3':
        exercise3()
    else:
        print("Not a valid exercise.")