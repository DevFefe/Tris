import Tris
from tkinter import *

main = Tk()
main.title("Games")
main.geometry("100x50")

Tris = Button(main, command = Tris.player_name, text = "Tris 3x3", width = 7, height = 2)

Tris.grid(column = 0, row = 0)

main.mainloop()

