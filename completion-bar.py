import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    for i in range(101):  # 0 to 100%
        progress_bar['value'] = i  # Update progress bar
        progress_label.config(text=f"Progress: {i}%")
        root.update_idletasks()  # Refresh UI
        time.sleep(0.03)  # Simulate work being done
    progress_label.config(text="Completed!")

# Create main window
root = tk.Tk()
root.title("Progress Bar Example")
root.geometry("350x200")
root.configure(bg="#f0f0f0")

# Create a styled progress bar
style = ttk.Style()
style.theme_use("clam")
style.configure("TProgressbar", thickness=20, troughcolor="#e0e0e0", background="#0078D7", troughrelief="flat", borderwidth=1)

progress_bar = ttk.Progressbar(root, length=300, mode='determinate', style="TProgressbar")
progress_bar.pack(pady=20)

# Create a progress label
progress_label = tk.Label(root, text="Progress: 0%", font=("Arial", 12), bg="#f0f0f0")
progress_label.pack()

# Start progress automatically
root.after(1000, start_progress)

# Run the application
root.mainloop()
