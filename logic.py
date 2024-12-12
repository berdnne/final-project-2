import csv
import re

class Card:

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def get_rank(self) -> str:
        return self.rank

    def get_suit(self) -> str:
        return self.suit


def get_balance() -> int:

    with open('info.csv', 'r') as info_file:
        return int(info_file.read().split()[0])

def get_round() -> int:

    with open('info.csv', 'r') as info_file:
        return int(info_file.read().split()[1])

def set_balance(balance: int):

    round_num = get_round()

    with open('info.csv', 'w') as info_file:
        content = csv.writer(info_file)
        content.writerow([balance])
        content.writerow([round_num])

def set_round(round_num: int):

    balance = get_balance()

    with open('info.csv', 'w') as info_file:
        content = csv.writer(info_file)
        content.writerow([balance])
        content.writerow([round_num])

def get_sorted_deck() -> list[Card]:

    deck = []
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['S','D','C','H']

    for suit in suits:
        for rank in ranks:
            deck.append(Card(rank, suit))

    return deck

class Blackjack:
    def __init__(self):

        self.round_active = False
        self.__dealer_hand = []
        self.__player_hand = []
        self.__deck = get_sorted_deck()
        self.__bet = 0

    def bet(self, amount):

        if self.round_active:
            return

        bet_amount = amount.strip()

        if len(bet_amount) == 0 or re.search('[^0-9]', bet_amount):
            raise ValueError('Enter a numerical bet amount')

        bet_amount = int(bet_amount)

        if bet_amount > get_balance() or bet_amount <= 0:
            raise ValueError('Enter a bet between zero and your balance')

        self.__bet = bet_amount

    def start_round(self):
        self.round_active = True

