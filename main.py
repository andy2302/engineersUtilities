from abc import ABC
import customtkinter as ctk


def on_calc_button_click():
    print("Calculator")


def on_button_click():
    print("Click1")


class MyTabView(ctk.CTkTabview, ABC):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Calculators")
        self.add("Converters")

        # Calculators
        self.calc_button = ctk.CTkButton(master=self.tab("Calculators"),
                                         text='Calculator',
                                         command=on_calc_button_click)
        self.calc_button.grid(row=0, column=0, padx=20, pady=10)

        self.button = ctk.CTkButton(master=self.tab("Calculators"),
                                    text='Click me!',
                                    command=on_button_click)
        self.button.grid(row=0, column=1, padx=20, pady=10)

        # Converters
        self.button = ctk.CTkButton(master=self.tab("Converters"),
                                    text='Distances',
                                    command=on_button_click)
        self.button.grid(row=0, column=0, padx=20, pady=10)

        self.button = ctk.CTkButton(master=self.tab("Converters"),
                                    text='Weights',
                                    command=on_button_click)
        self.button.grid(row=0, column=1, padx=20, pady=10)

        self.button = ctk.CTkButton(master=self.tab("Converters"),
                                    text='Temperatures',
                                    command=on_button_click)
        self.button.grid(row=0, column=2, padx=20, pady=10)

        self.button = ctk.CTkButton(master=self.tab("Converters"),
                                    text='Binary Hex and Decimal',
                                    command=on_button_click)
        self.button.grid(row=1, column=0, padx=20, pady=10)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        window = ctk.CTk()
        window.title('Engineers Utilities')
        window.geometry('600x600')

        # set the window icon
        window.iconbitmap('E:/Python Projects Uni/engineersUtilities/assets/mainMenu.ico')

        label = ctk.CTkLabel(window,
                             text='Engineers Utilities',
                             text_color=('blue', 'white'),
                             font=('Montserrat', 60),
                             anchor="center", pady=0)
        label.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        # Tab view
        self.tab_view = MyTabView(master=window)
        self.tab_view.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

        # Quit
        quit_button = ctk.CTkButton(window,
                                    text='Quit',
                                    command=self.quit)
        quit_button.grid(row=2, column=0, padx=20, pady=20)

        # add padding to center the widgets in the window
        window.grid_rowconfigure(0, weight=1)
        window.grid_rowconfigure(3, weight=1)
        window.grid_columnconfigure(0, weight=1)

        window.mainloop()


app = App()
