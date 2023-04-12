import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import subprocess
import sys
from os.path import abspath, dirname, join


def open_data_conversion():
    data_conv_path = abspath(join(dirname(__file__), 'DataConverter.py'))
    subprocess.Popen([sys.executable, data_conv_path])


class DataConverter(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Data Converter')
        self.geometry('450x500')

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
            "Bits": 1,
            "Bytes": 8,
            "Kilobits": 1000,
            "Kilobytes": 8000,
            "Kibibytes": 8192,
            "Megabits": 1e6,
            "Mebibits": 1048576,
            "Megabytes": 8e6,
            "Mebibytes": 8388608,
            "Gigabits": 1e9,
            "Gibibits": 1073741824,
            "Gigabytes": 8e9,
            "Gibibytes": 8589934592,
            "Terabits": 1e12,
            "Terabibits": 1099511627776,
            "Terabytes": 8e12,
            "Tebibytes": 8796093022208,
            "Petabits": 1e15,
            "Pebibits": 1125899906842624,
            "Petabytes": 8e15,
            "Pebibytes": 9007199254740992,
            "Exabits": 1e18,
            "Exbibits": 1152921504606846976,
            "Exabytes": 8e18,
            "Exbibytes": 9.223372036854776e+18,
            "Zetabits": 1e21,
            "Zebibits": 1180591620717411303424,
            "Zetabytes": 8e21,
            "Zebibytes": 9.444732965739290427e+21,
            "Yottabits": 1e24,
            "Yobibits": 1208925819614629174706176,
            "Yottabytes": 8e24,
            "Yobibytes": 9.671406556917033397e+24,
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
                                            text='Convert', font=('Arial', 14), command=self.convert_data_unit)
        self.convert_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        # create quit button
        self.quit_button = ctk.CTkButton(self, text='Quit', font=('Arial', 14), command=self.destroy)
        self.quit_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

        self.mainloop()

    def get_conversion_factor(self, unit):
        units = {
            "Bits": 1,
            "Bytes": 8,
            "Kilobits": 1000,
            "Kilobytes": 8000,
            "Kibibytes": 8192,
            "Megabits": 1000000,
            "Mebibits": 1048576,
            "Megabytes": 8000000,
            "Mebibytes": 8388608,
            "Gigabits": 1000000000,
            "Gibibits": 1073741824,
            "Gigabytes": 8000000000,
            "Gibibytes": 8589934592,
            "Terabits": 1000000000000,
            "Terabibits": 1099511627776,
            "Terabytes": 8000000000000,
            "Tebibytes": 8796093022208,
            "Petabits": 1000000000000000,
            "Pebibits": 1125899906842624,
            "Petabytes": 8000000000000000,
            "Pebibytes": 9007199254740992,
            "Exabits": 1000000000000000000,
            "Exbibits": 1152921504606846976,
            "Exabytes": 8000000000000000000,
            "Exbibytes": 10307921510400000000,
            "Zetabits": 1000000000000000000000,
            "Zebibits": 1180591620717411303424,
            "Zetabytes": 8000000000000000000000,
            "Zebibytes": 11258999068426240000000,
            "Yottabits": 1000000000000000000000000,
            "Yobibits": 1208925819614629174706176,
            "Yottabytes": 8000000000000000000000000,
            "Yobibytes": 12089258196146291747061760,
        }
        return units.get(unit)

    def convert_data_unit(self):
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
    DataConverter()


