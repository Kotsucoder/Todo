def main():
    password = input("Enter password: ")

    while password != "pass123":
        password = input("Enter password: ")
    
    print("Password was correct.")

if __name__ == '__main__':
    main()