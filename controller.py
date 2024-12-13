from tkinter.constants import END, DISABLED

import logic

class Controller:
    def __init__(self, model, view):

        """
        Establishes a model and view as per MVC structure.
        :param model: Blackjack class
        :param view: Gui class
        """

        self.model = model
        self.view = view

    def bet(self, amount: str) -> None:

        """
        Stores bet, alerts the user of any errors, and begins a round.
        :param amount: Bet amount
        :return: None
        """

        self.view.entry_bet.delete(0, END)

        try:
            self.model.bet(amount)
        except ValueError as error:
            self.view.label_action.config(text=error, fg='red')
            return

        self.play_round()

    def play_round(self) -> None:

        """
        Deals a hand to the dealer and player, disables betting buttons, and shows hands.
        :return: None
        """

        self.view.label_money.config(text=f'${logic.get_balance()}')

        self.model.deal_starting_hands()

        self.view.toggle_actions()
        self.view.toggle_betting()

        self.view.show_dealer_cards(self.model.dealer_hand, True)
        self.view.show_player_cards(self.model.player_hand)
        self.view.label_action.config(text=f'${self.model.player_bet} bet', fg='black')

    def hit(self) -> None:

        """
        Draws one card to the players hand. Player busts if their hand value is over 21.
        :return: None
        """

        self.model.draw_player_card()
        self.view.show_player_cards(self.model.player_hand)

        dealer_value = logic.get_hand_value(self.model.dealer_hand)
        player_value = logic.get_hand_value(self.model.player_hand)

        if player_value > 21:

            self.view.show_dealer_cards(self.model.dealer_hand, False)

            self.model.reset()

            self.view.label_action.config(text=f'You: {player_value}, Dealer: {dealer_value}, Bust!', fg='black')
            self.view.label_money.config(text=f'${logic.get_balance()}')
            self.view.label_round.config(text=f'Round {logic.get_round()}')

            self.view.toggle_actions()
            self.view.toggle_betting()

    def dealer_turn(self) -> None:

        """
        The dealer hits until their hand value is above 17, or until they bust.
        Disables player action buttons. Pays the player accordingly
        :return: None
        """

        self.view.toggle_actions()
        self.view.show_dealer_cards(self.model.dealer_hand, False)

        while logic.get_hand_value(self.model.dealer_hand) < 17:
            self.model.draw_dealer_card()

        self.view.show_dealer_cards(self.model.dealer_hand, False)

        dealer_value = logic.get_hand_value(self.model.dealer_hand)
        player_value = logic.get_hand_value(self.model.player_hand)

        round_info = f'You: {player_value}, Dealer: {dealer_value}, '

        if dealer_value == player_value:

            payout = self.model.payout(1)
            round_info += f'Push! ${payout} returned.'

        elif player_value == 21:

            payout = self.model.payout(3)
            round_info += f'Blackjack! You win ${payout}!'

        elif dealer_value > 21:

            payout = self.model.payout(2)
            round_info += f'Dealer busts! You win ${payout}!'

        elif player_value > dealer_value:

            payout = self.model.payout(2)
            round_info += f'You win ${payout}!'

        else:

            self.model.player_bet = 0
            round_info += 'Dealer wins!'

        self.model.reset()

        self.view.label_action.config(text=round_info, fg='black')
        self.view.label_money.config(text=f'${logic.get_balance()}')
        self.view.label_round.config(text=f'Round {logic.get_round()}')

        self.view.toggle_betting()
