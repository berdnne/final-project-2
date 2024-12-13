import csv
import re
import random

class Card:

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

class Blackjack:
    def __init__(self):

        self.round_active = False
        self.player_active = False
        self.dealer_hand = []
        self.player_hand = []
        self.__deck = get_sorted_deck()
        self.player_bet = 0

    def bet(self, amount: str) -> None:

        bet_amount = amount.strip()

        if len(bet_amount) == 0 or re.search('[^0-9]', bet_amount):
            raise ValueError('Enter a numerical bet amount')

        bet_amount = int(bet_amount)

        if bet_amount > get_balance() or bet_amount <= 0:
            raise ValueError('Enter a bet between zero and your balance')

        self.player_bet = bet_amount

        set_balance(get_balance() - self.player_bet)

    def draw_dealer_card(self) -> None:

        random_index = random.randrange(len(self.__deck))
        self.dealer_hand.append(self.__deck[random_index])
        self.__deck.pop(random_index)

    def draw_player_card(self) -> None:

        random_index = random.randrange(len(self.__deck))
        self.player_hand.append(self.__deck[random_index])
        self.__deck.pop(random_index)


    def deal_starting_hands(self) -> None:

        for i in range(2):
            self.draw_dealer_card()
            self.draw_player_card()

    def reset(self):

        self.round_active = False
        self.player_active = False
        self.player_hand.clear()
        self.dealer_hand.clear()
        self.__deck = get_sorted_deck()
        self.player_bet = 0
        set_round(get_round() + 1)

    def push_payout(self) -> int:

        payout = self.player_bet

        set_balance(get_balance() + payout)
        self.player_bet = 0

        return payout

    def normal_payout(self) -> int:

        payout = 2 * self.player_bet

        set_balance(get_balance() + payout)
        self.player_bet = 0

        return payout

    def blackjack_payout(self) -> int:

        payout = 3 * self.player_bet

        set_balance(get_balance() + payout)
        self.player_bet = 0

        return payout

def get_balance() -> int:

    with open('info.csv', 'r') as info_file:
        return int(info_file.read().split()[0])

def get_round() -> int:

    with open('info.csv', 'r') as info_file:
        return int(info_file.read().split()[1])

def set_balance(balance: int) -> None:

    round_num = get_round()

    with open('info.csv', 'w') as info_file:
        content = csv.writer(info_file)
        content.writerow([balance])
        content.writerow([round_num])

def set_round(round_num: int) -> None:

    balance = get_balance()

    with open('info.csv', 'w') as info_file:
        content = csv.writer(info_file)
        content.writerow([balance])
        content.writerow([round_num])

def get_sorted_deck() -> list[Card]:

    deck = []
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['♠','♦','♣','♥']

    for suit in suits:
        for rank in ranks:
            deck.append(Card(rank, suit))

    return deck

def get_card_value(card: Card) -> int:

    match card.rank:
        case '2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'|'10':
            return int(card.rank)
        case 'J'|'Q'|'K':
            return 10
        case 'A':
            return 11
        case _:
            raise ValueError('Invalid card rank')

def get_hand_value(hand: list[Card]) -> int:

    value = 0
    aces = 0

    for card in hand:
        value += get_card_value(card)
        if card.rank == 'A':
            aces += 1

    while value > 21 and aces > 0:
        aces -= 1
        value -= 10

    return value