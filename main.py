def main():
    USER_PROMPT = "Enter a todo: "

    todos = []

    while True:
        todo = input(USER_PROMPT)
        print(todo.capitalize())
        todos.append(todo)

if __name__ == '__main__':
    main()