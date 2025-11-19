# David Stalmakov, 11/19/2025
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk


class MyGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.title("Long-Distance Call Calculator")
        self.main_window.geometry("400x400")

        self.rate_var = tk.StringVar(value="Daytime")

        # Create a label for rate selection
        self.label_rate = tk.Label(self.main_window, text="Select Rate: ")
        self.label_rate.pack(padx=5, pady=5)

        # Create radio buttons
        self.radio_daytime = tk.Radiobutton(self.main_window, text="Daytime (6:00 A.M. - 5:59 P.M.) $0.02/min", variable=self.rate_var, value="Daytime")
        self.radio_daytime.pack(padx=5, pady=5)

        self.radio_evening = tk.Radiobutton(self.main_window, text="Evening (6:00 P.M. - 11:59 P.M.) $0.12/min", variable=self.rate_var, value="Evening")
        self.radio_evening.pack(padx=5, pady=5)

        self.radio_off_peak = tk.Radiobutton(self.main_window, text="Off-Peak (12:00 A.M. - 5:59 A.M.) $0.05/min", variable=self.rate_var, value="Off-Peak")
        self.radio_off_peak.pack(padx=5, pady=5)

        # Create a label and entry for the number of minutes
        self.label_minutes = tk.Label(self.main_window, text="Enter number of minutes:")
        self.label_minutes.pack(pady=10)

        self.entry_minutes = tk.Entry(self.main_window)
        self.entry_minutes.pack()

        # Calculate Button
        self.calc_button = tk.Button(self.main_window, text="Calculate Charge", command=self.calculate_charge)
        self.calc_button.pack(padx=5, pady=5)

        self.main_window.mainloop()

    def calculate_charge(self):
        try:
            minutes = float(self.entry_minutes.get())
            # Determine the rate based on the selected category
            rate_category = self.rate_var.get()
            if rate_category == "Daytime":
                rate = 0.02
            elif rate_category == "Evening":
                rate = 0.12
            elif rate_category == "Off-Peak":
                rate = 0.05
            else:
                tk.messagebox.showerror("Error", "Please select a rate category.")
                return
            # Calculate the Charge
            charge = minutes * rate

            # Display the charge
            tk.messagebox.showinfo("Charge", f"The charge for your call is ${charge:.2f}")
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid number.")

my_gui = MyGUI()