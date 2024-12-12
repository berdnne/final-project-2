from tkinter.constants import END

import logic
import time

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def bet(self, amount: str) -> None:

        if self.model.round_active:
            return

        self.view.entry_bet.delete(0, END)

        try:
            self.model.bet(amount)
        except ValueError as error:
            self.view.label_action.config(text=error, fg='red')
            return

        self.play_round()

    def play_round(self):

        self.view.label_money.config(text=f'${logic.get_balance()}')

        self.model.round_active = True
        self.model.player_active = True
        self.model.deal_starting_hands()

        self.view.show_dealer_cards(self.model.dealer_hand, True)
        self.view.show_player_cards(self.model.player_hand)
        self.view.label_action.config(text=f'${self.model.player_bet} bet', fg='black')

    def hit(self):

        if not self.model.player_active:
            return

        self.model.draw_player_card()
        self.view.show_player_cards(self.model.player_hand)

        player_hand_value = logic.get_hand_value(self.model.player_hand)

        if player_hand_value > 21:
            self.view.label_action.config(text=f'{player_hand_value}, you busted! Place your new bet!', fg='black')
            self.view.show_dealer_cards(self.model.dealer_hand, False)
            self.model.reset()

    def stand(self):

        if not self.model.player_active:
            return



        self.model.player_active = False
        self.view.label_action.config(text=f'You stand, dealer has {logic.get_hand_value(self.model.dealer_hand)}', fg='black')
        self.view.show_dealer_cards(self.model.dealer_hand, False)

        while logic.get_hand_value(self.model.dealer_hand) < 17:

            #time.sleep(1.5)
            self.model.draw_dealer_card()
            self.view.show_dealer_cards(self.model.dealer_hand, False)

        if logic.get_hand_value(self.model.dealer_hand) > 21:
            pass
