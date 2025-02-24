import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("simple computer")
        
        # Used to store calculation expressions
        self.expression = ""
        # Add a new flag to determine whether the calculation has just been completed
        self.just_calculated = False

        # display area
        self.display = tk.Entry(master, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        # Button definition
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row = 1
        col = 0
        for button_text in buttons:
            button = tk.Button(master, text=button_text, padx=20, pady=20, font=("Arial", 18),
                               command=lambda bt=button_text: self.button_click(bt))
            button.grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, value):
        if value == "C":
            # clear expression
            self.expression = ""
            self.display.delete(0, tk.END)
            self.just_calculated = False
        elif value == "=":
            try:
                # calculation expression
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.expression = result
                # Set flag after calculation
                self.just_calculated = True
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error!")
                self.expression = ""
                self.just_calculated = False
        else:
            # If the calculation has just been completed and a number or decimal point is pressed, the old calculation formula will be automatically cleared and a new calculation will begin.
            if self.just_calculated and value in "0123456789.":
                self.expression = ""
                self.display.delete(0, tk.END)
                self.just_calculated = False
            else:
                # If the operation symbol is pressed, the old operation expression will not be cleared, allowing the user to continue the operation.
                self.just_calculated = False

            self.expression += value
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
