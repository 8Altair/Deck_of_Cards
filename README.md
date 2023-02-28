[Deck of Cards](#Deck_of_Cards)

[Card class](##Card class)
[Constructor](###Constructor)
[Representation](###Representation)

[Deck class](##Deck class)
[Constructor](###Constructor)
[Representation](###Representation)
[Count](###Count)
[Shuffle](###Shuffle)
[Deal](###Deal)

[Unit test](##Unit test)
[Card test](###Card test)
[Deck test](###Deck test)



# Deck_of_Cards

## Card class
The Card class represents a playing card with a suit and value. The Deck class represents a deck of cards, which is essentially a list of Card objects.
The Deck class has methods for shuffling the deck, dealing cards from the top of the deck, and dealing a hand of cards.
### Constructor
The Card class has a constructor that takes two parameters: suit and value. The suit must be one of the four possible suits defined in the class, and the
value must be one of the possible values defined in the class.
### Representation
The Card class also has a repr method that returns a string representation of the card in the format "value of suit".

## Deck class
The Deck class represents a deck of playing cards (of type Card). The Deck class has methods for counting the number of cards in the deck, shuffling the
deck, dealing a single card from the top of the deck, and dealing a hand of cards.
### Constructor
The Deck class has a constructor that creates a list of 52 Card objects, one for each possible combination of suit and value.
### Representation
The Deck class also has a repr method that returns a string representation of the deck in the format "Deck of <number of cards> cards".
### Count
The Deck class has a count method that returns the number of cards in the deck. If there are no cards left in the deck, it returns 0.
### Shuffle
The shuffle method shuffles the deck of cards using the shuffle function from the random module.
### Deal
The _deal method is a private method that deals cards from the deck. It takes an optional parameter for the number of cards to deal and returns a list of
Card objects. If the number of cards to deal is not specified, it defaults to 1. If there are not enough cards in the deck to deal, it raises a ValueError.

The deal_card method is a public method that deals a single card from the top of the deck and returns the card that was dealt. If there are no cards left in
the deck, it raises a ValueError.

The deal_hand method is a public method that deals a hand of cards with the specified number of cards and returns a list of Card objects. If there are not
enough cards in the deck to deal, it raises a ValueError.

## Unit test
There are also two test classes, CardTestCase and DeckTestCase, that use the unittest module to test the functionality of the Card and Deck classes.
### Card test
The CardTestCase class tests whether a valid card can be created by passing valid suit and value parameters to the Card class constructor, whether a
ValueError is raised when an invalid suit parameter is passed to the Card class constructor, whether a ValueError is raised when an invalid value
parameter is passed to the Card class constructor, and whether the repr method of the Card class returns the expected string representation of a card.
### Deck test
The DeckTestCase class tests whether a new deck is created with 52 cards, whether the count method returns the correct number of cards in the deck,
whether a ValueError is raised when there are no cards left in the deck and the deal_card method is called, whether a ValueError is raised when there are not
enough cards left in the deck and the deal_hand method is called, whether the shuffle method shuffles the deck of cards, and whether the repr method of the
Deck class returns the expected string representation of the deck.
