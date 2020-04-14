# Patrick Johnson         4/13/2020 #
# SWDV 630 3W 20/SP2         Week 5 #
#####################################
# Facade Design Pattern Example
# Uses the BakedGoodFactory from the other example
# Hides the individual item creation behind bundles

import factory_example as bakedgoods

class BundleFacade:
    def __init__(self):
        self._bakery = bakedgoods.BakedGoodFactory
    
    def MakeCookieTray(self):
        tray = []
        tray.append(self._bakery.create('Cookie', 'Snickerdoodle', 'Cinnamon', 12))
        tray.append(self._bakery.create('Cookie', 'Oatmeal', 'Raisin', 12))
        tray.append(self._bakery.create('Cookie', 'Sugar', 'Lemon', 12))      
        return tray

    def MakeWeddingCombo(self):
        combo = []
        combo.append(self._bakery.create('Cake', 'Wedding', 'Chocolate', 1))
        combo.append(self._bakery.create('Cupcake', '"Mr"', 'Vanilla', 24))
        combo.append(self._bakery.create('Cupcake', '"Mrs"', 'Chocolate', 24))
        return combo

def main():
    bundles = BundleFacade()
    
    cookies = bundles.MakeCookieTray()
    for item in cookies:
        print(item)
    
    for item in bundles.MakeWeddingCombo():
        print(item)

if __name__=="__main__":
    main()