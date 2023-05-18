import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.resizable(False, False)

        # Set the font once and use this constant wherever needed
        self.FONT = ("Arial", 16)

        # Create the entry widget to display the input and output
        self.entry = tk.Entry(self.window, width=25, borderwidth=5, font=self.FONT)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create the buttons for digits and operations
        self.create_literal_button('7', 2, 0)
        self.create_literal_button('8', 2, 1)
        self.create_literal_button('9', 2, 2)
        self.create_literal_button('4', 3, 0)
        self.create_literal_button('5', 3, 1)
        self.create_literal_button('6', 3, 2)
        self.create_literal_button('1', 4, 0)
        self.create_literal_button('2', 4, 1)
        self.create_literal_button('3', 4, 2)
        self.create_literal_button('0', 5, 1)

        #self.create_literal_button('÷', 1, 3)
        self.create_literal_button('/', 1, 3)
        self.create_literal_button('*', 2, 3)
        self.create_literal_button('-', 3, 3)
        self.create_literal_button('+', 4, 3)
        self.create_literal_button('.', 5, 2)
        #self.create_literal_button('√', 1, 0)
        #self.create_literal_button('a'u'\u02E3', 1, 1)

        #self.create_literal_button('±', 1, 3)
        self.create_equals_button('=', 5, 3)

        self.create_clear_button('C', 5, 0)

    # This function creates the buttons for the numerals and operands
    def create_literal_button(self, text, row, column):
        button = tk.Button(text=text, height=3, width=8, font = self.FONT, borderwidth=2,
                           command=lambda: self.entry.insert(tk.END, text))
        button.grid(row=row, column=column)

    # This function creates the button for the equals sign
    def create_equals_button(self, text, row, column):
        button = tk.Button(text=text, height=3, width=8, font = self.FONT, borderwidth=2,
                           command=lambda: self.calculate())
        button.grid(row=row, column=column)

    # This functions create the button the clear function
    def create_clear_button(self, text, row, column):
        button = tk.Button(text=text, height=3, width=8, font = self.FONT, borderwidth=2,
                           command=lambda: self.entry.delete(0, tk.END))
        button.grid(row=row, column=column)

    # This function is bound to the equals button using lambda functionality
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

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
