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
            for num in range(1,self.size +1):
                self.locations.append(f'{column} {num}') #f-string
    def set_cards(self):
            used_locations = []
            for word in self.card_options:
                for i in range(2):
                    #grabbing 2 locations
                    #sets remove duplicates 
                    #run the following code for a context example set1 = {'a','b'} set 2 = {'a'} set1-set2
                    available_locations = set(self.locations) - set(used_locations)
                    #convert it back to a list so we can use random() on it 
                    random_location = random.choice(list(available_locations))
                    used_locations.append(random_location)
                    card = Card(word, random_location)
                    self.cards.append(card)


    def create_row(self,num):
         row = []
         for column in self.columns:
              for card in self.cards:
                   if card.location == f'{column} {num}':
                        if card.matched:
                             row.append(str(card))
                        else:
                             row.append('   ')
         return row  


         
         
    def create_grid(self):
         #template
         # | A | B | C | D |
         header = ' |  ' + '  |  '.join(self.columns) + ' |'
         print(header)
         for row in range(1, self.size + 1):
              print_row = f'{row}| '
              get_row = self.create_row(row)
              print_row+= ' | '.join(get_row) + ' |'
              print(print_row)








if __name__ == '__main__':
    game = Game()
    game.set_cards()
    game.create_grid()
    game.cards[0].matched = True
    game.cards[1].matched = True
    game.cards[2].matched = True
    game.cards[3].matched = True
    print(game.create_row(1))
    print(game.create_row(2))
    print(game.create_row(3))
    print(game.create_row(4))



   



