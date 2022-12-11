def exp1():
    while True:
        print("Hello")

def exp2():
    todos = []

    while True:
        USER_PROMPT = "Enter a todo: "
        todo = input(USER_PROMPT)
        print(todo.capitalize())
        todos.append(todo)

def exp3():
    USER_PROMPT = "Enter a todo: "
    todos = []

    while True:
        todo = input(USER_PROMPT)
        print(todo.title())
        todos.append(todo)

def exp4():
    USER_PROMPT = "Enter a todo: "
    todos = []

    while True:
        todo = input(USER_PROMPT)
        todo.title()
        todos.append(todo)

def exp5():
    USER_PROMPT = "Enter a todo: "
    todos = []

    while True:
        todo = input(USER_PROMPT)
        print(todo.title)
        todos.append(todo)

if __name__ == '__main__':
    execute = input("Choose what experiment you want to execute (1-5): ")
    if execute == "1":
        exp1()
    elif execute == "2":
        exp2()
    elif execute == "3":
        exp3()
    elif execute == "4":
        exp4()
    elif execute == "5":
        exp5()
    else:
        print("Not a valid experiment.")