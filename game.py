#cards
#grid size
# card options
#columsn
#locations
#methods 
    #card card instances words paired with locations
    #grid 
    #check for matches 
    #if game has been won
    #run the game 
#__main__
#create instance
#call the start game method 


from cards import Card
import random
#memory game
class Game:
    def __init__(self):
        self.size = 4
        self.card_options = ['Add', 'Boo', 'Cat', 'Dev', 'Egg', 'Far', 'Gum', 'Hut']
        self.columns = ['A', 'B', 'C','D']
        self.cards = []
        self.locations = []

        for column in self.columns:
            for num in range(1,self.size+1):
                self.locations.append(f'{column} {num}')
    def set_cards(self):
            used_locations = []
            for word in self.card_options:
                for i in range(2):
                    #sets remove duplicates 
                    available_locations = set(self.locations) - set(used_locations)
                    #convert it back to a list so we can use random() on it 
                    random_location = random.choice(list(available_locations))
                    used_locations.append(random_location)
                    card = Card(word, random_location)
                    self.cards.append(card)











if __name__ == '__main__':
    game = Game()
    for card in game.cards:
         print(card)


