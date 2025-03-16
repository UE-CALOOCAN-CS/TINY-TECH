import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Activity Area")
root.geometry("1000x600")
root.configure(bg="#f0f0f0")

# Left panel
left_frame = tk.Frame(root, width=300, height=600, bg="#d9d9d9")
left_frame.place(x=0, y=0, width=300, height=600)

# Separator line between left and center
tk.Frame(root, bg="#000000", width=2, height=600).place(x=300, y=0)

# Upper section (Heading)
left_upper = tk.Frame(left_frame, bg="#d9d9d9")
left_upper.place(x=0, y=0, width=300, height=300)
heading_label = tk.Label(left_upper, text="Heading", font=("Arial", 12, "bold"), bg="#d9d9d9")
heading_label.pack(anchor="w", padx=10, pady=5)
text_label = tk.Label(left_upper, text="Lorem ipsum dolor sit amet...", wraplength=270, bg="#d9d9d9")
text_label.pack(anchor="w", padx=10)

# Separator line between upper and lower section in left panel
tk.Frame(left_frame, bg="#000000", width=300, height=2).place(x=0, y=300)

# Lower section (Instructions)
left_lower = tk.Frame(left_frame, bg="#d9d9d9")
left_lower.place(x=0, y=302, width=300, height=298)
instructions_label = tk.Label(left_lower, text="INSTRUCTIONS", font=("Arial", 10, "bold"), bg="#d9d9d9")
instructions_label.pack(anchor="w", padx=10, pady=10)
instructions_text = tk.Label(left_lower, text="Heading\nLorem ipsum dolor sit amet...", wraplength=270, bg="#d9d9d9")
instructions_text.pack(anchor="w", padx=10)

# Radio Buttons
answer_var = tk.StringVar()
for i in range(1, 4):
    tk.Radiobutton(left_lower, text=f"ANSWER {i}", variable=answer_var, value=f"Answer {i}", bg="#d9d9d9").pack(anchor="w", padx=20)

# Submit Button
submit_button = tk.Button(left_lower, text="SUBMIT", bg="#4CAF50", fg="white", padx=10, pady=5)
submit_button.pack(pady=10)

# Center panel (Empty)
center_frame = tk.Frame(root, width=300, height=600, bg="#ffffff")
center_frame.place(x=302, y=0, width=300, height=600)

# Separator line between center and right
tk.Frame(root, bg="#000000", width=2, height=600).place(x=602, y=0)

# Right panel
right_frame = tk.Frame(root, width=396, height=600, bg="#ffffff")
right_frame.place(x=604, y=0, width=396, height=600)

# Upper section (View Source & Run Code)
right_upper = tk.Frame(right_frame, bg="#ffffff")
right_upper.place(x=0, y=0, width=396, height=300)
view_button = tk.Button(right_upper, text="VIEW SOURCE", bg="#008CBA", fg="white", padx=10, pady=5)
view_button.place(x=283, y=10)
run_button = tk.Button(right_upper, text="RUN CODE", bg="#008CBA", fg="white", padx=10, pady=5)
run_button.place(x=295, y=250)

# Separator line between upper and lower section in right panel
tk.Frame(right_frame, bg="#000000", width=396, height=2).place(x=0, y=300)

# Lower section (Clear Screen Button)
right_lower = tk.Frame(right_frame, bg="#ffffff")
right_lower.place(x=0, y=302, width=396, height=298)
clear_button = tk.Button(right_lower, text="CLEAR SCREEN", bg="#f44336", fg="white", padx=10, pady=5)
clear_button.place(x=270, y=250)

# Run main loop
root.mainloop()
