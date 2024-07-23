class Person:
    def __init__(self, name, age, password) -> None:
        self.name = name
        self._age = age
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    # password = property(get_password, set_password)


person = Person("ram", 12, "password")

# print(person.name)
# print(person._age)
person.password = "123"
print(person.password)
