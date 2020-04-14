# Patrick Johnson         4/13/2020 #
# SWDV 630 3W 20/SP2         Week 5 #
#####################################
# Factory Design Pattern Example

import abc

class BakedGood(metaclass=abc.ABCMeta):
    def __init__(self, name, flavor, quantity):
        self.name = name
        self.flavor = flavor
        self.quantity = quantity
        
    @abc.abstractmethod
    def get_role(self):
        pass
    
    def __str__(self):
        return "{}: {} {} flavored {}".format(self.__class__.__name__, self.quantity, self.flavor, self.name)

class Cookie(BakedGood):
    def get_role(self):
        return "Cookie"

class Cake(BakedGood):
    def get_role(self):
        return "Cake"
    
class Cupcake(BakedGood):
    def get_role(self):
        return "Cupcake"
    
class BakedGoodFactory():
    @classmethod
    def create(cls, baked_good_type, *args):        
        bgt = baked_good_type.lower().strip()
        
        if baked_good_type == "Cookie":
            return Cookie(*args)
        elif baked_good_type == "Cake":
            return Cake(*args)
        elif baked_good_type == "Cupcake":
            return Cupcake(*args)
        
        
def main():
    bakery = BakedGoodFactory()
    print(bakery.create('Cupcake','Red Velvet', 'Chocolate', 2))
    print(bakery.create('Cookie','Macaroon', 'Lemon', 6))
    print(bakery.create('Cake','Ice Cream', 'Vanilla', 1))
    
    # without instantiating the factory class:
    print(BakedGoodFactory.create('Cookie', 'Snickerdoodle', 'Cinnamon', 12))
    
if __name__=="__main__":
    main()
        
                
            