def main():
    USER_PROMPT = "Enter a todo: "
    todo1 = input(USER_PROMPT)
    todo2 = input(USER_PROMPT)
    todo3 = input(USER_PROMPT)

    todos = [todo1, todo2, todo3, "Hello"]
    print(todos)

    print(type(todo1))

if __name__ == '__main__':
    main()