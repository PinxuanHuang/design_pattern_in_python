class Turkey:
    def fly(self):
        raise NotImplementedError
    def gobble(self):
        raise NotImplementedError

class WildTurkey(Turkey):
    def __init__(self) -> None:
        pass
    def fly(self):
        print("turkey fly")
    def gobble(self):
        print("turkey gobble")

if __name__ == "__main__":
    wild_turkey = WildTurkey()
    wild_turkey.fly()
    wild_turkey.gobble()