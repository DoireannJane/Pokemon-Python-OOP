import random

data =[
    {
      "name": "Bulbasaur",
      "damage": 60
    }, {
      "name": "Caterpie",
      "damage": 40
    }, {
      "name": "Charmander",
      "damage": 60
    }, {
      "name": "Clefairy",
      "damage": 50
    }, {
      "name": "Jigglypuff",
      "damage": 60
    }, {
      "name": "Mankey",
      "damage": 30
    }, {
      "name": "Meowth",
      "damage": 60
    }, {
      "name": "Nidoran - female",
      "damage": 60
    }, {
      "name": "Nidoran - male",
      "damage": 50
    }, {
      "name": "Oddish",
      "damage": 40
    }, {
      "name": "Pidgey",
      "damage": 50
    }, {
      "name": "Pikachu",
      "damage": 50
    }, {
      "name": "Poliwag",
      "damage": 50
    }, {
      "name": "Psyduck",
      "damage": 60
    }, {
      "name": "Rattata",
      "damage": 30
    }, {
      "name": "Squirtle",
      "damage": 60
    }, {
      "name": "Vulpix",
      "damage": 50
    }, {
      "name": "Weedle",
      "damage": 40
    }
  ]



class Card:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        
class Deck:
    def __init__(self):
        self.cards = []
        self.graveyard = []

    def new_deck(self, data):
        random.shuffle(data)
        for pokemon in data:
            card = Card(pokemon['name'], pokemon['damage'])
            self.cards.append(pokemon)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, deck):
        self.rounds_won = 0
        self.hand = []
        self.graveyard = []
        self.name = name
        self.deck = deck

    def draw_hand(self):
        while (len(self.hand)) < 3:
            self.hand.append(self.deck.draw())

    def discard_card(self, card):
        self.graveyard.append(card)
        self.hand.remove(card)

                        
    def view_hand(self):
        return self.hand
    
    def play_card(self):
        card = input("which card would you like to play?")
        if card == "1":
          return self.hand[0]
        elif card == "2":
          return self.hand[1]
        elif card == "3":
          return self.hand[2]
        else:
          return "Please pick a number 1-3"
    

class Game:
    def __init__(self, player1, player2):
        self.rounds_played = 0
        self.player1 = player1
        self.player2 = player2

    def start(self):
        print(f"{self.player1.name} versus the almighty CPU")
    
    # def clear_score(self):
    #   self.rounds_played = 0
    #   self.player1.rounds_won = 0
    #   self.player2.rounds_won = 0
    #   self.player1.deck.append(self.player1.graveyard)
    #   self.player2.deck.append(self.player2.graveyard)
    
    def play_round(self):
        print(f"round {self.rounds_played +1}!")
        print(f"You won {self.player1.rounds_won} and CPU won {self.player2.rounds_won} rounds") 
        self.player1.draw_hand()
        self.player2.draw_hand()
        card = input(f"Which card would you like to play?? {self.player1.hand}")
      
        if card == "1":
          
          play_card= self.player1.hand[0]
          op_card = self.player2.hand[0]
          print(f"You chose {play_card['name']} and CPU chose {op_card}")
          self.player1.discard_card(self.player1.hand[0])
          self.player2.discard_card(self.player2.hand[0])

          if play_card['damage'] > op_card['damage']:
            self.player1.rounds_won += 1 
            self.rounds_played += 1
            self.player1.draw_hand()
            self.player2.draw_hand()
            print(f"You won this round!")

          elif play_card['damage'] < op_card['damage']:
            self.player2.rounds_won += 1
            self.rounds_played += 1
            self.player1.draw_hand()
            self.player2.draw_hand()
            print(f"You Lost this round! CPU won!")
            
          else:
            self.rounds_played += 1
            self.player1.rounds_won += 1
            self.player2.rounds_won += 1
            self.player1.draw_hand()
            self.player2.draw_hand()
            print(f"This round was a tie!")
            
        elif card == "2":
          play_card= self.player1.hand[1]
          op_card = self.player2.hand[1]
          print(f"You chose {play_card['name']} and CPU chose {op_card}")
          self.player1.discard_card(self.player1.hand[1])
          self.player2.discard_card(self.player2.hand[1])

          if play_card['damage'] > op_card['damage']:
            self.player1.rounds_won += 1 
            self.rounds_played += 1
            self.player1.draw_hand()
            self.player2.draw_hand()
            print(f"You won this round!")
            
          elif play_card['damage'] < op_card['damage']:
            self.player2.rounds_won += 1
            self.rounds_played += 1
            self.player1.draw_hand()
            self.player2.draw_hand()
            print(f"You Lost this round! CPU won!")

          else:
            self.rounds_played += 1
            self.player1.rounds_won += 1
            self.player2.rounds_won += 1
            self.player1.draw_hand()
            self.player2.draw_hand()
            print(f"This round was a tie!")
          
        elif card == "3":
          play_card= self.player1.hand[2]
          op_card = self.player2.hand[2]
          print(f"You chose {play_card['name']} and CPU chose {op_card}")
          self.player1.discard_card(self.player1.hand[0])
          self.player2.discard_card(self.player2.hand[0])

          if play_card['damage'] > op_card['damage']:
            self.player1.rounds_won += 1 
            self.rounds_played += 1
            self.player1.draw_hand()
            self.player2.draw_hand()
            print(f"You won this round!")

          elif play_card['damage'] < op_card['damage']:
            self.player2.rounds_won += 1 
            self.rounds_played += 1
            self.player1.draw_hand()
            self.player2.draw_hand()
            print(f"You Lost this round! CPU won!")

          else:
            self.rounds_played += 1
            self.player1.rounds_won += 1
            self.player2.rounds_won += 1
            self.player1.draw_hand()
            self.player2.draw_hand()
            print(f"This round was a tie!")
         

        else:
          print("PLEASE PICK A NUMBER 1 -3")
          self.play_round()

    def play_rounds(self):
      print(f"{self.player1.name} versus the almighty CPU")
      while self.rounds_played <= 2:
        self.play_round()
      else:
        print(f"The Game is over! You scored: {self.player1.rounds_won} CPU scored: {self.player2.rounds_won}")
        # again = input("Would you like to play again? y or n ")
        # if again == "y":
        #   self.clear_score()
        #   self.play_round()
        # else:
        #   print("Thank you for playing!")



      

        # player2_card = self.player2.deck.draw()
        #   return(f"CPU chose {player2_card}")

        
        

        # player1_card = self.player1.play_card()
      
        # if player1_card['damage']> player2_card['damage']:
        #     self.round += 1
        #     return f"Player has one this round!"
        # elif player1_card['damage'] < player2_card['damage']:
        #     self.round += 1
        #     return "CPU has one this round!"
        # else: 
        #     self.round += 1
        #     return "This Round is a tie!"

eggbert_deck = Deck()
cpu_deck = Deck()
cpu_deck.new_deck(data)
eggbert_deck.new_deck(data)
cpu = Player("Computer", cpu_deck)
eggbert = Player("eggbert", eggbert_deck)

game = Game(eggbert, cpu)
game.play_rounds()


# print (eggbert.hand)
# print (eggbert.rounds_won)

