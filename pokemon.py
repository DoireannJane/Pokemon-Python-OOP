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
        for pokemon in data:
            card = Card(pokemon['name'], pokemon['damage'])
            self.cards.append(pokemon)


eggbert_deck = Deck()

eggbert_deck.new_deck(data)

print(eggbert_deck.cards)
