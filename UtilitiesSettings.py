import json
import customtkinter as ctk
from tkinter import messagebox
import subprocess
import sys
from os.path import abspath, dirname, join
from elevate_privileges import elevate_privileges_and_grant_wmi_permissions

JSON_FILE = "shortcuts.json"


def open_settings():
    settings_path = abspath(join(dirname(__file__), 'UtilitiesSettings.py'))
    subprocess.Popen([sys.executable, settings_path])


class Settings(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Settings')
        self.geometry('450x500')

        self.shortcuts_frame = ctk.CTkFrame(self)
        self.shortcuts_frame.pack(padx=20, pady=20)

        self.app_name_label = ctk.CTkLabel(self.shortcuts_frame, text="App name:")
        self.app_name_label.grid(row=0, column=0, padx=(0, 10))
        self.app_name_entry = ctk.CTkEntry(self.shortcuts_frame)
        self.app_name_entry.grid(row=0, column=1)

        self.app_path_label = ctk.CTkLabel(self.shortcuts_frame, text="App path:")
        self.app_path_label.grid(row=1, column=0, padx=(0, 10))
        self.app_path_entry = ctk.CTkEntry(self.shortcuts_frame)
        self.app_path_entry.grid(row=1, column=1)

        self.add_shortcut_button = ctk.CTkButton(self.shortcuts_frame, text="Add Shortcut", command=self.add_shortcut)
        self.add_shortcut_button.grid(row=2, column=1, pady=(10, 0))

        self.grant_wmi_permissions_button = ctk.CTkButton(
            self.shortcuts_frame, text="Run as Admin", command=lambda: elevate_privileges_and_grant_wmi_permissions("main.py"))
        self.grant_wmi_permissions_button.grid(row=3, column=1, pady=(10, 0))

        self.mainloop()

    def add_shortcut(self):
        app_name = self.app_name_entry.get().strip()
        app_path = self.app_path_entry.get().strip()

        if not app_name or not app_path:
            messagebox.showerror("Error", "Both App name and App path must be provided")
            return

        shortcut = {"name": app_name, "path": app_path}

        try:
            with open(JSON_FILE, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(shortcut)

        with open(JSON_FILE, "w") as f:
            json.dump(data, f)

        messagebox.showinfo("Success", f"Shortcut for '{app_name}' added successfully")


if __name__ == '__main__':
    Settings()