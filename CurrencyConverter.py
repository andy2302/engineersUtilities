import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import subprocess
import sys
from os.path import abspath, dirname, join
from forex_python.converter import CurrencyRates
import requests
from dotenv import load_dotenv
import os


def open_currency_conv():
    currency_path = abspath(join(dirname(__file__), 'CurrencyConverter.py'))
    subprocess.Popen([sys.executable, currency_path])


load_dotenv()
print("API Key after loading .env:", os.environ.get('OPENEXCHANGERATES_API_KEY'))


class CurrencyConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Currency Converter')
        self.geometry('500x400')

        # Add your icon file path here
        self.iconbitmap('E:/Python Projects Uni/engineersUtilities/assets/converter.ico')

        # Create labels
        self.from_label = ctk.CTkLabel(self, text='From:', font=('Arial', 14))
        self.from_label.grid(row=0, column=0, padx=10, pady=10)

        self.to_label = ctk.CTkLabel(self, text='To:', font=('Arial', 14))
        self.to_label.grid(row=1, column=0, padx=10, pady=10)

        self.amount_label = ctk.CTkLabel(self, text='Amount:', font=('Arial', 14))
        self.amount_label.grid(row=2, column=0, padx=10, pady=10)

        self.result_label = ctk.CTkLabel(self, text='Result:', font=('Arial', 14))
        self.result_label.grid(row=3, column=0, padx=10, pady=10)

        # Create dropdowns
        self.currency_rates = CurrencyRates()
        self.currencies = sorted(self.get_available_currencies())

        self.from_currency = ctk.CTkComboBox(self, values=self.currencies, font=('Arial', 14))
        self.from_currency.grid(row=0, column=1, padx=10, pady=10)

        self.to_currency = ctk.CTkComboBox(self, values=self.currencies, font=('Arial', 14))
        self.to_currency.grid(row=1, column=1, padx=10, pady=10)

        # Create entry widgets
        self.amount_entry = ctk.CTkEntry(self, font=('Arial', 14))
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

        self.result_entry = ctk.CTkEntry(self, font=('Arial', 14))
        self.result_entry.grid(row=3, column=1, padx=10, pady=10)

        # Create convert button
        self.convert_button = ctk.CTkButton(self, text='Convert', font=('Arial', 14), command=self.convert_currency)
        self.convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Create quit button
        self.quit_button = ctk.CTkButton(self, text='Quit', font=('Arial', 14), command=self.destroy)
        self.quit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.mainloop()

    def get_available_currencies(self):
        api_key = os.environ.get('OPENEXCHANGERATES_API_KEY')  # replace with your api key api_key = 'YOUR_KEY'
        url = f"https://openexchangerates.org/api/currencies.json?app_id={api_key}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Failed to fetch currency rates")

        data = response.json()
        return data.keys()

    def get_conversion_rate(self, from_currency, to_currency):
        api_key = os.environ.get('OPENEXCHANGERATES_API_KEY')  # replace with your api key api_key = 'YOUR_KEY'
        print(f'API Key: {api_key}')

        url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&base=USD&symbols={from_currency},{to_currency}"
        response = requests.get(url)

        print(f"Request URL: {url}")  # Debugging line
        print(f"Response Status Code: {response.status_code}")  # Debugging line
        print(f"Response Content: {response.content}")  # Debugging line

        if response.status_code != 200:
            raise Exception("Failed to fetch conversion rate")

        data = response.json()
        from_rate = data["rates"][from_currency]
        to_rate = data["rates"][to_currency]
        return to_rate / from_rate

    def convert_currency(self):
        try:
            # Get input values
            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()
            amount = float(self.amount_entry.get())

            if not from_currency or not to_currency:
                raise ValueError('Please select a currency from the dropdown menus.')

            # Perform the conversion
            conversion_rate = self.get_conversion_rate(from_currency, to_currency)
            converted_amount = amount * conversion_rate

            # Set result
            self.result_entry.delete(0, ctk.END)
            self.result_entry.insert(0, round(converted_amount, 4))

        except ValueError as e:
            tk.messagebox.showerror('Error', str(e))


if __name__ == '__main__':
    CurrencyConverterApp()