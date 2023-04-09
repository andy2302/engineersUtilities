# some test to see how i'll implement the images
import customtkinter as ctk
from PIL import Image


def on_calc_button_click():
    print("Calculator")


def on_button_click():
    print("Click1")


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

my_image = ctk.CTkImage(light_image=Image.open("E:/Python Projects Uni/engineersUtilities/assets/menu.png"),
                                  dark_image=Image.open("E:/Python Projects Uni/engineersUtilities/assets/menu.png"),
                                  size=(200, 200))

image_label = ctk.CTkLabel(window, image=my_image)
image_label.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

window.add("Calculators")
window.add("Converters")

# Calculators
window.calc_button = ctk.CTkButton(master=window.tab("Calculators"), text='Calculator', command=on_calc_button_click)
window.calc_button.grid(row=0, column=0, padx=20, pady=10)

window.button = ctk.CTkButton(master=window.tab("Calculators"), text='Click me!', command=on_button_click)
window.button.grid(row=0, column=1, padx=20, pady=10)

# Converters
window.button = ctk.CTkButton(master=window.tab("Converters"), text='Distances', command=on_button_click)
window.button.grid(row=0, column=0, padx=20, pady=10)

window.button = ctk.CTkButton(master=window.tab("Converters"), text='Weights', command=on_button_click)
window.button.grid(row=0, column=1, padx=20, pady=10)

window.button = ctk.CTkButton(master=window.tab("Converters"), text='Temperatures', command=on_button_click)
window.button.grid(row=0, column=2, padx=20, pady=10)

window.button = ctk.CTkButton(master=window.tab("Converters"), text='Binary Hex and Decimal', command=on_button_click)
window.button.grid(row=1, column=0, padx=20, pady=10)


quit_button = ctk.CTkButton(window, text='Quit', command=window.quit)
quit_button.grid(row=3, column=0, padx=20, pady=20)

# add padding to center the widgets in the window
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_columnconfigure(0, weight=1)

window.mainloop()

#
# app = App()
