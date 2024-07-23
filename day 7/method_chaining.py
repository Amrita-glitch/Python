class Burger:

    def bun(self):
        print("Bun ")
        return self

    def patty(self):
        print("patty ")
        return self

    def tomato(self):
        print("tomato ")
        return self

    def sauce(self):
        print("sauce ")
        return self


burger = Burger()


burger.bun().patty().tomato().sauce().bun()
