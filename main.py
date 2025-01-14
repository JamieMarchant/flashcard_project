from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# ------------------------------------ Data -----------------------------------
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ------------------------------------ fuctionality ---------------------------


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/Words_to_learn.csv", index=False)
    new_word()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=second_img)


# ----------------------------------- Vocab radomiser -------------------------


def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=first_img)
    flip_timer = window.after(3000, func=flip_card)


# -----------------------------------UI Setup---------------------------------


window = Tk()
window.title("Flashy")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=567, width=800)
canvas.pack()
first_img = PhotoImage(file="images/card_front.png")
second_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=first_img)
card_title = canvas.create_text(400, 150, fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, fill="black", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, command=None)
right_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=new_word)
wrong_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(row=1, column=0)

new_word()

window.mainloop()
