import tkinter as tk
from tkinter import messagebox
import random

def play(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result = ""
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == 'Rock' and computer_choice == 'Scissors') or
        (player_choice == 'Paper' and computer_choice == 'Rock') or
        (player_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    messagebox.showinfo("Result", f"Your choice: {player_choice}\nComputer's choice: {computer_choice}\nResult: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Rock Paper Scissors")

    # Set the window size
    root.geometry("800x800")

    label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
    label.pack()

    # Increase button width and height
    button_width = 30
    button_height = 6

    rock_button = tk.Button(root, text="Rock", width=button_width, height=button_height, bg="pink", command=lambda: play("Rock"))
    rock_button.pack(pady=40)

    paper_button = tk.Button(root, text="Paper", width=button_width, height=button_height, bg="light blue", command=lambda: play("Paper"))
    paper_button.pack(pady=40)

    scissors_button = tk.Button(root, text="Scissors", width=button_width, height=button_height, bg="violet", command=lambda: play("Scissors"))
    scissors_button.pack(pady=40)

    quit_button = tk.Button(root, text="Quit", width=button_width, height=button_height, bg="grey", command=root.destroy)
    quit_button.pack(pady=40)

    root.mainloop()
