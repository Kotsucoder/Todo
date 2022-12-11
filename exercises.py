def exercise1():
    name = input("Enter your name: ")
    print(name.capitalize())

def exercise2():
    name = input("Enter your name: ")
    while True:
        print(name.capitalize())

def exercise3():
    while True:
        name = input("What is your name? ")
        print(name.capitalize())

def bugfix1():
    # while True
    # print("Hello")
    #
    # Solution: Place a colon at the end of "while True" and indent the print statement.
    while True:
        print("Hello")

def bugfix2():
    # greeting = "hello"
    # print(upper(greeting))
    #
    # Solution: Run upper() as an attribute of greeting
    greeting = "hello"
    print(greeting.upper())

def bugfix3():
    # countries = []
    #
    # while True:
    #     country = input("Enter the country: ")
    #     countries.append(country)
    # print(countries)
    # 
    # Solution: Indent the print() statement.
    countries = []
    
    while True:
        country = input("Enter the country: ")
        countries.append(country)
        print(countries)

if __name__ == "__main__":
    execute = input("Choose an exercise (1-3, bug1-bug3): ")

    if execute == "1":
        exercise1()
    elif execute == "2":
        exercise2()
    elif execute == "3":
        exercise3()
    elif execute == "bug1":
        bugfix1()
    elif execute == "bug2":
        bugfix2()
    elif execute == "bug3":
        bugfix3()
    else:
        print("Not a valid exercise.")