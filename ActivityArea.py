import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Activity Area")
root.geometry("1920x1080")
root.configure(bg="#f0f0f0")

# ========== LEFT PANEL ==========
left_frame = tk.Frame(root, width=400, height=793, bg="#d9d9d9")
left_frame.place(x=0, y=0, width=400, height=793)

# Separator line between left and center
tk.Frame(root, bg="#000000", width=2, height=793).place(x=400, y=0)

# Upper section (Heading) - Scrollable
left_upper = tk.Frame(left_frame, bg="#d9d9d9")
left_upper.place(x=0, y=10, width=400, height=377)

# Create canvas and scrollbar for upper section
upper_canvas = tk.Canvas(left_upper, bg="#d9d9d9", width=380, height=377, highlightthickness=0)
upper_scrollbar = tk.Scrollbar(left_upper, orient="vertical", command=upper_canvas.yview)
upper_scrollable_frame = tk.Frame(upper_canvas, bg="#d9d9d9")

upper_scrollable_frame.bind(
    "<Configure>",
    lambda e: upper_canvas.configure(scrollregion=upper_canvas.bbox("all"))
)

upper_canvas.create_window((0, 0), window=upper_scrollable_frame, anchor="nw", width=380)
upper_canvas.configure(yscrollcommand=upper_scrollbar.set)

upper_canvas.pack(side="left", fill="both", expand=True)
upper_scrollbar.pack(side="right", fill="y")

# Add content to upper scrollable frame
heading_label = tk.Label(upper_scrollable_frame, text="Heading", font=("Arial", 12, "bold"), bg="#d9d9d9")
heading_label.pack(anchor="w", padx=10, pady=5)
text_label = tk.Label(upper_scrollable_frame, text="Lorem ipsum dolor sit amet...", wraplength=270, bg="#d9d9d9")
text_label.pack(anchor="w", padx=10)

# Separator line between upper and lower section in left panel
tk.Frame(left_frame, bg="#000000", width=400, height=2).place(x=0, y=387)

# Lower section (Instructions) - Scrollable
left_lower = tk.Frame(left_frame, bg="#d9d9d9")
left_lower.place(x=0, y=390, width=400, height=403)

# Create canvas and scrollbar for lower section
lower_canvas = tk.Canvas(left_lower, bg="#d9d9d9", width=380, height=403, highlightthickness=0)
lower_scrollbar = tk.Scrollbar(left_lower, orient="vertical", command=lower_canvas.yview)
lower_scrollable_frame = tk.Frame(lower_canvas, bg="#d9d9d9")

lower_scrollable_frame.bind(
    "<Configure>",
    lambda e: lower_canvas.configure(scrollregion=lower_canvas.bbox("all"))
)

lower_canvas.create_window((0, 0), window=lower_scrollable_frame, anchor="nw", width=380)
lower_canvas.configure(yscrollcommand=lower_scrollbar.set)

lower_canvas.pack(side="left", fill="both", expand=True)
lower_scrollbar.pack(side="right", fill="y")

# Add content to lower scrollable frame
instructions_label = tk.Label(lower_scrollable_frame, text="INSTRUCTIONS", font=("Arial", 12, "bold"), bg="#d9d9d9")
instructions_label.pack(anchor="w", padx=10, pady=10)
instructions_text = tk.Label(lower_scrollable_frame, text="Heading\nLorem ipsum dolor sit amet...", wraplength=270, bg="#d9d9d9")
instructions_text.pack(anchor="w", padx=10)

# Radio Buttons
answer_var = tk.StringVar()
for i in range(1, 4):
    tk.Radiobutton(lower_scrollable_frame, text=f"ANSWER {i}", variable=answer_var, value=f"Answer {i}", bg="#d9d9d9").pack(anchor="w", padx=20)

