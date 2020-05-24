try:
    with open("hello_world.txt", "w") as f:
        f.write("hello world\n")
except:
    print("ERROR: Whilte writing to hello_world file")
finally:
    print("Always workk")


class EmptyListError(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"EmptyListError"


def db_list():
    return [1]


try:
    list_db = db_list()
    if not len(list_db):
        raise EmptyListError(
            {"message": "DB list is empty"})
    print("DB list not empty exception not raised")
except EmptyListError as e:
    details = ""
    for arg in e.args:
        for key, value in arg.items():
            details += f"{key}: {value}\n"
    print(details)
