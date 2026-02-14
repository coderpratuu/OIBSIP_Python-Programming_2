import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

# ================= DATABASE SETUP =================
conn = sqlite3.connect("bmi_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bmi_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    weight REAL,
    height REAL,
    bmi REAL,
    date TEXT
)
""")
conn.commit()

# ================= BMI FUNCTIONS =================
def calculate_bmi():
    try:
        name = entry_name.get()
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        category = categorize_bmi(bmi)

        result_label.config(
            text=f"BMI: {bmi}\nCategory: {category}",
            fg=get_color(category)
        )

        save_data(name, weight, height, bmi)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid positive numbers.")

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_color(category):
    colors = {
        "Underweight": "#3498db",
        "Normal Weight": "#2ecc71",
        "Overweight": "#f1c40f",
        "Obese": "#e74c3c"
    }
    return colors.get(category, "black")

# ================= DATA FUNCTIONS =================
def save_data(name, weight, height, bmi):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO bmi_records (name, weight, height, bmi, date) VALUES (?, ?, ?, ?, ?)",
        (name, weight, height, bmi, date)
    )
    conn.commit()

def view_history():
    cursor.execute("SELECT name, bmi, date FROM bmi_records")
    records = cursor.fetchall()

    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    history_window.geometry("400x300")

    text_area = tk.Text(history_window)
    text_area.pack(fill="both", expand=True)

    for record in records:
        text_area.insert(tk.END, f"Name: {record[0]} | BMI: {record[1]} | Date: {record[2]}\n")

def show_graph():
    cursor.execute("SELECT bmi, date FROM bmi_records ORDER BY date")
    data = cursor.fetchall()

    if not data:
        messagebox.showinfo("No Data", "No BMI records to display.")
        return

    bmi_values = [row[0] for row in data]
    dates = [row[1] for row in data]

    plt.figure()
    plt.plot(dates, bmi_values, marker='o')
    plt.xticks(rotation=45)
    plt.title("BMI Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.tight_layout()
    plt.show()

# ================= GUI DESIGN =================
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x450")
root.configure(bg="#1e272e")

title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Helvetica", 20, "bold"),
    bg="#1e272e",
    fg="#ffffff"
)
title_label.pack(pady=20)

frame = tk.Frame(root, bg="#485460", padx=20, pady=20)
frame.pack(pady=10)

tk.Label(frame, text="Name:", bg="#485460", fg="white").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Weight (kg):", bg="#485460", fg="white").grid(row=1, column=0, sticky="w")
entry_weight = tk.Entry(frame)
entry_weight.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Height (m):", bg="#485460", fg="white").grid(row=2, column=0, sticky="w")
entry_height = tk.Entry(frame)
entry_height.grid(row=2, column=1, pady=5)

tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="#00a8ff",
    fg="white",
    padx=10,
    pady=5
).pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 14, "bold"),
    bg="#1e272e"
)
result_label.pack(pady=10)

tk.Button(
    root,
    text="View History",
    command=view_history,
    bg="#9c88ff",
    fg="white",
    padx=10,
    pady=5
).pack(pady=5)

tk.Button(
    root,
    text="Show BMI Trend",
    command=show_graph,
    bg="#4cd137",
    fg="white",
    padx=10,
    pady=5
).pack(pady=5)

root.mainloop()
