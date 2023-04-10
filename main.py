from abc import ABC
import customtkinter as ctk
from calculator import open_calculator
from DistanceConverter import open_distance_converter
from developmentFeatures import open_indev_features
import tkinter as tk
from tkinter import messagebox


def on_calc_button_click():
    open_calculator()


def on_dist_button_click():
    open_distance_converter()


def development_button_click():
    tk.messagebox.showerror('DEVELOPMENT', 'Feature currently under development')


def open_dev_feat():
    open_indev_features()


class MyTabView(ctk.CTkTabview, ABC):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs ------------------------------------------------------------------------------------------------
        self.add("Calculators")
        self.add("Converters")
        self.add("Information")
        self.add("PC statistics")

        # Calculators ------------------------------------------------------------------------------------------------
        self.calc_button = ctk.CTkButton(master=self.tab("Calculators"),
                                         text='Calculator',  # to add square root, power, 1 over x, memory
                                         command=on_calc_button_click)
        self.calc_button.grid(row=0, column=0, padx=20, pady=10)

        self.scy_button = ctk.CTkButton(master=self.tab("Calculators"),
                                        text='Scientific',  # calculator with advanced functions, (ex. log, ln, etc.)
                                        command=development_button_click)
        self.scy_button.grid(row=0, column=1, padx=20, pady=10)

        self.BINARY_button = ctk.CTkButton(master=self.tab("Calculators"),
                                           text='Programmer',  # binary hex dec oct
                                           command=development_button_click)
        self.BINARY_button.grid(row=0, column=2, padx=20, pady=10)

        self.date_button = ctk.CTkButton(master=self.tab("Calculators"),
                                         text='Date calculation',  # from date to date
                                         command=development_button_click)
        self.date_button.grid(row=1, column=0, padx=20, pady=10)

        self.graph_button = ctk.CTkButton(master=self.tab("Calculators"),
                                          text='Graphic',  # matplotlib?
                                          command=development_button_click)
        self.graph_button.grid(row=1, column=1, padx=20, pady=10)

        self.GB_button = ctk.CTkButton(master=self.tab("Calculators"),
                                       text='Data',  # matplotlib?
                                       command=development_button_click)
        self.GB_button.grid(row=1, column=2, padx=20, pady=10)

        # Converters ------------------------------------------------------------------------------------------------
        self.dist_button = ctk.CTkButton(master=self.tab("Converters"),
                                         text='Distances',  # self-explanatory
                                         command=on_dist_button_click)
        self.dist_button.grid(row=0, column=0, padx=20, pady=10)

        self.weight_button = ctk.CTkButton(master=self.tab("Converters"),
                                           text='Weights',  # self-explanatory
                                           command=development_button_click)
        self.weight_button.grid(row=0, column=1, padx=20, pady=10)

        self.cur_button = ctk.CTkButton(master=self.tab("Converters"),
                                        text='Currency',  # self-explanatory
                                        command=development_button_click)
        self.cur_button.grid(row=0, column=2, padx=20, pady=10)

        self.vol_button = ctk.CTkButton(master=self.tab("Converters"),
                                        text='Volume',  # self-explanatory
                                        command=development_button_click)
        self.vol_button.grid(row=1, column=0, padx=20, pady=10)

        self.temp_button = ctk.CTkButton(master=self.tab("Converters"),
                                         text='Temperatures',  # self-explanatory
                                         command=development_button_click)
        self.temp_button.grid(row=1, column=1, padx=20, pady=10)

        self.energy_button = ctk.CTkButton(master=self.tab("Converters"),
                                           text='Energy',  # self-explanatory
                                           command=development_button_click)
        self.energy_button.grid(row=1, column=2, padx=20, pady=10)

        self.area_button = ctk.CTkButton(master=self.tab("Converters"),
                                         text='Area',  # self-explanatory
                                         command=development_button_click)
        self.area_button.grid(row=2, column=0, padx=20, pady=10)

        self.speed_button = ctk.CTkButton(master=self.tab("Converters"),
                                          text='Speed',  # self-explanatory
                                          command=development_button_click)
        self.speed_button.grid(row=2, column=1, padx=20, pady=10)

        self.time_button = ctk.CTkButton(master=self.tab("Converters"),
                                         text='Time',  # self-explanatory
                                         command=development_button_click)
        self.time_button.grid(row=2, column=2, padx=20, pady=10)

        self.power_button = ctk.CTkButton(master=self.tab("Converters"),
                                          text='Power',  # self-explanatory
                                          command=development_button_click)
        self.power_button.grid(row=3, column=0, padx=20, pady=10)

        self.pressure_button = ctk.CTkButton(master=self.tab("Converters"),
                                             text='Pressure',  # self-explanatory
                                             command=development_button_click)
        self.pressure_button.grid(row=3, column=1, padx=20, pady=10)

        self.angle_button = ctk.CTkButton(master=self.tab("Converters"),
                                          text='Angle',  # self-explanatory
                                          command=development_button_click)
        self.angle_button.grid(row=3, column=2, padx=20, pady=10)

        # Information ------------------------------------------------------------------------------------------------
        self.electronic_button = ctk.CTkButton(master=self.tab("Information"),
                                               text='Electronics - Formulas, Schematic Design, PCB Design',
                                               # Information helpful for an electronic engineer/student
                                               command=development_button_click)
        self.electronic_button.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

        self.prog_button = ctk.CTkButton(master=self.tab("Information"),
                                         text='Programming - Languages, Building Apps, AI',
                                         # Information helpful for a programmer/student
                                         command=development_button_click)
        self.prog_button.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

        self.mech_button = ctk.CTkButton(master=self.tab("Information"),
                                         text='Mechanics - Physics, Motion, Materials and Applications',
                                         # Information helpful for a Mechanical engineer/student
                                         command=development_button_click)
        self.mech_button.grid(row=2, column=0, columnspan=3, padx=20, pady=10)

        self.robo_button = ctk.CTkButton(master=self.tab("Information"),
                                         text='Robotics - Combining Electronics and Mechanics with Programming',
                                         # Information helpful for an engineer getting into robotics
                                         command=development_button_click)
        self.robo_button.grid(row=3, column=0, columnspan=3, padx=20, pady=10)


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

        # Dev
        dev_button = ctk.CTkButton(window, text='In Dev Features', command=open_dev_feat)
        dev_button.grid(row=2, column=0, padx=20, pady=20)

        # Quit
        quit_button = ctk.CTkButton(window,
                                    text='Quit',
                                    command=self.quit)
        quit_button.grid(row=3, column=0, padx=20, pady=20)

        # add padding to center the widgets in the window
        window.grid_rowconfigure(0, weight=1)
        window.grid_rowconfigure(3, weight=1)
        window.grid_columnconfigure(0, weight=1)

        window.mainloop()


app = App()
