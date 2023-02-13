from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
dict_data = {}
current_card = {}
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except:
    og_data = pandas.read_csv('data/italianWords.csv')
    dict_data = og_data.to_dict(orient="records")
else:
    dict_data = data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card['English'])
    canvas.itemconfig(card_bg, image=bg_pic_back)


def is_known():
    dict_data.remove(current_card)
    print(len(dict_data))
    data = pandas.DataFrame(dict_data)
    data.to_csv("data/words_to_learn.csv",index=False)
    update_word()


# ---------------------------- update word ------------------------------- #
def update_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_data)
    print(current_card['Italian'])
    canvas.itemconfig(card_title, text="Italian", fill='black')
    canvas.itemconfig(card_word, text=current_card['Italian'], fill='black')
    canvas.itemconfig(card_bg, image=bg_pic)
    flip_timer = window.after(3000, flip_card)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
bg_pic = PhotoImage(file="images/card_front.png")
bg_pic_back = PhotoImage(file="images/card_back.png")

card_bg = canvas.create_image(400, 263, image=bg_pic)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text='', font=("Arial", 40, "italic"))

card_word = canvas.create_text(400, 263, text='', font=("Arial", 60, "bold"))

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=update_word)
wrong_button.grid(row=1, column=0)
update_word()

window.mainloop()
