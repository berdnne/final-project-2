from gui import *
from controller import Controller
from logic import Blackjack

def main():

    window = Tk()
    window.title('Blackjack')
    window.geometry('240x240')
    window.resizable(False, False)
    view = Gui(window)
    controller = Controller(Blackjack(), view)
    view.set_controller(controller)
    window.mainloop()


if __name__ == '__main__':
    main()