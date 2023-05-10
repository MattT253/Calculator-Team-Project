import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")

        self.entry = tk.Entry(self.window, width=25, font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4)
       

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
