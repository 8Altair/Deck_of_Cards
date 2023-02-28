from main import Card
from main import Deck
import unittest as u


class DeckTestCase(u.TestCase):  # Defining a test case class that inherits from the unittest.TestCase class
    def setUp(self):  # Defining a setup method that is called before every test
        self.deck = Deck()  # Create a Deck instance

    def tearDown(self):  # Defining a teardown method that is called after every test
        del self.deck  # Delete a Deck instance

    def test_init(self):  # Defining a test case for the __init__ method of the Deck class
        self.assertTrue(isinstance(self.deck.cards, list))  # Asserting that the cards attribute is a list
        self.assertEqual(len(self.deck.cards), 52)  # Asserting that the length of the cards list is 52

    def test_count(self):  # Defining a test case for the count method of the Deck class
        self.assertEqual(self.deck.count(), 52)  # Asserting that the count method returns 52 for a newly created deck
        self.deck.cards.pop()  # Removing a card from the deck
        self.assertEqual(self.deck.count(), 51)  # Asserting that the count method returns 51
        for i in range(51):  # Removing all the cards from the deck
            self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 0)  # Asserting that the count method returns 0

    def test_repr(self):  # Defining a test case for the __repr__ method of the Deck class
        self.assertEqual(repr(self.deck),
                         "Deck of 52 cards")  # Asserting that the __repr__ method returns the expected string

    def test_deal_card(self):  # Defining a test case for the deal_card method of the Deck class
        card = self.deck.cards[-1]  # Getting the last card of the deck
        self.assertIsInstance(card, Card)  # Asserting that the last card of the deck is an instance of the Card class
        self.assertEqual(card,
                         self.deck.deal_card())  # Asserting that the deal_card method returns the last card of the deck
        self.assertEqual(self.deck.count(), 51)  # Asserting that the count of the deck has decreased by 1

    def test_shuffle(self):  # Defining a test case for the shuffle method of the Deck class
        cards = self.deck.cards.copy()  # Copying the cards list of the deck
        self.deck.shuffle()  # Shuffling the deck
        self.assertIsInstance(self.deck, Deck)  # Asserting that the deck is an instance of the Deck class
        self.assertEqual(self.deck.count(), 52)  # Asserting that the count of the deck is 52
        self.assertNotEqual(self.deck, cards)  # Asserting that the shuffled deck is not the same as the original deck

    def test_shuffle_incomplete_deck(self):  # Defining a test case for the shuffle method of the Deck class with an incomplete deck
        self.deck._deal(10)  # Removing 10 cards from the deck
        with self.assertRaises(ValueError):  # Asserting that shuffling an incomplete deck raises a ValueError
            self.deck.shuffle()  # Try to shuffle the remaining cards in the deck

    def test_deal_hand(self):  # Defining a test case for the deal_hand method of the Deck class
        hand = self.deck.deal_hand(5)  # Dealing a hand of 5 cards from the deck
        self.assertIsInstance(hand, list)  # Asserting that the hand is a list
        self.assertEqual(len(hand), 5)  # Asserting that the length of the hand is 5
        self.assertEqual(self.deck.count(), 47)  # Asserting that the number of cards of the hand is 47

    def test_deal_entire_deck(self):  # Test that deal_hand method returns all remaining cards and removes them from the deck
        hand = self.deck.deal_hand(52)  # Deal a hand of 52 cards, which should exhaust the deck
        self.assertIsInstance(hand, list)  # Ensure that the dealt hand is of type list
        self.assertEqual(len(hand), 52)  # Ensure that the hand has a length of 52, i.e., it is indeed the entire deck
        self.assertEqual(self.deck.count(), 0)  # Ensure that the count of cards in the deck is now zero

    def test_deal_more_than_deck(self):  # Test that deal_hand method raises an error if more cards are requested than are in the deck
        self.deck.deal_hand(52)  # Deal a hand (entire deck)
        with self.assertRaises(ValueError):  # Ensure that a ValueError is raised, as this operation is not possible
            self.deck.deal_hand(
                1)  # Attempt to deal a card after dealing a hand of 53 cards, which is more than the deck contains


if __name__ == '__main__':
    u.main()  # Test running
