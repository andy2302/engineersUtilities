import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import subprocess
import sys
from os.path import abspath, dirname, join


def open_volume():
    volume_path = abspath(join(dirname(__file__), 'VolumeConverter.py'))
    subprocess.Popen([sys.executable, volume_path])


class VolumeConverter(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Volume Converter')
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
            "Milliliters": 1,
            "Cubic centimeters": 1,
            "Liters": 1000,
            "Cubic meters": 1e6,
            "Teaspoons (US)": 4.92892,
            "Tablespoons (US)": 14.7868,
            "Fluid ounces (US)": 29.5735,
            "Cups (US)": 236.588,
            "Pints (US)": 473.176,
            "Quarts (US)": 946.353,
            "Gallons (US)": 3785.41,
            "Cubic inches": 16.3871,
            "Cubic feet": 28316.8,
            "Cubic yards": 764555,
            "Teaspoons (UK)": 5.91939,
            "Tablespoons (UK)": 17.7582,
            "Fluid ounces (UK)": 28.4131,
            "Pints (UK)": 568.261,
            "Quarts (UK)": 1136.52,
            "Gallons (UK)": 4546.09,
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

        # create standard unit labels
        self.l_label = ctk.CTkLabel(self, text='Liters', font=('Arial', 14))
        self.l_label.grid(row=0, column=3, padx=30)

        self.ml_label = ctk.CTkLabel(self, text='Milliliters', font=('Arial', 14))
        self.ml_label.grid(row=1, column=3, padx=30)

        self.tsp_label = ctk.CTkLabel(self, text='Teaspoons (US)', font=('Arial', 14))
        self.tsp_label.grid(row=2, column=3, padx=30)

        self.tbsp_label = ctk.CTkLabel(self, text='Tablespoons (US)', font=('Arial', 14))
        self.tbsp_label.grid(row=3, column=3, padx=30)

        # create standard unit result labels
        self.l_result_label = ctk.CTkLabel(self, text='', font=('Arial', 14))
        self.l_result_label.grid(row=0, column=2, padx=30, sticky='E')

        self.ml_result_label = ctk.CTkLabel(self, text='', font=('Arial', 14))
        self.ml_result_label.grid(row=1, column=2, padx=30, sticky='E')

        self.tsp_result_label = ctk.CTkLabel(self, text='', font=('Arial', 14))
        self.tsp_result_label.grid(row=2, column=2, padx=30, sticky='E')

        self.tbsp_result_label = ctk.CTkLabel(self, text='', font=('Arial', 14))
        self.tbsp_result_label.grid(row=3, column=2, padx=30, sticky='E')

        # create convert button
        self.convert_button = ctk.CTkButton(self,
                                            text='Convert', font=('Arial', 14), command=self.convert_volume)
        self.convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # create quit button
        self.quit_button = ctk.CTkButton(self, text='Quit', font=('Arial', 14), command=self.destroy)
        self.quit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.mainloop()

    def get_conversion_factor(self, unit):
        units = {
            "Milliliters": 1,
            "Cubic centimeters": 1,
            "Liters": 1000,
            "Cubic meters": 1e6,
            "Teaspoons (US)": 4.92892,
            "Tablespoons (US)": 14.7868,
            "Fluid ounces (US)": 29.5735,
            "Cups (US)": 236.588,
            "Pints (US)": 473.176,
            "Quarts (US)": 946.353,
            "Gallons (US)": 3785.41,
            "Cubic inches": 16.3871,
            "Cubic feet": 28316.8,
            "Cubic yards": 764555,
            "Teaspoons (UK)": 5.91939,
            "Tablespoons (UK)": 17.7582,
            "Fluid ounces (UK)": 28.4131,
            "Pints (UK)": 568.261,
            "Quarts (UK)": 1136.52,
            "Gallons (UK)": 4546.09,
        }
        return units.get(unit)

    def convert_volume(self):
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

            # update standard unit result labels
            standard_units = {'l': 'Liters', 'ml': 'Milliliters', 'tsp': 'Teaspoons (US)', 'tbsp': 'Tablespoons (US)'}
            for key, value in standard_units.items():
                label = getattr(self, f"{key}_result_label")
                conversion_factor = self.get_conversion_factor(value)
                converted_value = amount * from_value / conversion_factor
                label.configure(text=f"{round(converted_value, 4)}")

        except ValueError as e:
            tk.messagebox.showerror('Error', str(e))


if __name__ == '__main__':
    VolumeConverter()
