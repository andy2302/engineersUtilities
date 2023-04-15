from abc import ABC
import customtkinter as ctk
from SimpleCalculator.calculator import open_calculator
from DistanceConverter import open_distance_converter
from developmentFeatures import open_indev_features
from ProgrammerConverter import open_programmer
from TemperatureConverter import open_temp_converter
from VolumeConverter import open_volume
from DataConverter import open_data_conversion
from MassConverter import open_mass
from EnergyConverter import open_energy
from AreaConverter import open_area
from CurrencyConverter import open_currency_conv
from SpeedConverter import open_speed_conversion
from TimeConverter import open_time_converter
from PowerConverter import open_power_converter
from PressureConverter import open_pressure_converter
from AngleConverter import open_angle_converter
from FrequencyConverter import open_freq_converter
import tkinter as tk
from tkinter import messagebox


def on_calc_button_click():
    open_calculator()


def on_programmer_click():
    open_programmer()


def on_dist_button_click():
    open_distance_converter()


def on_temp_conv_button_click():
    open_temp_converter()


def on_volume_conv_click():
    open_volume()


def on_mass_conv_click():
    open_mass()


def on_data_conv_click():
    open_data_conversion()


def on_energy_conv_click():
    open_energy()


def on_area_conv_click():
    open_area()


def on_currency_conv_click():
    open_currency_conv()


def on_speed_conv_click():
    open_speed_conversion()


def on_time_conv_click():
    open_time_converter()


def on_power_conv_click():
    open_power_converter()


def on_pressure_conv_click():
    open_pressure_converter()


def on_angle_conv_click():
    open_angle_converter()


def on_freq_conv_click():
    open_freq_converter()


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
                                         text='Calculator',  # Simple Calculator
                                         command=on_calc_button_click)
        self.calc_button.grid(row=0, column=0, padx=20, pady=10)

        self.scy_button = ctk.CTkButton(master=self.tab("Calculators"),
                                        text='Scientific',  # calculator with advanced functions, (ex. log, ln, etc.)
                                        command=development_button_click)
        self.scy_button.grid(row=0, column=1, padx=20, pady=10)

        self.BINARY_button = ctk.CTkButton(master=self.tab("Calculators"),
                                           text='Programmer',  # binary hex dec oct
                                           command=on_programmer_click)
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
                                       text='Data',
                                       command=on_data_conv_click)
        self.GB_button.grid(row=1, column=2, padx=20, pady=10)

        # Converters ------------------------------------------------------------------------------------------------
        # Create a canvas widget and a scrollbar widget
        self.converters_canvas = ctk.CTkCanvas(self.tab("Converters"))
        self.converters_scrollbar = ctk.CTkScrollbar(self.tab("Converters"),
                                                     command=self.converters_canvas.yview)
        self.converters_canvas.config(yscrollcommand=self.converters_scrollbar.set, bg='#2b2b2b')
        self.converters_scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

        # Create a frame inside the canvas to hold the converter buttons
        self.converters_frame = ctk.CTkFrame(self.converters_canvas)
        self.converters_canvas.create_window((0, 0), window=self.converters_frame, anchor='nw')

        self.dist_button = ctk.CTkButton(master=self.converters_frame,
                                         text='Distances',  # self-explanatory
                                         command=on_dist_button_click)
        self.dist_button.grid(row=0, column=0, padx=20, pady=10)

        self.weight_button = ctk.CTkButton(master=self.converters_frame,
                                           text='Weights',  # self-explanatory
                                           command=on_mass_conv_click)
        self.weight_button.grid(row=0, column=1, padx=20, pady=10)

        self.cur_button = ctk.CTkButton(master=self.converters_frame,
                                        text='Currency',  # self-explanatory
                                        command=on_currency_conv_click)
        self.cur_button.grid(row=0, column=2, padx=20, pady=10)

        self.vol_button = ctk.CTkButton(master=self.converters_frame,
                                        text='Volume',  # self-explanatory
                                        command=on_volume_conv_click)
        self.vol_button.grid(row=1, column=0, padx=20, pady=10)

        self.temp_button = ctk.CTkButton(master=self.converters_frame,
                                         text='Temperatures',  # self-explanatory
                                         command=on_temp_conv_button_click)
        self.temp_button.grid(row=1, column=1, padx=20, pady=10)

        self.energy_button = ctk.CTkButton(master=self.converters_frame,
                                           text='Energy',  # self-explanatory
                                           command=on_energy_conv_click)
        self.energy_button.grid(row=1, column=2, padx=20, pady=10)

        self.area_button = ctk.CTkButton(master=self.converters_frame,
                                         text='Area',  # self-explanatory
                                         command=on_area_conv_click)
        self.area_button.grid(row=2, column=0, padx=20, pady=10)

        self.speed_button = ctk.CTkButton(master=self.converters_frame,
                                          text='Speed',  # self-explanatory
                                          command=on_speed_conv_click)
        self.speed_button.grid(row=2, column=1, padx=20, pady=10)

        self.time_button = ctk.CTkButton(master=self.converters_frame,
                                         text='Time',  # self-explanatory
                                         command=on_time_conv_click)
        self.time_button.grid(row=2, column=2, padx=20, pady=10)

        self.power_button = ctk.CTkButton(master=self.converters_frame,
                                          text='Power',  # self-explanatory
                                          command=on_power_conv_click)
        self.power_button.grid(row=3, column=0, padx=20, pady=10)

        self.pressure_button = ctk.CTkButton(master=self.converters_frame,
                                             text='Pressure',  # self-explanatory
                                             command=on_pressure_conv_click)
        self.pressure_button.grid(row=3, column=1, padx=20, pady=10)

        self.angle_button = ctk.CTkButton(master=self.converters_frame,
                                          text='Angle',  # self-explanatory
                                          command=on_angle_conv_click)
        self.angle_button.grid(row=3, column=2, padx=20, pady=10)

        self.freq_button = ctk.CTkButton(master=self.converters_frame,
                                         text='Frequency',  # self-explanatory
                                         command=on_freq_conv_click)
        self.freq_button.grid(row=4, column=1, padx=20, pady=10)

        # Pack the canvas
        self.converters_frame = ctk.CTkFrame(self.converters_canvas, bg_color='#2b2b2b')
        self.converters_canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)
        self.converters_canvas.configure(width=100, height=100)  # Set the width and height of the canvas
        self.converters_canvas.bind('<Configure>', lambda e: self.converters_canvas.configure(
            scrollregion=self.converters_canvas.bbox('all')))

        # Bind mousewheel to the scrollbar
        self.master.bind_all('<MouseWheel>', self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.converters_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

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

        # Dev - after finishing development will be changed to another
        # functionality (ex. opening default calculator app) or something else
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
