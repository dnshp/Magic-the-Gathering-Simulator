import json
from random import shuffle
DELIMITER = ';'

class Card:
    def __init__(self, name, cost, types, typeline, text, power, toughness):
        self.name = name
        self.cost = cost
        self.types = types
        self.typeline = typeline
        self.text = text
        self.power = power
        self.toughness = toughness

    def read(self):
        if "Land" in self.types:
            print(self.name)
        else:
            print(self.name + " (" + self.cost + ")")
        print(self.typeline)
        print(self.text)
        if "Creature" in self.types:
            print(self.power + " / " + self.toughness)
        print()

    def copy(self):
        return Card(self.name, self.cost, self.types, self.typeline, self.text, self.power, self.toughness)

class Hand:
    def __init__(self):
        self.cards = []

    def add_to_hand(self, card):
        self.cards.append(card)
        print("Drew " + self.cards[-1].name)

    def read(self):
        for card in self.cards:
            card.read()

    def list(self):
        for i in range(len(self.cards)):
            print(str(i + 1) + ". " + self.cards[i].name)

    def remove_from_hand(self, index):
        rv = self.cards[index]
        self.cards = self.cards[:index] + self.cards[index + 1:]
        return rv

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card, quantity):
        for i in range(quantity):
            self.cards.append(card.copy())

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        rv = self.cards[0]
        self.cards = self.cards[1:]
        return rv

    def view(self):
        for i in range(len(self.cards)):
            print(str(i+1) + ". " + self.cards[i].name)

    def remove_from_deck(self, index):
        rv = self.cards[index]
        self.cards = self.cards[:index] + self.cards[index + 1:]
        return rv

class Board:
    def __init__(self):
        self.nonlands = []
        self.lands = []
        self.nstates = []
        self.lstates = []

    def view(self):
        print("NONLAND PERMANENTS")
        for i in range(len(self.nonlands)):
            print(str(i + 1) + ". " + self.nonlands[i].name + " (" + ("tapped" if self.nstates[i] else "untapped") + ")")
        print()
        print("LANDS")
        for i in range(len(self.lands)):
            print(str(i + 1) + ". " + self.lands[i].name + " (" + ("tapped" if self.lstates[i] else "untapped") + ")")

    def add_card(self, card, state):
        if "Land" in card.types:
            self.lands.append(card)
            self.lstates.append(state)
        else:
            self.nonlands.append(card)
            self.nstates.append(state)

    def remove_land(self, index):
        rv = self.lands[index]
        self.lands = self.lands[:index] + self.lands[index + 1:]
        return rv

    def remove_nonland(self, index):
        rv = self.nonlands[index]
        self.nonlands = self.nonlands[:index] + self.nonlands[index + 1:]
        return rv

    def untap_all(self):
        for i in range(len(self.lstates)):
            self.lstates[i] = 0
        for i in range(len(self.nstates)):
            self.nstates[i] = 0

class Player:
    def __init__(self, deck):
        self.deck = deck
        self.hand = Hand()
        self.board = Board()
        self.graveyard = Graveyard()
        self.life = 20

    def draw(self, quantity):
        for i in range(quantity):
            self.hand.add_to_hand(self.deck.draw())

    def mulligan(self):
        hand_size = len(self.hand.cards)
        for i in range(hand_size):
            self.deck.add_card(self.hand.cards[0], 1)
            self.hand.cards = self.hand.cards[1:]
        self.draw(hand_size - 1)

    def display_life(self):
        print(self.life)

    def set_life(self, new_life):
        self.life = new_life
        print("Life total set to " + str(self.life) + ".")

    def change_life(self, change):
        self.life += change
        print("Life total changed to " + str(self.life) + ".")

class Graveyard:
    def __init__(self):
        self.cards = []

    def add_to_graveyard(self, card):
        self.cards.append(card)

    def view(self):
        for i in range(len(self.cards)):
            print(str(i+1) + ". " + self.cards[i].name)

def import_cards():
    file = open("AllCards.json", 'r')
    data = json.load(file)
    cards = []
    s = {"Enchantment"}
    for card in data:
        current = data[card]

        if current["layout"] != "token":
            types = current["types"][:]
            if "power" in current:
                power = current["power"]
                toughness = current["toughness"]
            else:
                power = "0"
                toughness = "0"

            if "manaCost" not in current:
                manaCost = "0"
            else:
                manaCost = current["manaCost"][1:-1]

            if "text" in current:
                text = current["text"]
            else:
                text = ""

            cards.append(Card(current["name"], manaCost, types, current["type"], text, power, toughness))
    file.close()
    return cards

def find_card(cards, name):
    for card in cards:
        if card.name == name:
            return card
    return None

def initialize():
    all_cards = import_cards()
    shahar_jeskai_control = Deck()
    shahar_jeskai_control.add_card(find_card(all_cards, "Restoration Angel"), 2)
    shahar_jeskai_control.add_card(find_card(all_cards, "Snapcaster Mage"), 4)
    shahar_jeskai_control.add_card(find_card(all_cards, "Vendilion Clique"), 2)
    shahar_jeskai_control.add_card(find_card(all_cards, "Ajani Vengeant"), 1)
    shahar_jeskai_control.add_card(find_card(all_cards, "Cryptic Command"), 3)
    shahar_jeskai_control.add_card(find_card(all_cards, "Electrolyze"), 3)
    shahar_jeskai_control.add_card(find_card(all_cards, "Lightning Bolt"), 4)
    shahar_jeskai_control.add_card(find_card(all_cards, "Lightning Helix"), 2)
    shahar_jeskai_control.add_card(find_card(all_cards, "Mana Leak"), 3)
    shahar_jeskai_control.add_card(find_card(all_cards, "Path to Exile"), 3)
    shahar_jeskai_control.add_card(find_card(all_cards, "Shadow of Doubt"), 2)
    shahar_jeskai_control.add_card(find_card(all_cards, "Spell Snare"), 2)
    shahar_jeskai_control.add_card(find_card(all_cards, "Sphinx's Revelation"), 2)
    shahar_jeskai_control.add_card(find_card(all_cards, "Think Twice"), 1)
    shahar_jeskai_control.add_card(find_card(all_cards, "Arid Mesa"), 3)
    shahar_jeskai_control.add_card(find_card(all_cards, "Celestial Colonnade"), 4)
    shahar_jeskai_control.add_card(find_card(all_cards, "Glacial Fortress"), 1)
    shahar_jeskai_control.add_card(find_card(all_cards, "Hallowed Fountain"), 2)
    shahar_jeskai_control.add_card(find_card(all_cards, "Island"), 2)
    shahar_jeskai_control.add_card(find_card(all_cards, "Mountain"), 1)
    shahar_jeskai_control.add_card(find_card(all_cards, "Plains"), 1)
    shahar_jeskai_control.add_card(find_card(all_cards, "Sacred Foundry"), 1)
    shahar_jeskai_control.add_card(find_card(all_cards, "Scalding Tarn"), 4)
    shahar_jeskai_control.add_card(find_card(all_cards, "Steam Vents"), 2)
    shahar_jeskai_control.add_card(find_card(all_cards, "Sulfur Falls"), 2)
    shahar_jeskai_control.add_card(find_card(all_cards, "Tectonic Edge"), 3)
    shahar_jeskai_control.shuffle()
    return Player(shahar_jeskai_control)
