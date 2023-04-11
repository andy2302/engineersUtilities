import customtkinter as ctk
import subprocess
import sys
from os.path import abspath, dirname, join


def open_temp_converter():
    temperature_conv_path = abspath(join(dirname(__file__), 'TemperatureConverter.py'))
    subprocess.Popen([sys.executable, temperature_conv_path])


class TemperatureConverter(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Converter")
        self.geometry("400x200")

        self.iconbitmap('E:/Python Projects Uni/engineersUtilities/assets/converter.ico')

        self.celsius_var = ctk.DoubleVar()
        self.fahrenheit_var = ctk.DoubleVar()
        self.kelvin_var = ctk.DoubleVar()

        ctk.CTkLabel(self, text="Celsius:").grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.celsius_var, width=300).grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkLabel(self, text="Fahrenheit:").grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.fahrenheit_var, width=300).grid(row=1, column=1, padx=5, pady=5)
        ctk.CTkLabel(self, text="Kelvin:").grid(row=2, column=0, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.kelvin_var, width=300).grid(row=2, column=1, padx=5, pady=5)

        self.celsius_var.trace("w", self.convert_celsius)
        self.fahrenheit_var.trace("w", self.convert_fahrenheit)
        self.kelvin_var.trace("w", self.convert_kelvin)

        self.mainloop()

    def convert_celsius(self, *args):
        try:
            celsius = self.celsius_var.get()
            if celsius != "":
                celsius = float(celsius)
                fahrenheit = round(celsius * 9 / 5 + 32, 3)
                kelvin = round(celsius + 273.15, 3)
                self.fahrenheit_var.set(fahrenheit)
                self.kelvin_var.set(kelvin)
        except ValueError:
            pass

    def convert_fahrenheit(self, *args):
        try:
            fahrenheit = self.fahrenheit_var.get()
            if fahrenheit != "":
                fahrenheit = float(fahrenheit)
                celsius = round((fahrenheit - 32) * 5 / 9, 3)
                kelvin = round(celsius + 273.15, 3)
                self.celsius_var.set(celsius)
                self.kelvin_var.set(kelvin)
        except ValueError:
            pass

    def convert_kelvin(self, *args):
        try:
            kelvin = self.kelvin_var.get()
            if kelvin != "":
                kelvin = float(kelvin)
                celsius = round(kelvin - 273.15, 3)
                fahrenheit = round(celsius * 9 / 5 + 32, 3)
                self.celsius_var.set(celsius)
                self.fahrenheit_var.set(fahrenheit)
        except ValueError:
            pass


if __name__ == '__main__':
    TemperatureConverter()
