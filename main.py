from tkinter import *
BG_COLOR = "#2E2E2E"
BTN_COLOR = "#505050"
BTN_HOVER = "#696969"
TEXT_COLOR = "white"
DISPLAY_BG = "#1C1C1C"
HIGHLIGHT = "#FF9500"
def click(num):
    if len(label["text"]) < 12:
        label["text"] = str(num) if label["text"] == "0" else label["text"] + str(num)
def clear():
    label["text"] = "0"
def backspace():
    label["text"] = label["text"][:-1] if len(label["text"]) > 1 else "0"
def operation(op):
    global X, Op
    X, Op = float(label["text"]), op
    label["text"] = "0"
def calculate():
    global X, Op
    try:
        Y = float(label["text"])
        label["text"] = str(
            {"+": X + Y, "-": X - Y, "*": X * Y, "/": X / Y if Y else "Error", "%": X * Y / 100}.get(Op, "Error")
        )[:12]
    except:
        label["text"] = "Error"
def reciprocal():
    label["text"] = str(1 / float(label["text"]))[:12] if float(label["text"]) != 0 else "Error"
def square():
    label["text"] = str(float(label["text"]) ** 2)[:12]
def sqrt():
    try:
        value = float(label["text"])
        label["text"] = str(value ** 0.5)[:12] if value >= 0 else "Error"
    except ValueError:
        label["text"] = "Error"
def negate():
    label["text"] = str(-float(label["text"]))[:12]
def key_event(event):
    if event.char.isdigit() or event.char == ".":
        click(event.char)
    elif event.char in "+-*/":
        operation(event.char)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        backspace()
def show_info_window():
    info_window = Toplevel(root)
    info_window.title("Информация")
    info_window.geometry("300x150")
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    x = root_x + (root_width // 2) - 150
    y = root_y + (root_height // 2) - 75
    info_window.geometry(f"+{x}+{y}")
    info_window.transient(root)
    info_window.grab_set()
    Label(info_window, text="С любовью и уважением родителям:\nКириллу Валентиновичу и Маргарите Геннадиевне",
          font="Arial 10", wraplength=280).pack(pady=10)
    Label(info_window, text="О программе: Простой калькулятор\n Игорь Земсков © 2025", font="Arial 8").pack(side="bottom", pady=5)
root = Tk()
root.title("Калькулятор")
root.geometry("320x550+600+150")
root.configure(bg=BG_COLOR)
root.bind("<Key>", key_event)
label = Label(root, text="0", font=("Arial", 32), fg=TEXT_COLOR, bg=DISPLAY_BG,
              anchor="e", width=14, padx=10, pady=10)
label.pack(pady=15, padx=10, ipadx=5, ipady=5)
buttons = [
    ("←", backspace), ("C", clear), ("CE", clear), ("/", lambda: operation("/")),
    ("7", lambda: click(7)), ("8", lambda: click(8)), ("9", lambda: click(9)), ("*", lambda: operation("*")),
    ("4", lambda: click(4)), ("5", lambda: click(5)), ("6", lambda: click(6)), ("-", lambda: operation("-")),
    ("1", lambda: click(1)), ("2", lambda: click(2)), ("3", lambda: click(3)), ("+", lambda: operation("+")),
    ("±", negate), ("0", lambda: click(0)), (",", lambda: click(".")), ("=", calculate),
    ("1/x", reciprocal), ("x²", square), ("√", sqrt), ("%", lambda: operation("%"))
]
frame = Frame(root, bg=BG_COLOR)
frame.pack()
def create_button(text, cmd, color=BTN_COLOR):
    btn = Button(frame, text=text, font=("Arial", 14), width=6, height=2, fg=TEXT_COLOR, bg=color,
                 activebackground=BTN_HOVER, activeforeground="white", relief="flat",
                 command=cmd, bd=0)
    return btn
for i, (text, cmd) in enumerate(buttons):
    color = HIGHLIGHT if text in "+-*/=√x²%" else BTN_COLOR
    create_button(text, cmd, color).grid(row=i // 4, column=i % 4, padx=3, pady=3)
Button(root, text="О программе", font=("Arial", 12), command=show_info_window).pack(pady=10)
root.mainloop()