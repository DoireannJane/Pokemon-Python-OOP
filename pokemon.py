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
        self.name = name
        self.deck = deck

    def draw_hand(self):
        while (len(self.hand)) < 3:
            self.hand.append(self.deck.draw())

    def view_hand(self):
        return self.hand
    
    def play_card(self):
        card = input("which card would you like to play?")
        if card == 1:
          return self.hand[0]
        elif card == 2:
          return self.hand[1]
        elif card == 3:
          return self.hand[2]
    
    # def play_card(self, card):
    #     if card == 1:
    #         return self.hand[0]
    #     elif card == 2:
    #         return self.hand[1]
    #     elif card == 3: 
    #         return self.hand[2]
    #     else:
    #         return "Please enter a number 1-3"
    
class Game:
    def __init__(self, player1, cpu):
        self.round = 1
        self.player1 = player1
        self. cpu = cpu
        cpu_deck.shuffle
        eggbert_deck.shuffle
        
    def start(self):
        print(f"Player versus the almighty CPU")
    
    # def play_round(self):
        print(f"round {self.round}!")
        self.player1.draw_hand()
        self.cpu.draw_hand()

        # cpu_card = cpu.play_card(1)
      
    
        if player1_card['damage']> cpu_card['damage']:
            self.round += 1
            return f"Player has one this round!"
        elif player1_card['damage'] < cpu_card['damage']:
            self.round += 1
            return "CPU has one this round!"
        else: 
            self.round += 1
            return "This Round is a tie!"



eggbert_deck = Deck()
cpu_deck = Deck()
cpu_deck.new_deck(data)
eggbert_deck.new_deck(data)
cpu = Player("Computer", cpu_deck)
eggbert = Player("eggbert", eggbert_deck)

game = Game(eggbert, cpu)


# print (eggbert.hand)
# print (eggbert.rounds_won)

