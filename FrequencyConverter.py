import customtkinter as ctk
import subprocess
import sys
from os.path import abspath, dirname, join


def open_freq_converter():
    freq_converter_path = abspath(join(dirname(__file__), 'FrequencyConverter.py'))
    subprocess.Popen([sys.executable, freq_converter_path])


class FrequencyConverter(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Frequency Converter")
        self.geometry("800x200")

        self.iconbitmap('E:/Python Projects Uni/engineersUtilities/assets/converter.ico')

        # Create variables to store values entered by user
        self.hertz_var = ctk.StringVar()
        self.kilohertz_var = ctk.StringVar()
        self.megahertz_var = ctk.StringVar()
        self.gigahertz_var = ctk.StringVar()

        # Create labels for each conversion type
        ctk.CTkLabel(self, text="Hertz").grid(column=0, row=0, padx=5, pady=5)
        ctk.CTkLabel(self, text="Kilohertz").grid(column=0, row=1, padx=5, pady=5)
        ctk.CTkLabel(self, text="Megahertz").grid(column=0, row=2, padx=5, pady=5)
        ctk.CTkLabel(self, text="Gigahertz").grid(column=0, row=3, padx=5, pady=5)

        # Create entry fields for user input
        ctk.CTkEntry(self, textvariable=self.hertz_var, width=300).grid(column=1, row=0, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.kilohertz_var, width=300).grid(column=1, row=1, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.megahertz_var, width=300).grid(column=1, row=2, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.gigahertz_var, width=300).grid(column=1, row=3, padx=5, pady=5)

        # Bind the variables to their respective conversion functions
        self.hertz_var.trace("w", self.hertz_to_all)
        self.kilohertz_var.trace("w", self.kilohertz_to_all)
        self.megahertz_var.trace("w", self.megahertz_to_all)
        self.gigahertz_var.trace("w", self.gigahertz_to_all)

        self.mainloop()

    def hertz_to_all(self, *args):
        try:
            hertz = float(self.hertz_var.get())
            kilohertz = hertz / 1000
            megahertz = hertz / 1000000
            gigahertz = hertz / 1000000000
            self.kilohertz_var.set(format(kilohertz, '.15f'))
            self.megahertz_var.set(format(megahertz, '.15f'))
            self.gigahertz_var.set(format(gigahertz, '.15f'))
        except ValueError:
            pass

    def kilohertz_to_all(self, *args):
        try:
            kilohertz = float(self.kilohertz_var.get())
            hertz = kilohertz * 1000
            megahertz = hertz / 1000000
            gigahertz = hertz / 1000000000
            self.hertz_var.set(format(hertz, '.15f'))
            self.megahertz_var.set(format(megahertz, '.15f'))
            self.gigahertz_var.set(format(gigahertz, '.15f'))
        except ValueError:
            pass

    def megahertz_to_all(self, *args):
        try:
            megahertz = float(self.megahertz_var.get())
            hertz = megahertz * 1000000
            kilohertz = hertz / 1000
            gigahertz = hertz / 1000000000
            self.hertz_var.set(format(hertz, '.15f'))
            self.kilohertz_var.set(format(kilohertz, '.15f'))
            self.gigahertz_var.set(format(gigahertz, '.15f'))
        except ValueError:
            pass

    def gigahertz_to_all(self, *args):
        try:
            gigahertz = float(self.gigahertz_var.get())
            hertz = gigahertz * 1000000000
            kilohertz = hertz / 1000
            megahertz = hertz / 1000000
            self.hertz_var.set(format(hertz, '.15f'))
            self.kilohertz_var.set(format(kilohertz, '.15f'))
            self.megahertz_var.set(format(megahertz, '.15f'))
        except ValueError:
            pass


if __name__ == '__main__':
    FrequencyConverter()