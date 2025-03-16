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
import zipapp
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
               self.locations.append(f'{column}{num}') #f-string
    def set_cards(self):
        used_locations = []
        for word in self.card_options:
            for i in range(2):
                available_locations = set(self.locations) - set(used_locations)
                random_location = random.choice(list(available_locations))
                used_locations.append(random_location)
                card = Card(word, random_location)
                self.cards.append(card)


    def create_row(self, num):
        row = [] #append cards if they've been guessed or empty spaces
        for column in self.columns:
            for card in self.cards:
                if card.location == f'{column}{num}':
                    if card.matched:
                        row.append(str(card))
                    else:
                        row.append('   ') #append 3 empty spcaes if wrong
        return row

    def create_grid(self):
        # /  A  /  B  /  C  /  D  /
        header = ' |  '+ '  |  '.join(self.columns) + '  |'
        print(header)
        for row in range(1,self.size + 1):
            print_row = f'{row}| '
            get_row = self.create_row(row)
            print_row+=' | '.join(get_row)+' |'
            print(print_row)

            

    def check_match(self,loc1,loc2):
        cards = []
        for card in self.cards:
            if card.location == loc1 or card.location == loc2:
                cards.append(card)
        if cards[0] == cards[1]:
            cards[0].matched = True
            cards[1].matched = True 
            return True
        else:
            for card in cards:
                print(f'{card.location}: {card}')
                return False      

          
         
     
        

if __name__== "__main__":
    mygame = Game()
    mygame.set_cards()

    mygame.cards[0].matched = True
    mygame.cards[1].matched = True
    mygame.cards[2].matched = True
    mygame.cards[8].matched = True
    mygame.create_grid()
    #print(mygame.create_row(1))
    #print(mygame.create_row(2))
    #print(mygame.create_row(3))
    #print(mygame.create_row(4))
    

    
