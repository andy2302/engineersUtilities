import customtkinter as ctk
import subprocess
import sys
from os.path import abspath, dirname, join
import math


def open_angle_converter():
    angle_converter_path = abspath(join(dirname(__file__), 'AngleConverter.py'))
    subprocess.Popen([sys.executable, angle_converter_path])


class AngleConverter(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Angle Converter")
        self.geometry("400x200")

        self.iconbitmap('E:/Python Projects Uni/engineersUtilities/assets/converter.ico')

        # Create variables to store values entered by user
        self.degrees_var = ctk.StringVar()
        self.radians_var = ctk.StringVar()
        self.gradians_var = ctk.StringVar()

        # Create labels for each conversion type
        ctk.CTkLabel(self, text="Degrees").grid(column=0, row=0, padx=5, pady=5)
        ctk.CTkLabel(self, text="Radians").grid(column=0, row=1, padx=5, pady=5)
        ctk.CTkLabel(self, text="Gradians").grid(column=0, row=2, padx=5, pady=5)

        # Create entry fields for user input
        ctk.CTkEntry(self, textvariable=self.degrees_var, width=300).grid(column=1, row=0, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.radians_var, width=300).grid(column=1, row=1, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.gradians_var, width=300).grid(column=1, row=2, padx=5, pady=5)

        # Bind the variables to their respective conversion functions
        self.degrees_var.trace("w", self.degrees_to_all)
        self.radians_var.trace("w", self.radians_to_all)
        self.gradians_var.trace("w", self.gradians_to_all)

        self.mainloop()

    def degrees_to_all(self, *args):
        try:
            degrees = float(self.degrees_var.get())
            radians = degrees * math.pi / 180
            gradians = degrees * 200 / 180
            self.radians_var.set(round(radians, 5))
            self.gradians_var.set(round(gradians, 5))
        except ValueError:
            pass

    def radians_to_all(self, *args):
        try:
            radians = float(self.radians_var.get())
            degrees = radians * 180 / math.pi
            gradians = degrees * 200 / 180
            self.degrees_var.set(round(degrees, 5))
            self.gradians_var.set(round(gradians, 5))
        except ValueError:
            pass

    def gradians_to_all(self, *args):
        try:
            gradians = float(self.gradians_var.get())
            degrees = gradians * 180 / 200
            radians = degrees * math.pi / 180
            self.degrees_var.set(round(degrees, 5))
            self.radians_var.set(round(radians, 5))
        except ValueError:
            pass


if __name__ == '__main__':
    AngleConverter()
