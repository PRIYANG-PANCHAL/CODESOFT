import tkinter as tk
from tkinter import messagebox
import random
import winsound  # for sound (Windows)

# --------- WINDOW SETUP ---------
root = tk.Tk()
root.title("🔥 Tic Tac Toe PRO")
root.geometry("350x450")
root.config(bg="#1e1e2f")
root.resizable(False, False)

board = [" "] * 9
buttons = []
difficulty = "Hard"

# --------- SOUND ---------
def click_sound():
    try:
        winsound.Beep(600, 100)
    except:
        pass

def win_sound():
    try:
        winsound.Beep(1000, 200)
    except:
        pass

# --------- GAME LOGIC ---------
def check_winner(b, player):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(b[i] == player for i in combo) for combo in win_states)

def is_full():
    return " " not in board

# --------- MINIMAX (HARD AI) ---------
def minimax(b, is_max):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if " " not in b:
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, False))
                b[i] = " "
        return best
    else:
        best = 100
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, True))
                b[i] = " "
        return best

# --------- AI MOVE ---------
def ai_move():
    if difficulty == "Easy":
        empty = [i for i in range(9) if board[i] == " "]
        move = random.choice(empty)
    else:
        best_val = -100
        move = -1
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                val = minimax(board, False)
                board[i] = " "
                if val > best_val:
                    best_val = val
                    move = i

    board[move] = "O"
    buttons[move]["text"] = "O"
    buttons[move]["fg"] = "#ff4757"
    click_sound()

# --------- CLICK ---------
def click(i):
    if board[i] != " ":
        return

    board[i] = "X"
    buttons[i]["text"] = "X"
    buttons[i]["fg"] = "#1e90ff"
    click_sound()

    if check_winner(board, "X"):
        win_sound()
        status_label.config(text="🎉 You Win!", fg="#2ed573")
        root.after(1500, reset_game)
        return

    if is_full():
        status_label.config(text="😐 Draw!", fg="white")
        root.after(1500, reset_game)
        return

    root.after(300, ai_turn)

def ai_turn():
    ai_move()

    if check_winner(board, "O"):
        win_sound()
        status_label.config(text="🤖 AI Wins!", fg="#ff6b81")
        root.after(1500, reset_game)
        return

    if is_full():
        status_label.config(text="😐 Draw!", fg="white")
        root.after(1500, reset_game)

# --------- RESET ---------
def reset_game():
    global board
    board = [" "] * 9
    for btn in buttons:
        btn.config(text=" ")
    status_label.config(text="Your Turn", fg="white")

# --------- DIFFICULTY ---------
def set_easy():
    global difficulty
    difficulty = "Easy"
    status_label.config(text="Easy Mode", fg="#ffa502")

def set_hard():
    global difficulty
    difficulty = "Hard"
    status_label.config(text="Hard Mode", fg="#ff4757")

# --------- UI ---------
title = tk.Label(root, text="Tic Tac Toe PRO", font=("Arial", 18, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=10)

status_label = tk.Label(root, text="Your Turn", font=("Arial", 12),
                        bg="#1e1e2f", fg="white")
status_label.pack()

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=15)

for i in range(9):
    btn = tk.Button(frame, text=" ", font=("Arial", 20, "bold"),
                    width=5, height=2, bg="#2f3542", fg="white",
                    activebackground="#57606f",
                    command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# Buttons
control_frame = tk.Frame(root, bg="#1e1e2f")
control_frame.pack(pady=10)

tk.Button(control_frame, text="Easy", command=set_easy,
          bg="#ffa502", width=8).grid(row=0, column=0, padx=5)

tk.Button(control_frame, text="Hard", command=set_hard,
          bg="#ff4757", width=8).grid(row=0, column=1, padx=5)

tk.Button(root, text="Restart", command=reset_game,
          bg="#2ed573", width=15).pack(pady=10)

root.mainloop()