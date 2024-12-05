from tkinter import *

class Gui:
    def __init__(self, window):
        self.window = window

        self.frame_info = Frame(self.window)
        self.label_round = Label(self.frame_info, text='Round 0')
        self.label_money = Label(self.frame_info, text='$1000')

        self.label_round.pack(side='left', padx=40, pady=10)
        self.label_money.pack(side='right', padx=40, pady=10)
        self.frame_info.pack()

        self.frame_hands = Frame(self.window)
        self.label_dealer_hand = Label(self.frame_hands, text='The dealer has...')
        self.label_action = Label(self.frame_hands, text='You draw a...')
        self.label_player_hand = Label(self.frame_hands, text='You have...')

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