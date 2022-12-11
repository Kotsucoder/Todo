def main():
    USER_PROMPT = "Enter a todo: "

    while True:
        todo = input(USER_PROMPT)
        print(todo)
        print("Next...")

if __name__ == '__main__':
    main()