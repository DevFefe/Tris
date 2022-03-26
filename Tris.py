from tkinter import *
from tkinter import messagebox

count = 0
countPartita = 0


PunteggioPlayer1 = 0
PunteggioPlayer2 = 0

griglia=[["", "", ""],
         ["", "", ""],
         ["", "", ""]]

def exit_main():
    global mainWindow, count, PunteggioPlayer1, PunteggioPlayer2
    for i in range(len(griglia)):
        for j in range(len(griglia)):
            griglia[i][j] = ""
    count = 0
    PunteggioPlayer1 = 0
    PunteggioPlayer2 = 0
    msg = messagebox.askquestion(title="Chiudi Programma", message="Vuoi chiedere il programma?")
    if msg == "yes":
        mainWindow.destroy()

def destroy():
    for i in range(len(griglia)):
        for j in range(len(griglia)):
            griglia[i][j] = ""
    global mainWindow, winnerWindow, count, player1, player2, countPartita
    count = 0
    mainWindow.destroy()
    winnerWindow.destroy()
    temp = player1
    player1 = player2
    player2 = temp
    countPartita += 1
    main_window()

def insert_symbol(button, riga, colonna):
    global count, player2, player1
    if griglia[riga][colonna] == "" or griglia[riga][colonna] == "F":
        if count % 2 == 0: #Player X
            player = Label(mainWindow, text = player2 + " (O)", height=1, width=16).grid(column = 0, row = 0, columnspan=2)
            button["text"] = "X"
            griglia[riga][colonna] = "X"
        else: #Player O
            player = Label(mainWindow, text = player1 + " (X)", height=1, width=16).grid(column = 0, row = 0, columnspan=2)
            button["text"] = "O"
            griglia[riga][colonna] = "O"
        count += 1
    else:
        messagebox.showerror(message = "Casella già occupata")
    print(griglia)
    print(count)
    print(countPartita)
    winner_check();

def winner_check():
    global count, PunteggioPlayer1, PunteggioPlayer2, countPartita
    if (griglia[0][0] == griglia[0][1] == griglia[0][2] == "X") or (griglia[1][0] == griglia[1][1] == griglia[1][2] == "X") or (griglia[2][0] == griglia[2][1] == griglia[2][2] == "X") or (griglia[0][0] == griglia[1][0] == griglia[2][0] == "X") or (griglia[0][1] == griglia[1][1] == griglia[2][1] == "X") or (griglia[0][2] == griglia[1][2] == griglia[2][2] == "X") or (griglia[0][0] == griglia[1][1] == griglia[2][2] == "X") or (griglia[0][2] == griglia[1][1] == griglia[2][0] == "X"):
        winner_window(player1)
        if countPartita % 2 == 0:
            PunteggioPlayer1 += 1
        else:
            PunteggioPlayer2 += 1
    elif (griglia[0][0] == griglia[0][1] == griglia[0][2] == "0") or (griglia[1][0] == griglia[1][1] == griglia[1][2] == "O") or (griglia[2][0] == griglia[2][1] == griglia[2][2] == "O") or(griglia[0][0] == griglia[1][0] == griglia[2][0] == "O") or (griglia[0][1] == griglia[1][1] == griglia[2][1] == "O") or (griglia[0][2] == griglia[1][2] == griglia[2][2] == "O") or (griglia[0][0] == griglia[1][1] == griglia[2][2] == "O") or (griglia[0][2] == griglia[1][1] == griglia[2][0] == "O"):
        winner_window(player2)
        if countPartita % 2 == 0:
            PunteggioPlayer2 += 1
        else:
            PunteggioPlayer1 += 1

    elif count >= 9:
        winner_window("NESSUNO")
    
def winner_window(player):
    global winnerWindow
    winnerWindow = Tk()
    winnerWindow.geometry("200x70")
    winnerWindow.title("Vincitore")
    label = Label(winnerWindow, text = "Il vincitore è " + player)
    label.pack()
    quit_btn = Button(winnerWindow, text = "Procedi", command = destroy)
    quit_btn.pack()

