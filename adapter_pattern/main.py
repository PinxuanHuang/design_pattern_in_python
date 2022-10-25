from duck import Duck, WildDuck
from turkey import Turkey, WildTurkey
from adapter import TurkeyAdapter, DuckAdapter
        
def test_duck(duck: Duck):
    duck.fly()
    duck.quack()    

def test_turkey(turkey: Turkey):
    turkey.fly()
    turkey.gobble()    

if __name__ == "__main__":
    wild_turkey = WildTurkey()
    fake_duck = TurkeyAdapter(wild_turkey)
    test_duck(fake_duck)

    wild_duck = WildDuck()
    fake_turkey = DuckAdapter(wild_duck)
    test_turkey(fake_turkey)