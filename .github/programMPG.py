# David Stalmakov, 11/19/2025
# MPG Calculator
import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        # Create window and frame
        self.main_window = tk.Tk()
        self.main_window.title("MPG Calculator")
        self.main_window.geometry("400x400")

        self.top_frame = tk.Frame(self.main_window)
        self.middle_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Input Gallons
        self.gallons_label = tk.Label(self.top_frame, text="Gallons of gas in the car")
        self.gallons_entry = tk.Entry(self.top_frame)

        self.gallons_label.pack(side="left")
        self.gallons_entry.pack(side="left")

        # Input Miles
        self.miles_label = tk.Label(self.middle_frame, text="Miles the car can be driven on the amount of gas")
        self.miles_entry = tk.Entry(self.middle_frame)

        self.miles_label.pack(side="left")
        self.miles_entry.pack(side="left")

        # Create Button
        self.calc_button = tk.Button(self.bottom_frame, text="Calculate MPG", command=self.calculate_mpg)
        self.quit_button = tk.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)
        self.result_label = tk.Label(self.bottom_frame, text="MPG: ")

        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
        self.result_label.pack(side="left")

        # Pack frames
        self.top_frame.pack(side="top")
        self.middle_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        tk.mainloop()

    def calculate_mpg(self):
        try:
            gallons = float(self.gallons_entry.get())
            miles = float(self.miles_entry.get())

            mpg = miles / gallons
            self.result_label.config(text=f"MPG: {mpg:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

my_gui = MyGUI()


