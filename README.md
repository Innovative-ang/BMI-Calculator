# BMI Calculator

This is a simple Body Mass Index (BMI) Calculator built using Python. The calculator takes user inputs for weight and height and then calculates and displays the BMI.

## Requirements

- Python 3.6 or higher is required.
- `pip install tkinter`
- `pip install numpy`

## Usage

1. Clone this repository to your local machine.
2. Install the necessary dependencies using the `Requirements` section above.
3. Run the `bmi_calculator.py` script to start the BMI Calculator.

## Features

- User-friendly interface to input weight and height.
- Real-time BMI calculation based on the inputs provided.
- Categorizes the BMI result into Underweight, Normal weight, Overweight, and Obese.

## Example Code

Here is a basic example of how the BMI Calculator works:

```python
import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    weight = float(entry_weight.get())
    height = float(entry_height.get()) / 100
    bmi = weight / (height * height)
    messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")

# Create and place the widgets
tk.Label(window, text="Weight (kg):").grid(row=0, column=0)
entry_weight = tk.Entry(window)
entry_weight.grid(row=0, column=1)

tk.Label(window, text="Height (cm):").grid(row=1, column=0)
entry_height = tk.Entry(window)
entry_height.grid(row=1, column=1)

tk.Button(window, text="Calculate", command=calculate_bmi).grid(row=2, columnspan=2)

# Start the Tkinter event loop
window.mainloop()
