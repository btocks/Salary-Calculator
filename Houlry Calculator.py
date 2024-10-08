import tkinter as tk

def calculate_hourly_pay():
    try:
        salary = float(salary_entry.get())
        hourly_pay = salary / 2080
        result_label.config(text=f"Hourly Pay: ${hourly_pay:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid salary")
        
def calculate_salary_pay():
    try:
        hourly = float(hourly_entry.get())
        salary_pay = hourly * 2080
        result_label.config(text=f"Salary Pay: ${salary_pay:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid hourly pay")

# Create main window
root = tk.Tk()
root.title("Hourly & Salary Pay Calculator")

# Create input field for salary
salary_label = tk.Label(root, text="Enter Salary:")
salary_label.pack()
salary_entry = tk.Entry(root)
salary_entry.pack()

# Button to calculate hourly pay
calculate_button = tk.Button(root, text="Calculate Hourly Pay", command=calculate_hourly_pay)
calculate_button.pack()

# Create input field for hourly pay
hourly_label = tk.Label(root, text="Enter Hourly Pay:")
hourly_label.pack()
hourly_entry = tk.Entry(root)
hourly_entry.pack()

# Button to calculate salary pay
calculate_button = tk.Button(root, text="Calculate Annual Salary", command=calculate_salary_pay)
calculate_button.pack()

# Display result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
