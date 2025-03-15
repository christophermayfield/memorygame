#class card
#hold a card
#matched or not?
#location 
#__eq__
class Person:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height 
        
class Card:
    def __init__(self,word,location):
        self.card = word
        self.location = location
        self.matched = False
    def __eq__(self, other):
        return self.card == other.card

    def __str__(self):
        return self.card 

if __name__ == '__main__':
    card1 = Card('Egg','A1')
    card2 = Card('Egg', 'B1')
    card3 = Card('Hut', 'D4')

    print(card1 == card2)
    print(card2 == card3)
    print(card1 == card3)
    print(card1)
    print(card3)

