class Hand():
    def __init__(self, cards):
        self.cards = cards

    def best_rank(self):
        ranks_with_three_of_a_kind = self._rank_with_count(3)
        if len(ranks_with_three_of_a_kind) == 1:
            return "Three of a Kind"

        ranks_with_pairs = self._rank_with_count(2)

        if len(ranks_with_pairs) == 2:
                return "Two Pair"

        if len(ranks_with_pairs) == 1:
            return "Pair"

        return "High Card"

    def _rank_with_count(self, count):
        return {
            rank : rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts