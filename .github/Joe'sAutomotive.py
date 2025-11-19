# David Stalmakov, 11/19/2025
# Joe's Automotive

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk


class MyGUI:
    def __init__(self):
        # Main Window
        self.main_window = tk.Tk()
        self.main_window.title("Joe's Automotive")
        self.main_window.geometry("400x400")

        # Frame for Check buttons
        self.cb_frame = ttk.Frame(self.main_window)
        self.bottom_frame = ttk.Frame(self.main_window)

        # Options
        self.service = {"Oil Change": 30.00, "Lube Job": 20.00, "Radiator Flush": 40.00, "Transmission Fluid": 100.00,
            "Inspection": 35.00, "Muffler Replacement": 200.00, "Tire Rotation": 20.00 }

        # Create IntVar for every check box
        self.cb_vars = {}
        for service, price in self.service.items():
            var = tk.IntVar()
            cb = ttk.Checkbutton(self.cb_frame, text=f"{service} - ${price:.2f}", variable=var)
            cb.pack()
            self.cb_vars[service] = var

        # Buttons
        self.calc_button = ttk.Button(self.bottom_frame, text="Calculate Total",command=self.calculate_total)
        self.quit_button = ttk.Button(self.bottom_frame, text="Quit",command=self.main_window.destroy)
        self.total_label = ttk.Label(self.bottom_frame, text="Total: $0.00")

        # Pack
        self.cb_frame.pack(side="top")
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
        self.total_label.pack(side="left")
        self.bottom_frame.pack(side="top")

        tk.mainloop()
    def calculate_total(self):
        total = 0
        for service, var in self.cb_vars.items():
            if var.get() == 1:
                total += self.service[service]
        self.total_label.config(text=f"{total:.2f}")

my_gui = MyGUI()
