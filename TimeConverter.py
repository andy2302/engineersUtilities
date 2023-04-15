import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import subprocess
import sys
from os.path import abspath, dirname, join


def open_time_converter():
    time_conv_path = abspath(join(dirname(__file__), 'TimeConverter.py'))
    subprocess.Popen([sys.executable, time_conv_path])


class TimeConverter(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Time Converter')
        self.geometry('450x500')

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
            "Microseconds": 0.000001,
            "Milliseconds": 0.001,
            "Seconds": 1,
            "Minutes": 60,
            "Hours": 3600,
            "Days": 86400,
            "Weeks": 604800,
            "Years": 31536000,
        }

        sorted_units = sorted(units.items(), key=lambda x: x[1])

        self.from_unit = ctk.CTkComboBox(self, values=[unit[0] for unit in sorted_units], font=('Arial', 14), width=300)
        self.from_unit.grid(row=0, column=1, padx=10, pady=10)

        self.to_unit = ctk.CTkComboBox(self, values=[unit[0] for unit in sorted_units], font=('Arial', 14), width=300)
        self.to_unit.grid(row=1, column=1, padx=10, pady=10)

        # create entry widgets
        self.amount_entry = ctk.CTkEntry(self, font=('Arial', 14), width=300)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

        self.result_entry = ctk.CTkEntry(self, font=('Arial', 14), width=300)
        self.result_entry.grid(row=3, column=1, padx=10, pady=10)

        # create convert button
        self.convert_button = ctk.CTkButton(self,
                                            text='Convert', font=('Arial', 14), command=self.convert_time_unit)
        self.convert_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        # create quit button
        self.quit_button = ctk.CTkButton(self, text='Quit', font=('Arial', 14), command=self.destroy)
        self.quit_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

        self.mainloop()

    def get_conversion_factor(self, unit):
        units = {
            "Microseconds": 0.000001,
            "Milliseconds": 0.001,
            "Seconds": 1,
            "Minutes": 60,
            "Hours": 3600,
            "Days": 86400,
            "Weeks": 604800,
            "Years": 31536000,
            }
        return units.get(unit)

    def convert_time_unit(self):
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

            # format result with commas
            formatted_result = format(round(result, 4), ',.4f')

            # set result
            self.result_entry.delete(0, ctk.END)
            self.result_entry.insert(0, formatted_result)

        except ValueError as e:
            tk.messagebox.showerror('Error', str(e))


if __name__ == '__main__':
    TimeConverter()