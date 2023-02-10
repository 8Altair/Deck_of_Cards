from random import shuffle as s


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
        self.cards = [Card(suit, value) for suit in Deck.possible_instances for value in Deck.possible_instances[suit]]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def _deal(self, number_of_cards=1):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")

        if self.count() > number_of_cards:
            new_deck = self.cards[-number_of_cards:]
            self.cards = self.cards[:-number_of_cards]
            return new_deck
        elif self.count() < number_of_cards:
            new_deck = self.cards
            self.cards = []
            return new_deck

    def shuffle(self):
        if self.count() == 52:
            s(self.cards)
            return self.cards
        else:
            raise ValueError("Only full decks can be shuffled.")

    def deal_card(self):
        return self._deal()[0]

    def deal_hand(self, number_of_cards):
        return self._deal(number_of_cards)


karta = Card("Hearts", "10")
print(karta)
dek = Deck()
dek.deal_hand(65)
print(dek.deal_hand(52))
