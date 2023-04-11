import customtkinter as ctk


class InDevFeatures(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Define the data for the table
        self.data = [
            ["Feature", "Version Value", "Completed"],
            ["Calculator", "1", "True"],
            ["Scientific", "2", "False"],
            ["Programmer", "3", "True"],
            ["Data Calc", "4", "False"],
            ["Graphic", "5", "False"],
            ["Data", "6", "False"],
            ["Distances", "7", "True"],
            ["Weight", "8", "False"],
            ["Currency", "9", "False"],
            ["Volume", "10", "True"],
            ["Temperature", "11", "True"],
            ["Energy", "12", "False"],
            ["Area", "13", "False"],
            ["Speed", "14", "False"],
            ["Time", "15", "False"],
            ["Power", "16", "False"],
            ["Pressure", "17", "False"],
            ["Angle", "18", "False"],
            ["Frequency", "19", "False"],
            ["Info Tab", "20", "False"],
            ["PC Statistics", "90", "False"],
            ["Macros Tab", "700", "False"],
            ["Current Version", " X ", ""],
        ]

        # Calculate the sum of "Version Value" for rows with "True" in the third column
        current_version = sum(int(row[1]) for row in self.data[1:-1] if row[2] == "True")
        vcs_version = 'v0.' + str(current_version)
        # Update the "Current Version" row with the calculated sum
        self.data[-1][1] = vcs_version

        # Define the dimensions of the table
        self.num_rows = len(self.data)
        self.num_cols = len(self.data[0])

        # Create the root window
        self.title('In Development features')
        self.geometry('450x450')

        # Create a frame to contain the canvas and scrollbar
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill=ctk.BOTH, expand=True)

        # Create a canvas to contain the table
        self.canvas = ctk.CTkCanvas(self.frame)
        self.canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

        # Create a frame to hold the table contents
        self.table_frame = ctk.CTkFrame(self.canvas)

        # Add the table frame to the canvas
        self.canvas.create_window((0, 0), window=self.table_frame, anchor=ctk.NW)

        # Create CTkLabel and CTkFrame widgets to display the data in a grid
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                cell_frame = ctk.CTkFrame(self.table_frame)
                cell_frame.grid(row=i, column=j, padx=1, pady=1)
                label = ctk.CTkLabel(cell_frame, text=self.data[i][j], width=30, font=('Montserrat', 20))
                label.pack()

        # Create a scrollbar for the canvas
        self.scrollbar = ctk.CTkScrollbar(self.frame, command=self.canvas.yview)
        self.scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

        # Connect the scrollbar to the canvas
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # Bind mousewheel scrolling to the canvas
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        # Set the size of the canvas scroll region
        self.table_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(ctk.ALL))

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * int(event.delta / 120), "units")


def open_indev_features():
    InDevFeatures().mainloop()


if __name__ == '__main__':
    open_indev_features()

