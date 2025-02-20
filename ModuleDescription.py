import tkinter as tk
from tkinter import ttk

# Create the main window
win = tk.Tk()
win.geometry("850x500")
win.title("Modules Section")

# Sidebar Frame
sidebar = tk.Frame(win, width=200, bg="gray", height=500)  # Increased width to fit "MODULES"
sidebar.place(x=0, y=0, width=200, height=500)

# Content Area with Scrollable Frame
content_frame = tk.Frame(win, bg="white", width=650, height=500)
content_frame.place(x=200, y=0, width=650, height=500)

canvas = tk.Canvas(content_frame, bg="white", width=650, height=500)
scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="white")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.place(x=0, y=0, width=630, height=500)
scrollbar.place(x=630, y=0, height=500)

# Label to show module description
module_label = tk.Label(scrollable_frame, text="Select a module to view details", font=("Arial", 14), wraplength=600, bg="white", bd=0, justify="center", anchor="center")
module_label.pack(pady=10, padx=10, fill="both", expand=True)

# Function to update content area
def show_module(module_name, description):
    module_label.config(text=f"{module_name}\n\n{description}")

# Function to toggle sidebar visibility
def toggle_sidebar():
    global sidebar_visible
    if sidebar_visible:
        sidebar.place_forget()
    else:
        sidebar.place(x=0, y=0, width=200, height=500)
    sidebar_visible = not sidebar_visible

sidebar_visible = True

# Hamburger Button
hamburger_btn = tk.Button(win, text="☰", font=("Arial", 14), command=toggle_sidebar, bg="lightgray")
hamburger_btn.place(x=5, y=5, width=40, height=30)

# Modules Label
modules_label = tk.Label(win, text="MODULES", font=("Arial", 14, "bold"), bg="lightgray")
modules_label.place(x=60, y=5, width=120, height=30)  # Adjusted width to fit text

# Modules Data
modules = [
    ("Module 1", "This is the description for Module 1. " * 10),
    ("Module 2", "This is the description for Module 2. " * 15),
    ("Module 3", "This is the description for Module 3. " * 20),
]

# Buttons for Modules
for index, (module_name, description) in enumerate(modules):
    btn = tk.Button(sidebar, text=module_name, command=lambda m=module_name, d=description: show_module(m, d), bg="lightgray")
    btn.place(x=10, y=50 + (index * 40), width=180, height=30)  # Adjusted width

win.mainloop()
