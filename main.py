
import pandas,random
from tkinter import *

try:
    df=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df=pandas.read_csv("data/french_words.csv")
finally:
    to_learn=df.to_dict(orient="records")

current_card={}
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- Unknown Button Mechanism ------------------------------- #

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    flip_timer=window.after(3000,func=flip_card)
    canvas.itemconfig(card_background,image=card_front_img)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card.get("French"),fill="black")

# ---------------------------- known Button Mechanism ------------------------------- #

def is_known():
    to_learn.remove(current_card)
    df2=pandas.DataFrame(to_learn)
    df2.to_csv("data/words_to_learn.csv",index=False)
    next_card()

# ---------------------------- Flip Mechanism ------------------------------- #
    
def flip_card():
    canvas.itemconfig(card_background,image=card_back_img)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card.get("English"),fill="white")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)

# Images

image2 = PhotoImage(file="images/wrong.png")
image3 = PhotoImage(file="images/right.png")
card_back_img=PhotoImage(file="images/card_back.png")
card_front_img=PhotoImage(file="images/card_front.png")

# Canvas

canvas=Canvas(width=800,height=526)
card_background=canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

card_word=canvas.create_text(400,263,font=("Ariel",60,"bold"))
card_title=canvas.create_text(400,150,font=("Ariel",40,"italic"))

# Buttons

unknown_button = Button(image=image2, highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

known_button = Button(image=image3, highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()