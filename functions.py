import  os
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Reads a text file and return the
      list of  todos items
    """
    if not os.path.exists(filepath):
        open(filepath,"w").close()
    with open(filepath,'r') as file:
        return file.readlines()


def write_todos(todos_local,filepath=FILEPATH):
    """
    open the file and write the to-do item in the text file.
    """
    with open(filepath,'w') as file_local:
        file_local.writelines(todos_local)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())