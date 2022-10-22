from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self) -> None:
        suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        values = ['A', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def count(self):
        return len(self.cards)

    def __repr__(self) -> str:
        return f"Deck of {len(self.cards)}"

    def _deal(self, num):
        count = self.count()
        remove_amount = min([count, num])
        if (len(self.cards) == 0):
            raise ValueError("All Cards Have Been Dealt.")
        hand = self.cards[-remove_amount:]
        self.cards = self.cards[:-remove_amount]
        return hand

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)


# Create new deck, shuffle and deal
c = Deck()
c.shuffle()
hand = c.deal_hand(51)
card = c.deal_card()

# print checks
print(hand)
print(card)
print(c.cards)

# error check
c.deal_card()
