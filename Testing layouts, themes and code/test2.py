from PIL import Image
import customtkinter as ctk

window = ctk.CTk()
window.title('Engineers Utilities')
window.geometry('1000x1000')

my_image = ctk.CTkImage(light_image=Image.open("E:/Python Projects Uni/engineersUtilities/assets/menu.png"),
                                  dark_image=Image.open("E:/Python Projects Uni/engineersUtilities/assets/menu.png"),
                                  size=(500, 500))

image_label = ctk.CTkLabel(window, image=my_image)
image_label.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

window.mainloop()
