def main():
    USER_PROMPT = "Enter a todo: "

    todos = []

    while True:
        todo = input(USER_PROMPT)
        todos.append(todo)
        print(todos)

if __name__ == '__main__':
    main()