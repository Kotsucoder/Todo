def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)



    elif user_action.startswith('show'):
        todos = get_todos()
        
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1}. {item}'
            print(row)



    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            
            write_todos(todos)
        except IndexError:
            print('Invalid Command: There is no todo with that number.')
            continue
        except ValueError:
            print('Invalid Command: Expected number for todo to edit.')
            continue



    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f'Todo {todo_to_remove} was removed from the list.'
            print(message)
        except IndexError:
            print('Invalid Command: There is no todo with that number.')
            continue
        except ValueError:
            print('Invalid Command: Expected number for todo to edit.')
            continue



    elif user_action.startswith('exit'):
        break



    else:
        print("Command is not valid")

print("Bye!")