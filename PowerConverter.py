import customtkinter as ctk
import subprocess
import sys
from os.path import abspath, dirname, join


def open_power_converter():
    power_converter_path = abspath(join(dirname(__file__), 'PowerConverter.py'))
    subprocess.Popen([sys.executable, power_converter_path])


class PowerConverter(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Power Converter")
        self.geometry("500x200")

        self.iconbitmap('E:/Python Projects Uni/engineersUtilities/assets/converter.ico')

        # Create variables to store values entered by user
        self.watts_var = ctk.StringVar()
        self.kilowatts_var = ctk.StringVar()
        self.hp_var = ctk.StringVar()
        self.fpmin_var = ctk.StringVar()
        self.btumin_var = ctk.StringVar()

        # Create labels for each conversion type
        ctk.CTkLabel(self, text="Watts").grid(column=0, row=0, padx=5, pady=5)
        ctk.CTkLabel(self, text="Kilowatts").grid(column=0, row=1, padx=5, pady=5)
        ctk.CTkLabel(self, text="Horsepower (US)").grid(column=0, row=2, padx=5, pady=5)
        ctk.CTkLabel(self, text="Foot-pounds/minute").grid(column=0, row=3, padx=5, pady=5)
        ctk.CTkLabel(self, text="BTUs/minute").grid(column=0, row=4, padx=5, pady=5)

        # Create entry fields for user input
        ctk.CTkEntry(self, textvariable=self.watts_var, width=300).grid(column=1, row=0, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.kilowatts_var, width=300).grid(column=1, row=1, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.hp_var, width=300).grid(column=1, row=2, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.fpmin_var, width=300).grid(column=1, row=3, padx=5, pady=5)
        ctk.CTkEntry(self, textvariable=self.btumin_var, width=300).grid(column=1, row=4, padx=5, pady=5)

        # Bind the variables to their respective conversion functions
        self.watts_var.trace("w", self.watts_to_all)
        self.kilowatts_var.trace("w", self.kilowatts_to_all)
        self.hp_var.trace("w", self.hp_to_all)
        self.fpmin_var.trace("w", self.fpmin_to_all)
        self.btumin_var.trace("w", self.btumin_to_all)

        self.mainloop()

    def watts_to_all(self, *args):
        try:
            watts = float(self.watts_var.get())
            kilowatts = watts / 1000.0
            hp = watts / 745.7
            fpmin = watts * 44.25
            btumin = watts * 0.056869
            self.kilowatts_var.set(round(kilowatts, 5))
            self.hp_var.set(round(hp, 5))
            self.fpmin_var.set(round(fpmin, 5))
            self.btumin_var.set(round(btumin, 5))
        except ValueError:
            pass

    def kilowatts_to_all(self, *args):
        try:
            kilowatts = float(self.kilowatts_var.get())
            watts = kilowatts * 1000.0
            hp = watts / 745.7
            fpmin = watts * 44.25
            btumin = watts * 0.056869
            self.watts_var.set(round(watts, 5))
            self.hp_var.set(round(hp, 5))
            self.fpmin_var.set(round(fpmin, 5))
            self.btumin_var.set(round(btumin, 5))
        except ValueError:
            pass

    def hp_to_all(self, *args):
        try:
            hp = float(self.hp_var.get())
            watts = hp * 745.7
            kilowatts = watts / 1000.0
            fpmin = watts * 44.25
            btumin = watts * 0.056869
            self.watts_var.set(round(watts, 5))
            self.kilowatts_var.set(round(kilowatts, 5))
            self.fpmin_var.set(round(fpmin, 5))
            self.btumin_var.set(round(btumin, 5))
        except ValueError:
            pass

    def fpmin_to_all(self, *args):
        try:
            fpmin = float(self.fpmin_var.get())
            watts = fpmin / 44.25
            kilowatts = watts / 1000.0
            hp = watts / 745.7
            btumin = watts * 0.056869
            self.watts_var.set(round(watts, 5))
            self.kilowatts_var.set(round(kilowatts, 5))
            self.hp_var.set(round(hp, 5))
            self.btumin_var.set(round(btumin, 5))
        except ValueError:
            pass

    def btumin_to_all(self, *args):
        try:
            btumin = float(self.btumin_var.get())
            watts = btumin / 0.056869
            kilowatts = watts / 1000.0
            hp = watts / 745.7
            fpmin = watts * 44.25
            self.watts_var.set(round(watts, 5))
            self.kilowatts_var.set(round(kilowatts, 5))
            self.hp_var.set(round(hp, 5))
            self.fpmin_var.set(round(fpmin, 5))
        except ValueError:
            pass


if __name__ == '__main__':
    PowerConverter()
