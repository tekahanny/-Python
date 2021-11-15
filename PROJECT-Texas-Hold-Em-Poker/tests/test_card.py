import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "Queen" ,suit = "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card(rank = "1", suit = "Diamonds")
        self.assertEqual(card.suit, "Diamonds")

    def test_has_string_representation_with_rank_and_suit(self):
        card = Card(rank = "7", suit = "Clubs")
        self.assertEqual(str(card), "7 of Clubs")

    def test_has_techical_representation(self):
        card = Card("2", "Spades")
        self.assertEqual(repr(card), "Card('2', 'Spades')")

    def test_card_has_four_possible_suit_option(self):
        self.assertEqual(
            Card.SUIT, ("Clubs", "Hearts", "Spades", "Diamonds")
        )

    def test_card_has_thirteen_possible_rank_option(self):
        self.assertEqual(
            Card.RANK, ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
        )

    def test_card_only_allows_for_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit = "Hears")