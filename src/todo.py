
import os

path = os.path.dirname(os.path.realpath(__file__))
# first is doc
def todo_work(user, content):
    # save to doc

    # read from doc

    # md to html
    pass

def todo_save_to(user, content):
    name = path + "/../todo/" + user
    with open(name, 'w') as file:
        print("save to file")
        file.write(content)


def todo_read_from(user):
    name = path + "/../todo/" + user
    with open(name) as file:
        print("read from file")
        return file.read()
