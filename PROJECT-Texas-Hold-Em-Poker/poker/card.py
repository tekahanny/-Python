class Card():
    SUIT = (
        "Clubs", "Hearts", "Spades", "Diamonds"
    )

    RANK = (
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"
    )
    def __init__(self, rank, suit):
        if rank in not self.RANK:
            


        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"