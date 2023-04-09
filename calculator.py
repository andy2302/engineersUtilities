import customtkinter as ctk
import darkdetect
from settings import *
from buttons import Button, ImageButton, NumButton, MathButton, MathImageButton
from PIL import Image

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        super().__init__(fg_color=(WHITE, BLACK))
        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        # self.resizable(False, False) #can be resized or not?
        self.title('Calculator')
        self.iconbitmap('E:/Python Projects Uni/engineersUtilities/assets/calculator.ico')
        self.title_bar_color(is_dark)

        # grid layout
        self.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform='a')
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform='a')

        # data
        self.result_string = ctk.StringVar(value='0')
        self.formula_string = ctk.StringVar(value='')
        self.display_nums = []
        self.full_operation = []

        # widgets
        self.create_widgets()

        self.mainloop()

    def create_widgets(self):
        # output labels
        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)

        OutputLabel(self, 0, 'SE', main_font, self.formula_string)  # formula
        OutputLabel(self, 1, 'E', result_font, self.result_string)  # result

        # clear AC button
        Button(
            parent=self,
            func=self.clear,
            text=OPERATORS['clear']['text'],
            col=OPERATORS['clear']['col'],
            row=OPERATORS['clear']['row'],
            font=main_font)

        # percentage Button
        Button(
            parent=self,
            func=self.percent,
            text=OPERATORS['percent']['text'],
            col=OPERATORS['percent']['col'],
            row=OPERATORS['percent']['row'],
            font=main_font)

        # invert button
        invert_image = ctk.CTkImage(
            light_image=Image.open(OPERATORS['invert']['image path']['dark']),
            dark_image=Image.open(OPERATORS['invert']['image path']['light'])
        )
        ImageButton(
            parent=self,
            text='',
            func=self.invert,
            col=OPERATORS['invert']['col'],
            row=OPERATORS['invert']['row'],
            image=invert_image
        )

        # number buttons
        for num, data in NUM_POSITIONS.items():
            NumButton(
                parent=self,
                text=num,
                func=self.num_press,
                col=data['col'],
                row=data['row'],
                font=main_font,
                span=data['span']
            )

        # math buttons
        for operator, data in MATH_POSITIONS.items():
            if data['image path']:
                divide_image=ctk.CTkImage(
                    light_image=Image.open(data['image path']['dark']),
                    dark_image=Image.open(data['image path']['light'])
                )

                MathImageButton(
                    parent=self,
                    operator=operator,
                    func=self.math_press,
                    col=data['col'],
                    row=data['row'],
                    image=divide_image
                )
            else:
                MathButton(parent=self,
                           text=data['character'],
                           operator=operator,
                           func=self.math_press,
                           col=data['col'],
                           row=data['row'],
                           font=main_font)

    def math_press(self, value):
        current_number = ''.join(self.display_nums)
        if current_number:
            self.full_operation.append(current_number)

            if value != '=':
                # update data
                self.full_operation.append(value)
                self.display_nums.clear()

                # update output
                self.result_string.set('')
                self.formula_string.set(' '.join(self.full_operation))

            else:
                formula = ' '.join(self.full_operation)
                result = eval(formula)

                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 3)

                self.full_operation.clear()
                self.display_nums = [str(result)]

                self.result_string.set(result)
                self.formula_string.set(formula)

    def num_press(self, value):
        self.display_nums.append(str(value))
        full_number = ''.join(self.display_nums)
        self.result_string.set(full_number)

    def invert(self):
        current_number = ''.join(self.display_nums)
        if current_number:
            if float(current_number) > 0:
                self.display_nums.insert(0, '-')
            else:
                del self.display_nums[0]

            self.result_string.set(''.join(self.display_nums))

    def percent(self):
        if self.display_nums:
            current_number = float(''.join(self.display_nums))
            percent_number = current_number / 100

            self.display_nums = list(str(percent_number))
            self.result_string.set(''.join(self.display_nums))

    def clear(self):
        self.result_string.set(0)
        self.formula_string.set('')
        self.display_nums.clear()
        self.full_operation.clear()

    def title_bar_color(self, is_dark):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_BAR_HEX_COLORS['dark'] if is_dark else TITLE_BAR_HEX_COLORS['light']
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            pass


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master=parent, font=font, textvariable=string_var)
        self.grid(column=0, columnspan=4, row=row, sticky=anchor, padx=10)


if __name__ == '__main__':
    Calculator(darkdetect.isDark())
