class Duck:
    def fly(self):
        raise NotImplementedError
    def quack(self):
        raise NotImplementedError

class WildDuck(Duck):
    def __init__(self) -> None:
        pass

    def fly(self):
        print("duck fly")

    def quack(self):
        print("duck quack")

if __name__ == "__main__":
    wild_duck = WildDuck()
    wild_duck.fly()
    wild_duck.quack()
