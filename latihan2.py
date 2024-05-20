from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)

        self.create_widgets(master)
        self.layout_widgets()

    def create_widgets(self, master):
        self.total_label = Label(master, textvariable=self.total_label_text)
        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate)  # wrap the command

        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.multiplication_button = Button(master, text="x", command=lambda: self.update("multiplication"))
        self.divine_button = Button(master, text="/", command=lambda: self.update("divine"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

    def layout_widgets(self):
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.multiplication_button.grid(row=3, column=0)
        self.divine_button.grid(row=3, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        elif method == "multiplication":
            self.total *= self.entered_number
        elif method == "devine":
            self.total /= self.entered_number
        elif method == "reset":
            self.total = 0
        
        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()
