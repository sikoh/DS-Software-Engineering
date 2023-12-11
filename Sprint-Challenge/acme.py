import random

class Product:
    '''Main Class decribing all acme products'''
    def __init__(self, name, price = 10, weight = 20, flammability = 0.5, identifier = 'None'):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)
    
    def stealability(self):
        ''' calculates the price divided by the weight, and then returns a message:
            * if the ratio is less than 0.5 return "Not so stealable..."
            * if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable."
            * otherwise return "Very stealable!"'''
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio >= 0.5 and ratio < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"
    
    def explode(self):
        '''calculates the flammability times the weight, and then returns a message:
            * If the product is less than 10 return "...fizzle."
            * If it is greater or equal to 10 but less than 50 return "...boom!"
            * Otherwise return "...BABOOM!!"'''
        explosion = self.flammability * self.weight
        if explosion < 10:
            return "...fizzle."
        elif explosion >= 10 and explosion < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    '''Subclass of `Product` to specifically decribing the Boxing Glove Product'''
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"       
