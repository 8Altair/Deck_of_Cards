from main import Card
import unittest as u


class CardTestCase(u.TestCase):  # This class is a TestCase subclass from the unittest module
    # This method tests whether a valid card can be created by passing valid suit and value parameters to the Card class constructor
    def test_create_valid_card(self):
        c = Card("Hearts", "A")  # Create a card with suit Hearts and value A
        self.assertEqual(c.suit, "Hearts")  # Check that the suit is Hearts and the value is A
        self.assertEqual(c.value, "A")  # Check that the value is A

    # This method tests whether a ValueError is raised when an invalid suit parameter is passed to the Card class constructor
    def test_create_invalid_suit(self):
        with self.assertRaises(ValueError):  # Use the assertRaises context manager to check if a ValueError is constructor
            Card("Junk", "A")

    # This method tests whether a ValueError is raised when an invalid value parameter is passed to the Card class constructor
    def test_create_invalid_value(self):
        # Use the assertRaises context manager to check if a ValueError is raised when an invalid value parameter is passed to the Card constructor
        with self.assertRaises(ValueError):
            Card("Hearts", "13")

    # This method tests whether the __repr__ method of the Card class returns the expected string representation of a card
    def test_repr(self):
        c = Card("Diamonds", "K")  # Create a card with suit Diamonds and value K
        self.assertEqual(repr(c), "K of Diamonds")  # Check that the string representation of the card is "K of Diamonds"


if __name__ == '__main__':
    u.main()    # Test running
