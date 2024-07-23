# def greetings(name):
#     print(f"hello {name}!! k gardai chau!!!")


# greetings("ram")
# greetings("shyam")
# greetings("hari")
# bin


def person(**kwargs):
    print(kwargs)
    print(
        f"""
        hello my name is {kwargs['name']} and mero age chai {kwargs['age']}
        and i am {kwargs['gender']}
        """
    )


person(name="ram", age=23, gender="male")
person(name="shyam", age=23, gender="male")