# Submit Button
submit_frame = tk.Frame(lower_scrollable_frame, bg="#d9d9d9")
submit_frame.pack(fill="x", pady=(100, 10))
submit_button = tk.Button(submit_frame, text="SUBMIT", bg="#4CAF50", fg="white", padx=15, pady=5)
submit_button.pack(expand=True)

# ========== CENTER PANEL (UNCHANGED) ==========
center_frame = tk.Frame(root, width=600, height=793, bg="#ffffff")
center_frame.place(x=402, y=0, width=600, height=793)

# Create canvas with scrollbar
center_canvas = tk.Canvas(center_frame, bg="#ffffff", highlightthickness=0)
center_scrollbar = tk.Scrollbar(center_frame, orient="vertical", command=center_canvas.yview)

# Pack them to make scrollbar fill height
center_canvas.pack(side="left", fill="both", expand=True)
center_scrollbar.pack(side="right", fill="y")

# Configure canvas scrolling
center_canvas.configure(yscrollcommand=center_scrollbar.set)

# Create scrollable frame INSIDE canvas
center_scrollable_frame = tk.Frame(center_canvas, bg="#ffffff")
center_canvas.create_window((0, 0), window=center_scrollable_frame, anchor="nw", width=600)

# Update scrollregion when frame size changes
def update_scrollregion(event):
    center_canvas.configure(scrollregion=center_canvas.bbox("all"))
center_scrollable_frame.bind("<Configure>", update_scrollregion)

# Add sample content (replace with your actual content)
for i in range(1, 21):
    tk.Label(center_scrollable_frame, 
            text=f"Content item {i}\nSample text to demonstrate scrolling", 
            bg="#ffffff", wraplength=550).pack(pady=5, padx=10, anchor="w")

# Mouse wheel handling for center panel only when hovered
def _on_mousewheel(event):
    center_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def _bind_mousewheel(event):
    center_canvas.bind_all("<MouseWheel>", _on_mousewheel)

def _unbind_mousewheel(event):
    center_canvas.unbind_all("<MouseWheel>")

center_canvas.bind("<Enter>", _bind_mousewheel)
center_canvas.bind("<Leave>", _unbind_mousewheel)

# ========== RIGHT PANEL (WITH ADDED SAMPLE CONTENT) ==========
# Separator line between center and right
tk.Frame(root, bg="#000000", width=2, height=793).place(x=802, y=0)

right_frame = tk.Frame(root, width=929, height=793, bg="#ffffff")
right_frame.place(x=804, y=0, width=929, height=793)

# Right Upper Section - Scrollable with fixed buttons
right_upper_container = tk.Frame(right_frame, bg="#ffffff")
right_upper_container.place(x=0, y=0, width=929, height=387)

# Create main frame that will contain both canvas and button frame
right_upper_main = tk.Frame(right_upper_container, bg="#ffffff")
right_upper_main.pack(fill="both", expand=True)

# Create canvas and scrollbar
right_upper_canvas = tk.Canvas(right_upper_main, bg="#ffffff", highlightthickness=0)
right_upper_scrollbar = tk.Scrollbar(right_upper_main, orient="vertical", command=right_upper_canvas.yview)
right_upper_scrollable_frame = tk.Frame(right_upper_canvas, bg="#ffffff")

right_upper_scrollable_frame.bind(
    "<Configure>",
    lambda e: right_upper_canvas.configure(scrollregion=right_upper_canvas.bbox("all"))
)

right_upper_canvas.create_window((0, 0), window=right_upper_scrollable_frame, anchor="nw", width=929)
right_upper_canvas.configure(yscrollcommand=right_upper_scrollbar.set)

right_upper_canvas.pack(side="left", fill="both", expand=True)
right_upper_scrollbar.pack(side="right", fill="y")

for i in range(1, 21):
    tk.Label(right_upper_scrollable_frame, 
            text=f"Sample content item {i}\nThis demonstrates the scrolling functionality in the upper right panel", 
            bg="#ffffff", wraplength=700).pack(pady=5, padx=10, anchor="w")

