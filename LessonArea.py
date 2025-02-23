import tkinter as tk
from tkinter import ttk, scrolledtext
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to enable 'Continue' button when solution is submitted
def submit_solution():
    continue_btn.config(state=tk.NORMAL)

def run_code():
    output_text.insert(tk.END, "Running code...\n")  # Placeholder for execution

# Create Main Tkinter Window
root = tk.Tk()
root.title("Exercise Interface")
root.geometry("900x600")
root.configure(bg="#f0f0f0")

# Left Panel (Exercise and Instructions)
left_frame = tk.Frame(root, width=300, height=600, bg="white", padx=10, pady=10)
left_frame.place(x=0, y=0)

exercise_label = tk.Label(left_frame, text="EXERCISE", font=("Arial", 14, "bold"), bg="white")
exercise_label.place(x=10, y=10)

exercise_desc = tk.Label(left_frame, text="Encoding time by color\n\nDescription of the exercise goes here.", wraplength=280, justify="left", bg="white")
exercise_desc.place(x=10, y=40)

instruction_label = tk.Label(left_frame, text="INSTRUCTIONS", font=("Arial", 12, "bold"), bg="white")
instruction_label.place(x=10, y=100)

instructions = tk.Label(left_frame, text="1. Follow the instructions here.\n2. Implement your solution in the coding area.\n3. Submit a valid solution to enable Continue.", wraplength=280, justify="left", bg="white")
instructions.place(x=10, y=130)

# Right Panel (Coding Area & Output)
right_frame = tk.Frame(root, width=600, height=600, bg="#f7f7f7", padx=10, pady=10)
right_frame.place(x=300, y=0)

# Coding Area
code_label = tk.Label(right_frame, text="Code Editor", font=("Arial", 12, "bold"), bg="#f7f7f7")
code_label.place(x=10, y=10)

code_input = scrolledtext.ScrolledText(right_frame, height=8, width=70)
code_input.place(x=10, y=40)

# Buttons
run_btn = tk.Button(right_frame, text="Run Code", command=run_code)
run_btn.place(x=10, y=190)

submit_btn = tk.Button(right_frame, text="Submit Answer", command=submit_solution)
submit_btn.place(x=90, y=190)

continue_btn = tk.Button(right_frame, text="Continue", state=tk.DISABLED)
continue_btn.place(x=200, y=190)

# Output Terminal
output_label = tk.Label(right_frame, text="Output:", font=("Arial", 12, "bold"), bg="#f7f7f7")
output_label.place(x=10, y=230)

output_text = scrolledtext.ScrolledText(right_frame, height=10, width=70)
output_text.place(x=10, y=260)

# Run Tkinter Main Loop
root.mainloop()
