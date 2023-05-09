import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the entry widget to display the input and output
        self.entry = tk.Entry(master, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create the buttons for digits and operations
        self.create_button('1', 1, 0)
        self.create_button('2', 1, 1)
        self.create_button('3', 1, 2)
        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('7', 3, 0)
        self.create_button('8', 3, 1)
        self.create_button('9', 3, 2)
        self.create_button('0', 4, 1)

        self.create_button('+', 1, 3)
        self.create_button('-', 2, 3)
        self.create_button('*', 3, 3)
        self.create_button('/', 4, 3)
        self.create_button('=', 4, 2)
        self.create_button('C', 4, 0)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, padx=30, pady=20,
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column)

    def button_click(self, text):
        if text == 'C':
            self.entry.delete(0, tk.END)
        elif text == '=':
            self.calculate()
        else:
            self.entry.insert(tk.END, text)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except ZeroDivisionError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error: Division by zero")
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error: Invalid input")

root = tk.Tk()
calculator_app = CalculatorApp(root)
root.mainloop()