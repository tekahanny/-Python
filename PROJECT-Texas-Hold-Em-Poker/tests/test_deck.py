import unittest
from poker.card import Card
from poker.deck import Deck

class TestDeck(unittest.TestCase):
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(deck.cards, [])

    def test_adds_cards_to_its_collection(self):
        card = Card(rank = "Ace", suit = "Hearts")
        deck = Deck()
        deck.add_cards([card])
        self.assertEqual(deck.cards, [card])

