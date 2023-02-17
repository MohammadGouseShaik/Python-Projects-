import math
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        # Create the display
        self.display = tk.Entry(master, width=40, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create the buttons
        button_text = [
            "sin", "cos", "tan", "log",
            "sqrt", "^", "(", ")",
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "pi", "+",
            "Clear", "Enter"
        ]
        self.buttons = []
        for i in range(6):
            for j in range(4):
                index = 4 * i + j
                text = button_text[index]
                button = tk.Button(master, text=text, width=7, height=3,
                                   command=lambda text=text: self.button_click(text))
                button.grid(row=i+1, column=j, padx=2, pady=2)
                self.buttons.append(button)

    def button_click(self, text):
        if text == "Clear":
            self.display.delete(0, tk.END)
        elif text == "Enter":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "sin":
            self.display.insert(tk.END, "math.sin(")
        elif text == "cos":
            self.display.insert(tk.END, "math.cos(")
        elif text == "tan":
            self.display.insert(tk.END, "math.tan(")
        elif text == "log":
            self.display.insert(tk.END, "math.log10(")
        elif text == "sqrt":
            self.display.insert(tk.END, "math.sqrt(")
        elif text == "^":
            self.display.insert(tk.END, "**")
        elif text == "pi":
            self.display.insert(tk.END, str(math.pi))
        else:
            self.display.insert(tk.END, text)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
