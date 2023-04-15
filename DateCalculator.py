import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime as dt
from tkcalendar import Calendar
import subprocess
import sys
from os.path import abspath, dirname, join

# This Calculator needs some refactoring and improvements

def open_date_calculator():
    date_calc_path = abspath(join(dirname(__file__), 'DateCalculator.py'))
    subprocess.Popen([sys.executable, date_calc_path])


class DateCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.day_entry = None
        self.day_label = None
        self.month_entry = None
        self.month_label = None
        self.year_entry = None
        self.year_label = None
        self.subtract_radio = None
        self.add_radio = None
        self.rad_var = None
        self.title('Date Calculator')
        self.geometry('600x600')

        self.iconbitmap('E:/Python Projects Uni/engineersUtilities/assets/converter.ico')

        # Move the StringVar creation to after the Tk initialization
        self.rad_var = tk.StringVar()

        self.mode = tk.StringVar()
        self.mode.set("Difference between dates")
        self.mode.trace("w", lambda *args: self.update_interface(self.mode.get()))

        self.dropdown = ttk.Combobox(self, textvariable=self.mode, values=["Difference between dates", "Add or Subtract days, months or years"], state="readonly")
        self.dropdown.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.date_label = ttk.Label(self, text="Date:")
        self.date_label.grid(row=1, column=0, padx=10, pady=10)

        self.date_entry = Calendar(self)
        self.date_entry.grid(row=1, column=1, padx=10, pady=10)

        self.date_label_2 = ttk.Label(self, text="Date:")
        self.date_label_2.grid(row=2, column=0, padx=10, pady=10)

        self.date_entry_2 = Calendar(self)
        self.date_entry_2.grid(row=2, column=1, padx=10, pady=10)

        self.result_label = ttk.Label(self, text="Result:")
        self.result_label.grid(row=3, column=0, padx=10, pady=10)

        self.result_entry = ttk.Entry(self)
        self.result_entry.grid(row=3, column=1, padx=10, pady=10)

        self.calculate_button = ttk.Button(self, text="Calculate", command=self.calculate_dates)
        self.calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.protocol("WM_DELETE_WINDOW", self.quit_app)

        self.create_add_subtract_widgets()  # Move this line inside the __init__ method
        self.update_interface(self.mode.get())

        self.mainloop()

    def quit_app(self):
        self.destroy()

    def calculate_dates(self):
        mode = self.mode.get()

        # Get the date1 input as a datetime.date object
        date1 = self.date_entry.selection_get()

        if mode == "Difference between dates":
            # Get the date2 input as a datetime.date object
            date2 = self.date_entry_2.selection_get()
            difference = abs(date2 - date1).days
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, f"{difference} days")
        else:
            years, months, days = self.get_year_month_day()
            if self.rad_var.get() == "subtract":
                years, months, days = -years, -months, -days

            new_date = date1 + dt.timedelta(days=(years * 365) + (months * 30) + days)
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, new_date.strftime("%Y-%m-%d"))

    def create_add_subtract_widgets(self):
        # Initialize the StringVar here and pass self as master
        self.rad_var = tk.StringVar(self)

        self.add_radio = ttk.Radiobutton(self, text="Add", variable=self.rad_var, value="add")
        self.add_radio.grid(row=5, column=0, padx=10, pady=10)

        self.subtract_radio = ttk.Radiobutton(self, text="Subtract", variable=self.rad_var, value="subtract")
        self.subtract_radio.grid(row=5, column=1, padx=10, pady=10)

        self.year_label = ttk.Label(self, text="Years:")
        self.year_label.grid(row=6, column=0, padx=10, pady=10)

        self.year_entry = ttk.Entry(self)
        self.year_entry.grid(row=6, column=1, padx=10, pady=10)

        self.month_label = ttk.Label(self, text="Months:")
        self.month_label.grid(row=7, column=0, padx=10, pady=10)

        self.month_entry = ttk.Entry(self)
        self.month_entry.grid(row=7, column=1, padx=10, pady=10)

        self.day_label = ttk.Label(self, text="Days:")
        self.day_label.grid(row=8, column=0, padx=10, pady=10)

        self.day_entry = ttk.Entry(self)
        self.day_entry.grid(row=8, column=1, padx=10, pady=10)

    def get_year_month_day(self):
        try:
            years = int(self.year_entry.get())
            months = int(self.month_entry.get())
            days = int(self.day_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for years, months, and days.")
            return

        return years, months, days

    def update_interface(self, mode):
        if mode == "Difference between dates":
            self.date_label_2.grid()
            self.date_entry_2.grid()
            self.calculate_button.configure(command=self.calculate_dates)
            self.add_radio.grid_remove()
            self.subtract_radio.grid_remove()
            self.year_label.grid_remove()
            self.year_entry.grid_remove()
            self.month_label.grid_remove()
            self.month_entry.grid_remove()
            self.day_label.grid_remove()
            self.day_entry.grid_remove()
        else:
            self.date_label_2.grid_remove()
            self.date_entry_2.grid_remove()
            self.calculate_button.configure(command=self.calculate_dates)
            self.add_radio.grid()
            self.subtract_radio.grid()
            self.year_label.grid()
            self.year_entry.grid()
            self.month_label.grid()
            self.month_entry.grid()
            self.day_label.grid()
            self.day_entry.grid()


if __name__ == '__main__':
    app = DateCalculator()
    # app.update_interface(app.mode.get())

