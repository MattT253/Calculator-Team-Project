import tkinter as tk
import calc_math

class Calculator:
    def __init__(self):
        # Instantiate the CalcMath class
        self.cm = calc_math.CalcMath()

        # Create 2 storage values for a number and a operator
        self.number = 0
        self.operator = ''

        # This flag is used to clear the display when a new value is being input after an
        #   operator button or the equals button has been pressed.
        self.clear_input_on_next_numeral = False

        # Create a GUI window and set a few of its variables
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.resizable(False, False)

        # Set the font once and use this constant wherever needed
        self.FONT = ("Arial", 16)

        # Create the entry widget to display the input and output
        self.entry = tk.Entry(self.window, width=25, borderwidth=5, font=self.FONT)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create the buttons for digits
        self.create_numeral_button('7', 3, 0)
        self.create_numeral_button('8', 3, 1)
        self.create_numeral_button('9', 3, 2)
        self.create_numeral_button('4', 4, 0)
        self.create_numeral_button('5', 4, 1)
        self.create_numeral_button('6', 4, 2)
        self.create_numeral_button('1', 5, 0)
        self.create_numeral_button('2', 5, 1)
        self.create_numeral_button('3', 5, 2)
        self.create_numeral_button('0', 6, 1)

        # Create a button for the decimal point, this is functionally the same as a digit input
        self.create_numeral_button('.', 6, 2)

        # Create the buttons for the operators that take 2 numeric inputs
        self.create_two_operand_button('÷', 2, 3)
        self.create_two_operand_button('X', 3, 3)
        self.create_two_operand_button('-', 4, 3)
        self.create_two_operand_button('+', 5, 3)
        self.create_two_operand_button('a√x', 2, 1)
        self.create_two_operand_button('a'u'\u02E3', 2, 2) # Exponentiation, using Unicode superscript x

        # Create the buttons for the operators that take 1 numeric input
        self.create_single_operand_button('√', 2, 0)
        self.create_single_operand_button('±', 6, 0)
        self.create_single_operand_button('log', 3, 0)
        self.create_single_operand_button('mod', 4, 0)


        # Create the special functional buttons such as equals and clear
        self.create_equals_button('=', 6, 3)
        self.create_clear_button('C', 1, 0)

        # Bind keyboard inputs to the window
        self.window.bind('<Key>', self.handle_keypress)

    # This function creates the buttons for the numerals
    def create_numeral_button(self, text, row, column):
        button = tk.Button(text=text, height=3, width=8, font=self.FONT, borderwidth=2,
                           command=lambda: self.numeral_helper(text))
        button.grid(row=row, column=column)

    # This function creates the buttons for single operand operators such as squareroot, absolute value, or negation
    def create_single_operand_button(self, text, row, column):
        button = tk.Button(text=text, height=3, width=8, font=self.FONT, borderwidth=2,
                           command=lambda: self.single_operator_helper(text))
        button.grid(row=row, column=column)

    # This function creates the buttons for 2 operand operators such as addition and subtraction
    def create_two_operand_button(self, text, row, column):
        button = tk.Button(text=text, height=3, width=8, font=self.FONT, borderwidth=2,
                           command=lambda: self.operator_helper(text))
        button.grid(row=row, column=column)

    # This function creates the button for the equals sign
    def create_equals_button(self, text, row, column):
        button = tk.Button(text=text, height=3, width=8, font=self.FONT, borderwidth=2,
                           command=lambda: self.calculate())
        button.grid(row=row, column=column)

    # This function creates the button for the clear function
    def create_clear_button(self, text, row, column):
        button = tk.Button(text=text, height=3, width=8, font=self.FONT, borderwidth=2,
                           command=lambda: self.entry.delete(0, tk.END))
        button.grid(row=row, column=column)

    # This function adds a digit or decimal point to the display and will clear the display if the 
    #   flag is set to True, that happens only after an operator button or the equals button has been pressed.
    def numeral_helper(self, number):
        if self.clear_input_on_next_numeral:
            self.entry.delete(0, tk.END)
            self.clear_input_on_next_numeral = False
        self.entry.insert(tk.END, number)

    # This function will calculate the result on the button press
    def single_operator_helper(self, operator):
        if self.is_float(self.entry.get()):
            self.operator = operator
            result = self.cm.calculate(self.operator, self.entry.get())
        else:
            result = "Error: non-numeric entry"
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(result))

    # This function will store the value and operator in the self.number and self.operator variables
    #   until the equals button is pressed
    def operator_helper(self, operator):
        if self.is_float(self.entry.get()):
            self.number = self.entry.get()
            self.operator = operator
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error: non-numeric entry")
        self.clear_input_on_next_numeral = True

    # Helper function to check is the string input can be cast to a float
    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
        
    # This function is bound to the equals button using lambda functionality
    def calculate(self):
        result = self.cm.calculate(self.operator, self.number, self.entry.get())
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(result))
        self.clear_input_on_next_numeral = True
        '''
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
        '''
    def handle_keypress(self, event):
     key = event.char
     allowed_chars = "0123456789.+-*/=\x08"  # Allowed characters: digits, decimal point, operators, equals, and backspace

     if key in allowed_chars:
        if key == '=':  # Process equals sign
            self.calculate()
        elif key == '\x08':  # Process backspace/delete
            self.entry.delete(len(self.entry.get()) - 1)
        else:
            self.numeral_helper(key)


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
    