def main_window():
    global mainWindow, player1, PunteggioPlayer1, PunteggioPlayer2, const_Player1, const_Player2

    mainWindow = Tk()
    mainWindow.title("Tris di Federico")

    player = Label(mainWindow, text=player1 + " (X)", height = 1, width = 16)
    player.grid(row = 0, column = 0, columnspan=2)

    quit_btn = Button(mainWindow, height = 1, width = 5, text = "Esci", command = exit_main)
    quit_btn.grid(row = 0, column = 2)

    btn1 = Button(mainWindow, height = 1, width= 1, font = ("Courier", 100), command = lambda: insert_symbol(btn1, 0, 0))
    btn2 = Button(mainWindow, height = 1, width = 1,font = ("Courier", 100), command = lambda: insert_symbol(btn2, 0, 1))
    btn3 = Button(mainWindow, height = 1, width = 1, font = ("Courier", 100), command = lambda: insert_symbol(btn3, 0, 2))
   
    btn4 = Button(mainWindow, height = 1, width = 1, font = ("Courier", 100), command = lambda: insert_symbol(btn4, 1, 0))
    btn5 = Button(mainWindow, height = 1, width = 1, font = ("Courier", 100), command = lambda: insert_symbol(btn5, 1, 1))
    btn6 = Button(mainWindow, height = 1, width = 1, font = ("Courier", 100), command = lambda: insert_symbol(btn6, 1, 2))

    btn7 = Button(mainWindow, height = 1, width = 1, font = ("Courier", 100), command = lambda: insert_symbol(btn7, 2, 0))
    btn8 = Button(mainWindow, height = 1, width = 1, font = ("Courier", 100), command = lambda: insert_symbol(btn8, 2, 1))
    btn9 = Button(mainWindow, height = 1, width = 1, font = ("Courier", 100), command = lambda: insert_symbol(btn9, 2, 2))

    btn1.grid(row = 2, column = 0, padx = 0, pady = 0)
    btn2.grid(row = 2, column = 1)
    btn3.grid(row = 2, column = 2)

    btn4.grid(row = 3, column = 0)
    btn5.grid(row = 3, column = 1)
    btn6.grid(row = 3, column = 2)

    btn7.grid(row = 4, column = 0)
    btn8.grid(row = 4, column = 1)
    btn9.grid(row = 4, column = 2)
    
    punteggio1 = Label(mainWindow, height = 1, width = 9, text= const_Player1 + ": " + str(PunteggioPlayer1)).grid(row = 6, column = 0)
    punteggio2 = Label(mainWindow, height = 1, width = 9, text= const_Player2 + ": " + str(PunteggioPlayer2)).grid(row = 6, column = 1)

    mainWindow.mainloop();

def select_player_names():
    global player1, player2, const_Player1, const_Player2
    player1 = nome1.get()
    player2 = nome2.get()
    const_Player1 = player1
    const_Player2 = player2

    print(player1, player2)
    playerName.destroy()
    main_window()


def player_name():
    global playerName, nome1, nome2
    playerName = Tk()

    playerName.title("Scegli i nomi")

    player1 = IntVar()
    player2 = IntVar()

    labelNome1 = Label(playerName, text = "Inserisci nome primo giocatore").grid(column = 0, row = 0)
    nome1 = Entry(playerName, textvariable = player1)
    nome1.grid(column = 1, row = 0)

    labelNome2 = Label(playerName, text = "Inserisci nome secondo giocatore").grid(column = 0, row = 1)
    nome2 = Entry(playerName, textvariable = player2)
    nome2.grid(column = 1, row = 1)

    submit = Button(playerName, text = "Ok", command = select_player_names).grid(column = 1, row = 2, sticky=E)
    
    