# Create separate frame for buttons (not part of scrollable content)
button_frame = tk.Frame(right_upper_container, bg="#ffffff")
button_frame.place(x=600, y=20, width=200, height=350)  # Same position as original

view_button = tk.Button(button_frame, text="VIEW SOURCE", bg="#008CBA", fg="white", padx=10, pady=5)
view_button.pack(anchor='nw', padx=5, pady=10)
run_button = tk.Button(button_frame, text="RUN CODE", bg="#008CBA", fg="white", padx=10, pady=5)
run_button.pack(anchor='sw', side='bottom', padx=10, pady=10)  # Bottom-left position

# Mouse wheel support for upper right
def _on_mousewheel_upper_right(event):
    right_upper_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def _bind_mousewheel_upper_right(event):
    right_upper_canvas.bind_all("<MouseWheel>", _on_mousewheel_upper_right)

def _unbind_mousewheel_upper_right(event):
    right_upper_canvas.unbind_all("<MouseWheel>")

right_upper_canvas.bind("<Enter>", _bind_mousewheel_upper_right)
right_upper_canvas.bind("<Leave>", _unbind_mousewheel_upper_right)

# Separator line between upper and lower section in right panel
tk.Frame(right_frame, bg="#000000", width=929, height=2).place(x=0, y=387)

# Right Lower Section - Scrollable with fixed button
right_lower_container = tk.Frame(right_frame, bg="#ffffff")
right_lower_container.place(x=0, y=389, width=929, height=404)

# Create main frame that will contain both canvas and button frame
right_lower_main = tk.Frame(right_lower_container, bg="#ffffff")
right_lower_main.pack(fill="both", expand=True)

# Create canvas and scrollbar
right_lower_canvas = tk.Canvas(right_lower_main, bg="#ffffff", highlightthickness=0)
right_lower_scrollbar = tk.Scrollbar(right_lower_main, orient="vertical", command=right_lower_canvas.yview)
right_lower_scrollable_frame = tk.Frame(right_lower_canvas, bg="#ffffff")

right_lower_scrollable_frame.bind(
    "<Configure>",
    lambda e: right_lower_canvas.configure(scrollregion=right_lower_canvas.bbox("all"))
)

right_lower_canvas.create_window((0, 0), window=right_lower_scrollable_frame, anchor="nw", width=929)
right_lower_canvas.configure(yscrollcommand=right_lower_scrollbar.set)

right_lower_canvas.pack(side="left", fill="both", expand=True)
right_lower_scrollbar.pack(side="right", fill="y")

for i in range(1, 31):
    tk.Label(right_lower_scrollable_frame, 
            text=f"Sample output line {i}: This demonstrates the scrolling functionality in the lower right panel", 
            bg="#ffffff", wraplength=700).pack(pady=2, padx=10, anchor="w")

# Create separate frame for clear button (not part of scrollable content)
clear_button_frame = tk.Frame(right_lower_container, bg="#ffffff")
clear_button_frame.place(x=600, y=350, width=200, height=50)  # Same position as original

clear_button = tk.Button(clear_button_frame, text="CLEAR SCREEN", bg="#f44336", fg="white", padx=10, pady=5)
clear_button.pack(anchor='w', side='left', padx=1, pady=5)

# Mouse wheel support for lower right
def _on_mousewheel_lower_right(event):
    right_lower_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def _bind_mousewheel_lower_right(event):
    right_lower_canvas.bind_all("<MouseWheel>", _on_mousewheel_lower_right)

def _unbind_mousewheel_lower_right(event):
    right_lower_canvas.unbind_all("<MouseWheel>")

right_lower_canvas.bind("<Enter>", _bind_mousewheel_lower_right)
right_lower_canvas.bind("<Leave>", _unbind_mousewheel_lower_right)

# Run main loop
root.mainloop()
