from gui import *

def main():
    window = Tk()
    window.title('Blackjack')
    window.geometry('240x240')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()