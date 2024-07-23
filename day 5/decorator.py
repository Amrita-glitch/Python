def hash(func):
    def wrapper():
        print("#@" * 10)
        func()
        print("#@" * 10)

    return wrapper


@hash
def hello():
    print("Hello")


@hash
def world():
    print("World")


# hash(hello)()

hello()

world()
