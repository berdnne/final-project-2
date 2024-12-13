import csv
import re
import random

class Card:

    def __init__(self, rank: str, suit: str):

        """
        Establishes a card object with rank and suit attributes.
        :param rank: 2 through 10, J, Q, or K
        :param suit: ♠,♦,♣,or ♥
        """

        self.rank = rank
        self.suit = suit

class Blackjack:
    def __init__(self):

        self.dealer_hand = []
        self.player_hand = []
        self.__deck = get_sorted_deck()
        self.player_bet = 0

    def bet(self, amount: str) -> None:

        """
        Stores the inputted bet and removes that amount from the player's balance.
        :param amount: The bet in whole dollars
        :return: None
        """

        bet_amount = amount.strip()

        if len(bet_amount) == 0 or re.search('[^0-9]', bet_amount):
            raise ValueError('Enter a numerical bet amount')

        bet_amount = int(bet_amount)

        if bet_amount > get_balance() or bet_amount <= 0:
            raise ValueError('Enter a bet between zero and your balance')

        self.player_bet = bet_amount

        set_balance(get_balance() - self.player_bet)

    def draw_dealer_card(self) -> None:

        """
        Removes a random card from the deck and puts it in the dealer's hand.
        :return: None
        """

        random_index = random.randrange(len(self.__deck))
        self.dealer_hand.append(self.__deck[random_index])
        self.__deck.pop(random_index)

    def draw_player_card(self) -> None:

        """
        Removes a random card from the deck and puts it in the player's hand.
        :return: None
        """

        random_index = random.randrange(len(self.__deck))
        self.player_hand.append(self.__deck[random_index])
        self.__deck.pop(random_index)


    def deal_starting_hands(self) -> None:

        """
        Removes a total of 4 random cards from the deck and puts them in the player's and dealer's hands (2 each).
        :return: None
        """

        for i in range(2):
            self.draw_dealer_card()
            self.draw_player_card()

    def reset(self) -> None:

        """
        Prepares another round by moving the player and dealer's cards back to the deck,
        resetting the player's bet, and incrementing the round number.
        :return: None
        """

        self.player_hand.clear()
        self.dealer_hand.clear()
        self.__deck = get_sorted_deck()
        self.player_bet = 0
        set_round(get_round() + 1)

    def payout(self, multiplier: int) -> int:

        """
        Adds an amount to the player's balance based on a multiplier.
        :param multiplier: The factor that will be applied to the player's bet and awarded
        :return: The computed payout
        """

        payout = multiplier * self.player_bet

        set_balance(get_balance() + payout)
        self.player_bet = 0

        return payout

def get_balance() -> int:

    """
    :return: The player's balance as specified in info.csv
    """

    with open('info.csv', 'r') as info_file:
        return int(info_file.read().split()[0])

def get_round() -> int:

    """
    :return: The current round as specified in info.csv
    """

    with open('info.csv', 'r') as info_file:
        return int(info_file.read().split()[1])

def set_balance(balance: int) -> None:

    """
    Sets the player's balance in info.csv to the amount specified.
    :param balance: Specified amount
    :return: None
    """

    round_num = get_round()

    with open('info.csv', 'w') as info_file:
        content = csv.writer(info_file)
        content.writerow([balance])
        content.writerow([round_num])

def set_round(round_num: int) -> None:

    """
    Sets the round in info.csv to the amount specified.
    :param round_num: Specified round
    :return: None
    """

    balance = get_balance()

    with open('info.csv', 'w') as info_file:
        content = csv.writer(info_file)
        content.writerow([balance])
        content.writerow([round_num])

def get_sorted_deck() -> list[Card]:

    """
    :return: A new sorted deck of 52 cards categorized by suit, then ascending rank
    """

    deck = []
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['♠','♦','♣','♥']

    for suit in suits:
        for rank in ranks:
            deck.append(Card(rank, suit))

    return deck

def get_card_value(card: Card) -> int:

    """
    :param card: The card to be evaluated
    :return: The integer value for a card based on Blackjack rules (numbered cards, face cards are 10, aces are 11)
    """

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

    """
    :param hand: List of cards
    :return: The total value of a hand. Aces' value depends on the other cards in the hand (1 or 11)
    """

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