def get_todos(filepath='todos.txt'):
    """Read a text file and return the list of todo items."""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath='todos.txt'):
    """Write the todo items list in a text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos)


print(__name__)
if __name__ == '__main__':
    print('Hello')
    print(get_todos())