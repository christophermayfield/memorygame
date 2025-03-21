def set_cards(self):
            used_locations = []
            for word in self.card_options:
                for i in range(2): #creates 2 cards for every work so we get 16 cards
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
                   if card.location == f'{column}{num}':
                        if card.matched:
                             row.append(str(card))
                        else:
                             row.append('   ')
         return row 


         
    def create_grid(self):
         #template
         # | A | B | C | D |
         header = ' |  ' + '  |  '.join(self.columns) + '  |'
         print(header)
         for row in range(1, self.size + 1):
              print_row = f'{row}| '
              get_row = self.create_row(row)
              print_row += ' | '.join(get_row) + ' |'
              print(print_row)


    def check_match(self, loc1,loc2):
         #empty array to hold the matches
         cards = []
         for card in self.cards:
              if card.location == loc1 or card.location == loc2:
                   cards.append(card)
              if cards[0] == cards[1]:
                   #changing the matched parameter to true if they're a match
                   cards[0].matched = True
                   cards[1].matched = True 
                   return True
              else: 
                   for card in cards:
                        print(f'{card.location}: {card}')  
                   return False
    def check_win(self):
         for card in self.cards:
              if card.matched == False:
                   return False
         return True
    def check_location(self, time):
         while True:
              guess = input(f'What is the location of your {time} card')
              if guess.upper() in self.locations:
                   return guess.upper()
              else:
                   return print("That's not a valid location. It should look like this : A1")
              
    def start_game(self):
         game_running = True
         print('Memory Game: lets go')
         self.set_cards()
         while game_running:
              self.create_grid()
              guess1 = self.check_location('first')
              guess2 = self.check_location('second')
              if self.check_match(guess1,guess2):
                   if self.check_win():
                        print('congrats, you have guessed them all!')
                        self.create_grid()
                        game_running = False
                   else:
                        input('those cards aren\'t a match try again')
              print('GAME OVER')        

                     
              
