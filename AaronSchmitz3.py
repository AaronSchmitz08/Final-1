from gui import *
from tkinter import *

def main():
    window = Tk()
    window.title("Final")
    window.geometry("410x180")
    window.resizable(False,False)
    Gui(window)
    window.mainloop()


if __name__ == "__main__":
    main()