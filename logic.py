class Card:

# rank constants

    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'

# suit constants

    SPADES = 'S'
    DIAMONDS = 'D'
    CLUBS = 'C'
    HEARTS = 'H'

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def get_rank(self) -> str:
        return self.rank

    def get_suit(self) -> str:
        return self.suit


def get_balance():

    with open('info.csv', 'r') as info_file:
        return int(info_file.read().split()[0])

def get_round():

    with open('info.csv', 'r') as info_file:
        return int(info_file.read().split()[1])


class Blackjack:
    def __init__(self):
        pass

