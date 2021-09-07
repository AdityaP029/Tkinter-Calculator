import math
from pathlib import Path
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


new_text = ""


# Key replacing
def key_replacing(*args):
    key = entry_1.get()
    new = key.replace("/", "\u00F7").replace("*", "\u00D7")
    return text_input.set(new)


# Function to get text from keyboard
def get_text(*event):
    global new_text
    txt = entry_1.get()
    new_text = txt.replace("\u00F7", "/").replace("\u00D7", "*")


# Function to display text
def click(numbers):
    entry_1.insert(END, numbers)


# Function to clear display
def clear_display():
    global new_text
    new_text = ""
    text_input.set('')


# Function for equal button
def equal_input(*event):
    global new_text
    get_text()
    try:
        evaluation = eval(new_text)
        text_input.set(evaluation)
        new_text = ""
    except SyntaxError:
        text_input.set("Syntax Error")
    except ZeroDivisionError:
        text_input.set("Math Error")
    except NameError:
        text_input.set("Computation Error")


# Function for square root
def square_root():
    global new_text
    get_text()
    try:
        sq = math.sqrt(float(new_text))
        text_input.set(sq)
        new_text = ''
    except ValueError:
        text_input.set("")


# Function for percentage
def percentage(sign):
    global new_text
    get_text()
    x = re.findall("/", new_text)
    try:
        if not x:
            text_input.set(new_text)
        else:
            operation = eval(new_text)
            per = operation * 100
            text_input.set(per)
    except SyntaxError:
        text_input.set("Invalid!")


# Function to delete
def delete():
    txt = entry_1.get()[:-1]
    entry_1.delete(0, END)
    entry_1.insert(0, txt)


window = Tk()

window.geometry("382x458")
window.configure(bg="#FFFFFF")
window.title("Calculator")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=458,
    width=382,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png")
)
text_input = StringVar()
entry_bg_1 = canvas.create_image(
    191.0,
    72.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#262626",
    highlightthickness=0,
    font="Delius 18",
    justify='right',
    textvariable=text_input,
    foreground="white"
)
entry_1.place(
    x=0.0,
    y=0.0,
    width=382.0,
    height=143.0
)

canvas.create_rectangle(
    2.842170943040401e-14,
    145.0,
    382.0,
    458.0,
    fill="#000000",
    outline="")

# Creating buttons
button_image_01 = PhotoImage(
    file=relative_to_assets("button_01.png"))
button_01 = Button(
    image=button_image_01,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(1),
    relief="flat"
)
button_01.place(
    x=2.842170943040401e-14,
    y=334.0,
    width=94.0,
    height=61.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_02.png"))
button_02 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(2),
    relief="flat"
)
button_02.place(
    x=95.99999999999997,
    y=334.0,
    width=94.0,
    height=61.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_03.png"))
button_03 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(3),
    relief="flat"
)
button_03.place(
    x=191.99999999999997,
    y=334.0,
    width=94.0,
    height=61.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_04.png"))
button_04 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(4),
    relief="flat"
)
button_04.place(
    x=2.842170943040401e-14,
    y=271.0,
    width=94.0,
    height=61.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_05.png"))
button_05 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(5),
    relief="flat"
)
button_05.place(
    x=95.99999999999997,
    y=271.0,
    width=94.0,
    height=61.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_06.png"))
button_06 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(6),
    relief="flat"
)
button_06.place(
    x=191.99999999999997,
    y=271.0,
    width=94.0,
    height=61.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_07.png"))
button_07 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(7),
    relief="flat"
)
button_07.place(
    x=2.842170943040401e-14,
    y=208.0,
    width=94.0,
    height=61.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_08.png"))
button_08 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(8),
    relief="flat"
)
button_08.place(
    x=95.99999999999997,
    y=208.0,
    width=94.0,
    height=61.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_09.png"))
button_09 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click(9),
    relief="flat"
)
button_09.place(
    x=191.99999999999997,
    y=208.0,
    width=94.0,
    height=61.0
)

