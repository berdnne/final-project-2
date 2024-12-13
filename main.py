from gui import *
from logic import Blackjack

def main():

    window = Tk()
    window.title('Blackjack')
    window.geometry('240x208')
    window.resizable(False, False)

    view = Gui(window)
    controller = Controller(Blackjack(), view)
    view.set_controller(controller)

    window.mainloop()

if __name__ == '__main__':
    main()