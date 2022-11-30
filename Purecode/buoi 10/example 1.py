from tkinter import *


def hello(event):
    print("Singe Click, Button-1")


def my_quit(event):
    print("Double Click, so let's stop")
    import sys
    sys.exit()


widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', my_quit)
widget.mainloop()
