import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from datetime import datetime
import os
import json

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("500x500")
        self.root.configure(bg="#87CEEB")
        self.user_data = {}

        # Create the menu bar
        self.create_menu()

        # Create UI elements
        self.create_widgets()

        # Load existing data
        self.load_data()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        about_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About", command=self.show_about)

    def show_about(self):
        about_text = (
            "This is a simple BMI Calculator to calculate your Body Mass Index accurately & shows previously stored Visualize historical BMI data with graphs or charts in Analyze Trends.\n\n\n"
            "Created By Anurag Kumar\n"
            "Using Python Language."
        )
        messagebox.showinfo("About", about_text)

    def create_widgets(self):
        tk.Label(self.root, text="Enter your details below:", bg="#87CEEB", fg="#333333", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        tk.Label(self.root, text="User Name:", bg="#87CEEB", fg="#333333", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_name = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_name.grid(row=1, column=1, padx=10, pady=10)
        self.entry_name.bind("<Return>", lambda event: self.entry_weight.focus_set())

        tk.Label(self.root, text="Weight (kg):", bg="#87CEEB", fg="#333333", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_weight = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_weight.grid(row=2, column=1, padx=10, pady=10)
        self.entry_weight.bind("<Return>", lambda event: self.entry_height.focus_set())

        tk.Label(self.root, text="Height (m):", bg="#87CEEB", fg="#333333", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_height = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_height.grid(row=3, column=1, padx=10, pady=10)
        self.entry_height.bind("<Return>", lambda event: self.calculate_bmi())

        tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi, bg="#4caf50", fg="#ffffff", font=("Helvetica", 12)).grid(row=4, column=0, columnspan=2, pady=10)

        self.label_result = tk.Label(self.root, text="", bg="#87CEEB", fg="#333333", font=("Helvetica", 12))
        self.label_result.grid(row=5, column=0, columnspan=2, pady=10)

        tk.Button(self.root, text="View History", command=self.view_history, bg="#2196f3", fg="#ffffff", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Analyze Trends", command=self.analyze_trends, bg="#ff5722", fg="#ffffff", font=("Helvetica", 12)).grid(row=7, column=0, columnspan=2, pady=10)

        self.label_feedback = tk.Label(self.root, text="", bg="#87CEEB", fg="red", font=("Helvetica", 12))
        self.label_feedback.grid(row=8, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        name = self.entry_name.get()
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            bmi = weight / (height ** 2)
            category = self.classify_bmi(bmi)
            result_text = f"BMI: {bmi:.2f} ({category})"
            self.label_result.config(text=result_text)

            # Save data
            self.save_data(name, weight, height, bmi, category)

            # Provide positive feedback
            self.label_feedback.config(text="BMI calculated and data saved successfully!", fg="green")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid weight and height.")
            self.label_feedback.config(text="Error: Invalid input! Please enter numeric values.", fg="red")

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    def save_data(self, name, weight, height, bmi, category):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {"date": date, "weight": weight, "height": height, "bmi": bmi, "category": category}
        if name in self.user_data:
            self.user_data[name].append(entry)
        else:
            self.user_data[name] = [entry]
        with open("user_data.json", "w") as file:
            json.dump(self.user_data, file)

    def load_data(self):
        if os.path.exists("user_data.json"):
            with open("user_data.json", "r") as file:
                self.user_data = json.load(file)

    def view_history(self):
        name = self.entry_name.get()
        if name in self.user_data:
            history = self.user_data[name]
            history_text = "\n".join([f"{entry['date']}: BMI {entry['bmi']:.2f} ({entry['category']})" for entry in history])
            messagebox.showinfo("BMI History", history_text)
        else:
            messagebox.showinfo("No Data", "No history found for this user.")

    def analyze_trends(self):
        name = self.entry_name.get()
        if name in self.user_data:
            history = self.user_data[name]
            dates = [entry['date'] for entry in history]
            bmi_values = [entry['bmi'] for entry in history]
            plt.plot(dates, bmi_values, marker='o')
            plt.xlabel("Date")
            plt.ylabel("BMI")
            plt.title(f"BMI Trend for {name}")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            messagebox.showinfo("No Data", "No history found for this user.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
