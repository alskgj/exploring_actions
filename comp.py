import random

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"A {self.color} {self.value}"

    def __eq__(self, other):
        if self.color == other.color and self.value == other.value:
            return True
        return False

class Deck:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def draw(self):
        return random.choice(self.items)

    def all_the_same_color(self):
        if not self.items:
            return True
        if all([self.items[0].color == e.color for e in self.items]):
            return True
        return False


if __name__ == '__main__':
    deck = Deck()
    deck.add(Card("red", 2))
    deck.add(Card("red", 3))
    print(deck.all_the_same_color())
    deck.add(Card("black", 5))
    print(deck.all_the_same_color())
    print(deck.draw())
