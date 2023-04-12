import customtkinter as ctk
import subprocess
import sys
from os.path import abspath, dirname, join


def open_programmer():
    programmer_path = abspath(join(dirname(__file__), 'ProgrammerConverter.py'))
    subprocess.Popen([sys.executable, programmer_path])


class ConversionBin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Programmer")
        self.geometry("400x150")

        self.iconbitmap('E:/Python Projects Uni/engineersUtilities/assets/converter.ico')

        # Create variables to store values entered by user
        self.decimal_var = ctk.StringVar()
        self.binary_var = ctk.StringVar()
        self.hexadecimal_var = ctk.StringVar()
        self.octal_var = ctk.StringVar()

        # Create labels for each conversion type
        ctk.CTkLabel(self, text="Decimal").grid(column=0, row=0, padx=5, pady=5)
        ctk.CTkLabel(self, text="Binary").grid(column=0, row=1, padx=5, pady=5)
        ctk.CTkLabel(self, text="Hexadecimal").grid(column=0, row=2, padx=5, pady=5)
        ctk.CTkLabel(self, text="Octal").grid(column=0, row=3, padx=5, pady=5)

        # Create entry fields for user input
        ctk.CTkEntry(self, textvariable=self.decimal_var, width=300).grid(column=1, row=0, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.binary_var, width=300).grid(column=1, row=1, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.hexadecimal_var, width=300).grid(column=1, row=2, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.octal_var, width=300).grid(column=1, row=3, padx=5, pady=5)

        # Bind the variables to their respective conversion functions
        self.decimal_var.trace("w", self.decimal_to_all)
        self.binary_var.trace("w", self.binary_to_all)
        self.hexadecimal_var.trace("w", self.hexadecimal_to_all)
        self.octal_var.trace("w", self.octal_to_all)

        self.mainloop()

    def decimal_to_all(self, *args):
        try:
            decimal = int(self.decimal_var.get())
            binary = format(decimal, "b").zfill(8)
            self.binary_var.set(" ".join([binary[i:i + 4] for i in range(0, len(binary), 4)]))
            self.hexadecimal_var.set(hex(decimal)[2:])
            self.octal_var.set(oct(decimal)[2:])
        except ValueError:
            pass

    def binary_to_all(self, *args):
        try:
            binary = self.binary_var.get().replace(" ", "")
            decimal = int(binary, 2)
            binary = binary.zfill(8)
            self.decimal_var.set(decimal)
            self.binary_var.set(" ".join([binary[i:i + 4] for i in range(0, len(binary), 4)]))
            self.hexadecimal_var.set(hex(decimal)[2:])
            self.octal_var.set(oct(decimal)[2:])
        except ValueError:
            pass

    def hexadecimal_to_all(self, *args):
        try:
            hexadecimal = self.hexadecimal_var.get()
            decimal = int(hexadecimal, 16)
            binary = format(decimal, "b").zfill(4)
            self.decimal_var.set(decimal)
            self.binary_var.set(" ".join([binary[i:i+4] for i in range(0, len(binary), 4)]))
            self.hexadecimal_var.set(hexadecimal.upper())
            self.octal_var.set(oct(decimal)[2:])
        except ValueError:
            pass

    def octal_to_all(self, *args):
        try:
            octal = self.octal_var.get()
            decimal = int(octal, 8)
            binary = format(decimal, "b").zfill(4)
            self.decimal_var.set(decimal)
            self.binary_var.set(" ".join([binary[i:i+4] for i in range(0, len(binary), 4)]))
            self.hexadecimal_var.set(hex(decimal)[2:].upper())
            self.octal_var.set(octal)
        except ValueError:
            pass


if __name__ == '__main__':
    ConversionBin()

