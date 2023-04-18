import tkinter as tk
import math
import subprocess
import sys
from os.path import abspath, dirname, join


def open_sci_calc():
    sci_path = abspath(join(dirname(__file__), 'ScientificCalculator.py'))
    subprocess.Popen([sys.executable, sci_path])


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("480x400")
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), justify="right", bd=10)
        entry.grid(row=0, column=0, columnspan=6)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4), ('(', 1, 5),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4), (')', 2, 5),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('10^x', 3, 4), ('n!', 3, 5),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3), ('x^y', 4, 4), ('ln', 4, 5),
            ('=', 5, 0, 1, 5), ('log', 5, 5)
        ]

        for btn in buttons:
            text, row, col = btn[:3]
            rowspan = btn[3] if len(btn) > 3 else 1
            colspan = btn[4] if len(btn) > 4 else 1

            if len(text) == 1 or text == "C":
                btn_widget = tk.Button(self, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            else:
                btn_widget = tk.Button(self, text=text, font=("Arial", 14), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            btn_widget.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew")

    def on_button_click(self, text):
        current_result = self.result_var.get()

        if text == "C":
            self.result_var.set("0")
        elif text == "=":
            try:
                self.result_var.set(eval(current_result))
            except Exception as e:
                self.result_var.set("Error")
        elif text in ("sqrt", "ln", "log", "10^x", "n!"):
            try:
                value = float(current_result)
                if text == "sqrt":
                    self.result_var.set(math.sqrt(value))
                elif text == "ln":
                    self.result_var.set(math.log(value))
                elif text == "log":
                    self.result_var.set(math.log10(value))
                elif text == "10^x":
                    self.result_var.set(10 ** value)
                elif text == "n!":
                    self.result_var.set(math.factorial(int(value)))
            except Exception as e:
                self.result_var.set("Error")
        elif text == "x^y":
            self.result_var.set(current_result + "**")
        else:
            if current_result == "0" or current_result == "Error":
                self.result_var.set(text)
            else:
                self.result_var.set(current_result + text)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

