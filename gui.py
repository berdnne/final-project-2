from tkinter import *

from logic import get_round, get_balance, Card
from controller import Controller

class Gui:

    def __init__(self, window):

        """
        Creates GUI elements.
        :param window: The window that the elements are housed in
        """

        self.window = window

        self.frame_info = Frame(self.window)
        self.label_round = Label(self.frame_info, text=f'Round {get_round()}')
        self.label_money = Label(self.frame_info, text=f'${get_balance()}')

        self.label_round.pack(side='left', padx=40, pady=10)
        self.label_money.pack(side='right', padx=40, pady=10)
        self.frame_info.pack()

        self.frame_hands = Frame(self.window)
        self.label_dealer_hand = Label(self.frame_hands)
        self.label_action = Label(self.frame_hands, text='Place your bet!')
        self.label_player_hand = Label(self.frame_hands)

        self.label_dealer_hand.pack(side='top', pady=2)
        self.label_action.pack(pady=2)
        self.label_player_hand.pack(side='bottom', pady=2)
        self.frame_hands.pack()

        self.frame_actions_normal = Frame(self.window)
        self.button_hit = Button(self.frame_actions_normal, text='Hit', width=12, command=self.hit, state='disabled')
        self.button_stand = Button(self.frame_actions_normal, text='Stand', width=12, command=self.stand, state='disabled')

        self.button_hit.pack(side='left', padx=5, pady=10)
        self.button_stand.pack(side='right', padx=5, pady=10)
        self.frame_actions_normal.pack()

        self.frame_bet = Frame(self.window)
        self.entry_bet = Entry(self.frame_bet, width=15)
        self.button_bet = Button(self.frame_bet, text='Bet', width=12, command=self.bet)

        self.entry_bet.pack(side='left', padx=5)
        self.button_bet.pack(side='right', padx=5)
        self.frame_bet.pack()

        self.controller = None

    def set_controller(self, controller: Controller) -> None:

        """
        Establishes a connection back to a controller as per MVC structure.
        :param controller: Connected controller
        :return: None
        """

        self.controller = controller

    def bet(self) -> None:

        """
        Points to the controller's bet method. Retrieves the entry in the text box next to the bet button.
        :return: None
        """

        if self.controller:
            self.controller.bet(self.entry_bet.get())

    def hit(self) -> None:

        """
        Points to the controller's hit method.
        :return: None
        """

        if self.controller:
            self.controller.hit()

    def stand(self) -> None:

        """
        Points to the controller's dealer_turn method
        :return: None
        """

        if self.controller:
            self.controller.dealer_turn()

    def toggle_actions(self) -> None:

        """
        Toggles the hit and stand buttons on or off depending on their state.
        :return: None
        """

        if self.button_hit['state'] == 'normal':
            self.button_hit.config(state='disabled')
            self.button_stand.config(state='disabled')
        else:
            self.button_hit.config(state='normal')
            self.button_stand.config(state='normal')

    def toggle_betting(self) -> None:

        """
        Toggles the bet entry and buttons on or off depending on their state.
        :return: None
        """

        if self.entry_bet['state'] == 'normal':
            self.entry_bet.config(state='disabled')
            self.button_bet.config(state='disabled')
        else:
            self.entry_bet.config(state='normal')
            self.button_bet.config(state='normal')

    def show_dealer_cards(self, cards: list[Card], hide_first: bool) -> None:

        """
        Shows the dealer's cards to the player.
        :param cards: Dealer's hand
        :param hide_first: Conceals the dealer's first card from the player. Used before dealer's turn
        :return: None
        """

        hand_info = 'Dealer\'s hand: '

        for i in range(len(cards)):

            if i == 0 and hide_first:
                hand_info += '?'
            else:
                hand_info += f'{cards[i].rank}{cards[i].suit}'

            if i != len(cards) - 1:
                hand_info += ', '

        self.label_dealer_hand.config(text=hand_info)

    def show_player_cards(self, cards: list[Card]) -> None:

        """
        Shows the player's cards.
        :param cards: Player's hand
        :return: None
        """

        hand_info = 'Your hand: '

        for i in range(len(cards)):

            hand_info += f'{cards[i].rank}{cards[i].suit}'

            if i != len(cards) - 1:
                hand_info += ', '

        self.label_player_hand.config(text=hand_info)
