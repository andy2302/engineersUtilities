import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import subprocess
import sys
from os.path import abspath, dirname, join


def open_mass():
    mass_path = abspath(join(dirname(__file__), 'MassConverter.py'))
    subprocess.Popen([sys.executable, mass_path])


class MassConverter(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Mass Converter')
        self.geometry('500x400')

        self.iconbitmap('E:/Python Projects Uni/engineersUtilities/assets/converter.ico')

        # create labels
        self.from_label = ctk.CTkLabel(self, text='From:', font=('Arial', 14))
        self.from_label.grid(row=0, column=0, padx=10, pady=10)

        self.to_label = ctk.CTkLabel(self, text='To:', font=('Arial', 14))
        self.to_label.grid(row=1, column=0, padx=10, pady=10)

        self.amount_label = ctk.CTkLabel(self, text='Amount:', font=('Arial', 14))
        self.amount_label.grid(row=2, column=0, padx=10, pady=10)

        self.result_label = ctk.CTkLabel(self, text='Result:', font=('Arial', 14))
        self.result_label.grid(row=3, column=0, padx=10, pady=10)

        # create dropdowns
        units = {
            "Carats": 0.2,
            "Milligrams": 0.001,
            "Centigrams": 0.01,
            "Decigrams": 0.1,
            "Grams": 1,
            "Dekagrams": 10,
            "Hectograms": 100,
            "Kilograms": 1000,
            "Metric tonnes": 1e6,
            "Ounces": 28.3495,
            "Pounds": 453.592,
            "Stone": 6350.29,
            "Short tons (US)": 907185,
            "Long tons (UK)": 1016046,
        }

        sorted_units = sorted(units.items(), key=lambda x: x[1])

        self.from_unit = ctk.CTkComboBox(self, values=[unit[0] for unit in sorted_units], font=('Arial', 14))
        self.from_unit.grid(row=0, column=1, padx=10, pady=10)

        self.to_unit = ctk.CTkComboBox(self, values=[unit[0] for unit in sorted_units], font=('Arial', 14))
        self.to_unit.grid(row=1, column=1, padx=10, pady=10)

        # create entry widgets
        self.amount_entry = ctk.CTkEntry(self, font=('Arial', 14))
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

        self.result_entry = ctk.CTkEntry(self, font=('Arial', 14))
        self.result_entry.grid(row=3, column=1, padx=10, pady=10)

        # create convert button
        self.convert_button = ctk.CTkButton(self,
                                            text='Convert', font=('Arial', 14), command=self.convert_mass)
        self.convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # create quit button
        self.quit_button = ctk.CTkButton(self, text='Quit', font=('Arial', 14), command=self.destroy)
        self.quit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.mainloop()

    def get_conversion_factor(self, unit):
        units = {
            "Carats": 0.2,
            "Milligrams": 0.001,
            "Centigrams": 0.01,
            "Decigrams": 0.1,
            "Grams": 1,
            "Dekagrams": 10,
            "Hectograms": 100,
            "Kilograms": 1000,
            "Metric tonnes": 1e6,
            "Ounces": 28.3495,
            "Pounds": 453.592,
            "Stone": 6350.29,
            "Short tons (US)": 907185,
            "Long tons (UK)": 1016046,
        }
        return units.get(unit)

    def convert_mass(self):
        try:
            # get input values
            from_unit = self.from_unit.get()
            from_value = self.get_conversion_factor(from_unit)
            to_unit = self.to_unit.get()
            to_value = self.get_conversion_factor(to_unit)
            amount = float(self.amount_entry.get())

            if not from_value or not to_value:
                raise ValueError('Please select a unit from the dropdown menus.')

            # calculate result
            result = amount * from_value / to_value

            # set result
            self.result_entry.delete(0, ctk.END)
            self.result_entry.insert(0, round(result, 4))

        except ValueError as e:
            tk.messagebox.showerror('Error', str(e))


if __name__ == '__main__':
    MassConverter()
