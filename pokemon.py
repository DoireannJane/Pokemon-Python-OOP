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

random.shuffle(data)

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
    def draw(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, deck):
        self.rounds_won = 0
        self.hand = []
        self.name = name
        self.deck = deck

    def draw_hand(self):
        random.shuffle(self.deck)
        while (len(self.hand)) < 3:
            self.hand.append(self.deck.draw())
        


       




eggbert_deck = Deck()
cpu_deck = Deck()
cpu_deck.new_deck(data)
eggbert_deck.new_deck(data)
cpu = Player("Computer", cpu_deck)
eggbert = Player("eggbert", eggbert_deck)



# print (eggbert.hand)
# print (eggbert.rounds_won)

