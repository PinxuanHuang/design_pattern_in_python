from duck import Duck, WildDuck
from turkey import Turkey, WildTurkey


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey) -> None:
        self.turkey = turkey
    def fly(self):
        self.turkey.fly()
    def quack(self):
        self.turkey.gobble()

class DuckAdapter(Turkey):
    def __init__(self, duck: Duck) -> None:
        self.duck = duck
    def fly(self):
        self.duck.fly()
    def gobble(self):
        self.duck.quack()

if __name__ == "__main__":
    wild_turkey = WildTurkey()
    fake_duck = TurkeyAdapter(wild_turkey)
    fake_duck.fly()
    fake_duck.quack()