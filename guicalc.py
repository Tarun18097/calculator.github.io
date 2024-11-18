import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.expression = ""  # To store the mathematical expression

        # Create display
        self.display = tk.Entry(root, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.display.insert(0, "0")  # Show 0 initially

        # Button layout
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        row = 1
        col = 0

        for button in buttons:
            btn = tk.Button(
                root,
                text=button,
                font=("Arial", 18),
                width=5,
                height=2,
                command=lambda b=button: self.on_button_click(b)
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:  # Move to next row after 4 columns
                col = 0
                row += 1

    def on_button_click(self, button):
        if button == "C":  # Clear the display
            self.expression = ""
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
        elif button == "=":  # Evaluate the expression
            try:
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.expression = str(result)
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        else:  # Add button value to the expression
            if self.display.get() == "0" or self.display.get() == "Error":
                self.display.delete(0, tk.END)
            self.expression += button
            self.display.insert(tk.END, button)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
