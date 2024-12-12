from tkinter.constants import END

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def bet(self, amount: str) -> None:

        self.view.entry_bet.delete(0, END)

        try:
            self.model.bet(amount)
        except ValueError as error:
            self.view.label_action.config(text=error, fg='red')

