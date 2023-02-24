from random import shuffle as s


class Card:  # Class definition for a playing card
    # These are class-level variables that define the possible suits and values for a card
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    # This is the constructor for a card object, which takes a suit and value as arguments
    def __init__(self, suit, value):
        # Check if the given suit is valid (i.e. one of the possible suits defined in the class)
        if suit in Card.suits:
            self.suit = suit
        else:
            raise ValueError("The suit is not valid.")
        # Check if the given value is valid (i.e. one of the possible values defined in the class)
        if value in Card.values:
            self.value = value
        else:
            raise ValueError("The card number is not valid.")

    # This is a special method that defines how the card object should be represented as a stri  ng
    def __repr__(self):
        # Return a string representation of the card in the format "value of suit"
        return "{} of {}".format(self.value, self.suit)


class Deck:
    # Defining a dictionary that maps each suit to the possible card values
    possible_instances = {"Hearts": Card.values,
                          "Diamonds": Card.values,
                          "Clubs": Card.values,
                          "Spades": Card.values}

    def __init__(self):
        # When a new deck is created, create a list of cards by iterating over each possible suit and value
        self.cards = (Card(suit, value) for suit in Deck.possible_instances for value in Deck.possible_instances[suit])

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


if __name__ == "__main__":
    karta = Card("Hearts", "10")
    print(karta)
    dek = Deck()
    dek.deal_hand(65)
    print(dek.deal_hand(52))
