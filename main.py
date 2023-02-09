from random import  shuffle as s

class Card:
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, suit, value):
        if suit in Card.suits:
            self.suit = suit
        else:
            raise ValueError("The suit is not valid.")
        if value in Card.values:
            self.value = value
        else:
            raise ValueError("The card number is not valid.")

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    possible_instances = {"Hearts": ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"),
                          "Diamonds": ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"),
                          "Clubs": ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"),
                          "Spades": ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")}

    def __init__(self):
        self.cards = [Card(suit, value) for suit in Deck.possible_instances for value in range(len(Deck.possible_instances[suit]))]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def _deal(self, number_of_cards):
        number_of_cards_in_the_deck = 0
        if self.count() > number_of_cards:
            number_of_cards_in_the_deck = self.count() - number_of_cards
        elif self.count() <= 0:
            raise ValueError("All cards have been dealt")
        new_deck = self.cards[-number_of_cards_in_the_deck:]
        self.cards = self.cards[:-number_of_cards_in_the_deck]
        return new_deck

    def shuffle(self):
        if self.count() == 52:
            s(self.cards)
            return self.cards
        else:
            raise ValueError("It is only possible to shuffle full deck.")

    def deal_card(self):

