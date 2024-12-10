from tkinter import *
import re

import logic
from logic import Blackjack

class Gui:
    def __init__(self, window):
        self.window = window

        self.frame_info = Frame(self.window)
        self.label_round = Label(self.frame_info, text=f'Round {logic.get_round()}')
        self.label_money = Label(self.frame_info, text=f'${logic.get_balance()}')

        self.label_round.pack(side='left', padx=40, pady=10)
        self.label_money.pack(side='right', padx=40, pady=10)
        self.frame_info.pack()

        self.frame_hands = Frame(self.window)
        self.label_dealer_hand = Label(self.frame_hands, text='') # the dealer has...
        self.label_action = Label(self.frame_hands, text='Place your bet!')
        self.label_player_hand = Label(self.frame_hands, text='') # you have...

        self.label_dealer_hand.pack(side='top', pady=2)
        self.label_action.pack(pady=2)
        self.label_player_hand.pack(side='bottom', pady=2)
        self.frame_hands.pack()

        self.frame_actions_normal = Frame(self.window)
        self.button_hit = Button(self.frame_actions_normal, text='Hit', width=12)
        self.button_stand = Button(self.frame_actions_normal, text='Stand', width=12)

        self.button_hit.pack(side='left', padx=5, pady=10)
        self.button_stand.pack(side='right', padx=5, pady=10)
        self.frame_actions_normal.pack()

        self.frame_actions_special = Frame(self.window)
        self.button_double_down = Button(self.frame_actions_special, text='Double Down', width=12)
        self.button_split = Button(self.frame_actions_special, text='Split', width=12)

        self.button_double_down.pack(side='left', padx=5)
        self.button_split.pack(side='right', padx=5)
        self.frame_actions_special.pack()

        self.frame_bet = Frame(self.window)
        self.entry_bet = Entry(self.frame_bet, width=15)
        self.button_bet = Button(self.frame_bet, text='Bet', width=12, command=self.bet)

        self.entry_bet.pack(side='left', padx=5, pady=10)
        self.button_bet.pack(side='right', padx=5, pady=10)
        self.frame_bet.pack()

        self.blackjack = Blackjack()

    def bet(self):

        bet_amount = self.entry_bet.get().strip()
        self.entry_bet.delete(0, END)

        if len(bet_amount) == 0 or re.search('[^0-9]', bet_amount):
            self.label_action.config(text='Enter a numerical bet amount', fg='red')
            return

        bet_amount = int(bet_amount)
        balance = logic.get_balance()

        print(bet_amount)
        print(balance)

        if bet_amount > balance or bet_amount <= 0:
            self.label_action.config(text='Enter a bet between 0 and your balance', fg='red')
            return

