# class GrandFather:
#     house = "luxery house"

#     def __init__(self) -> None:
#         print(self.house)


# class Father(GrandFather):

#     car = "ferrari"

#     def __init__(self) -> None:
#         print(self.car)
#         print("new house")
#         super().__init__()


# class Mother:
#     jewellary = "gold necklace"


# class Son(Father, Mother):
#     console = "PS5"

#     def __init__(self) -> None:
#         print(self.console)
#         super().__init__()


# # father = Father()
# son = Son()
# # print(son.house)
# # print(son.car)
# # print(son.console)
# # print(son.jewellary)


class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.name} age({self.age}) salary({self.salary})"

    def __eq__(self, other):
        return self.salary == other.salary


ram = Person("ram", 24, 10)
shyam = Person("shyam", 24, 10)

print(ram)
