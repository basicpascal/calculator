from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#fff"
    root.geometry("485x550+200+200")
    root.title("Calculator")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
