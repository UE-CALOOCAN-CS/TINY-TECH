import tkinter as tk
from tkinter import ttk

# Create the main window
win = tk.Tk()
win.geometry("850x500")
win.title("Modules Section")

# Sidebar Frame
sidebar = tk.Frame(win, width=200, bg="gray", height=500)
sidebar.place(x=0, y=0, width=200, height=500)

# Content Area with Scrollable Frame
content_frame = tk.Frame(win, bg="white", width=650, height=500)
content_frame.place(x=200, y=0, width=650, height=500)

canvas = tk.Canvas(content_frame, bg="white", width=650, height=450)
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

canvas.place(x=0, y=50, width=630, height=450)  # Adjusted to leave room for deadspace
scrollbar.place(x=630, y=50, height=450)

# Deadspace to show the previous module
deadspace = tk.Label(
    content_frame,
    text="Select a module",  # Initial text
    font=("Arial", 12, "italic"),
    bg="lightgray",
    fg="black",
    anchor="center",
    relief="sunken",
)
deadspace.place(x=0, y=0, width=650, height=50)  # Positioned at the top of content area

# Label to show module description
module_label = tk.Label(scrollable_frame, text="Select a module to view details", font=("Arial", 14), wraplength=600, bg="white", bd=0, justify="center", anchor="center")
module_label.pack(pady=10, padx=10, fill="both", expand=True)

# Variable to keep track of the last module
last_viewed_module = [None]  # Using a mutable list to maintain state between function calls

# Function to update content area and deadspace
def show_module(module_name, description):
    # Update the deadspace to show the *previous module*
    if last_viewed_module[0]:
        deadspace.config(text=f"Last viewed: {last_viewed_module[0]}")
    else:
        deadspace.config(text="Select a module")

    # Update the current module details
    module_label.config(text=f"{module_name}\n\n{description}")

    # Set the current module as the last viewed module
    last_viewed_module[0] = module_name

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
modules_label.place(x=60, y=5, width=120, height=30)

# Modules Data
modules = [
    ("Module 1", "This is the description for Module 1. " * 10),
    ("Module 2", "This is the description for Module 2. " * 15),
    ("Module 3", "This is the description for Module 3. " * 20),
]

# Buttons for Modules
for index, (module_name, description) in enumerate(modules):
    btn = tk.Button(sidebar, text=module_name, command=lambda m=module_name, d=description: show_module(m, d), bg="lightgray")
    btn.place(x=10, y=50 + (index * 40), width=180, height=30)

win.mainloop()