button_0 = PhotoImage(
    file=relative_to_assets("button_0.png"))
button_9 = Button(
    image=button_0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click("0"),
    relief="flat"
)
button_9.place(
    x=95.99999999999997,
    y=397.0,
    width=94.0,
    height=61.0
)

button_image_positive = PhotoImage(
    file=relative_to_assets("button_Positive.png"))
button_Positive = Button(
    image=button_image_positive,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click('+'),
    relief="flat"
)
button_Positive.place(
    x=288.0,
    y=334.0,
    width=94.0,
    height=61.0
)

button_image_negative = PhotoImage(
    file=relative_to_assets("button_Negative.png"))
button_Negative = Button(
    image=button_image_negative,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click('-'),
    relief="flat"
)
button_Negative.place(
    x=288.0,
    y=271.0,
    width=94.0,
    height=61.0
)

button_image_multiply = PhotoImage(
    file=relative_to_assets("button_Multiply.png"))
button_Multiply = Button(
    image=button_image_multiply,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click('\u00D7'),
    relief="flat"
)
button_Multiply.place(
    x=288.0,
    y=208.0,
    width=94.0,
    height=61.0
)

button_image_division = PhotoImage(
    file=relative_to_assets("button_Div.png"))
button_Division = Button(
    image=button_image_division,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click('\u00F7'),
    relief="flat"
)
button_Division.place(
    x=288.0,
    y=145.0,
    width=94.0,
    height=61.0
)

button_image_equal = PhotoImage(
    file=relative_to_assets("button_equal.png"))
button_Equal = Button(
    image=button_image_equal,
    borderwidth=0,
    highlightthickness=0,
    command=equal_input,
    relief="flat"
)
button_Equal.place(
    x=288.0,
    y=397.0,
    width=94.0,
    height=61.0
)

button_image_period = PhotoImage(
    file=relative_to_assets("button_period.png"))
button_Period = Button(
    image=button_image_period,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: click('.'),
    relief="flat"
)
button_Period.place(
    x=191.99999999999997,
    y=397.0,
    width=94.0,
    height=61.0
)

button_image_per = PhotoImage(
    file=relative_to_assets("button_per.png"))
button_Percentage = Button(
    image=button_image_per,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: percentage("%"),
    relief="flat"
)
button_Percentage.place(
    x=191.99999999999997,
    y=145.0,
    width=94.0,
    height=61.0
)

button_image_sq = PhotoImage(
    file=relative_to_assets("square_root.png"))
button_square_root = Button(
    image=button_image_sq,
    borderwidth=0,
    highlightthickness=0,
    command=square_root,
    relief="flat"
)
button_square_root.place(
    x=95.99999999999997,
    y=145.0,
    width=94.0,
    height=61.0
)

button_image_ac = PhotoImage(
    file=relative_to_assets("button_ac.png"))
button_AC = Button(
    image=button_image_ac,
    borderwidth=0,
    highlightthickness=0,
    command=clear_display,
    relief="flat",
)
button_AC.place(
    x=0.0,
    y=145.0,
    width=94.0,
    height=61.0
)

button_clear = PhotoImage(
    file=relative_to_assets("clear.png"))
button_c = Button(
    image=button_clear,
    borderwidth=0,
    highlightthickness=0,
    command=delete,
    relief="flat"
)
button_c.place(
    x=2.842170943040401e-14,
    y=397.0,
    width=94.0,
    height=61.0
)
# Binding Keys
window.bind('<Return>', equal_input)
window.bind('<KP_Enter>', equal_input)
window.bind('<slash>', key_replacing)
window.bind('<KP_Divide>', key_replacing)
window.bind('<asterisk>', key_replacing)
window.bind('<KP_Multiply>', key_replacing)

window.resizable(False, False)
window.mainloop()
