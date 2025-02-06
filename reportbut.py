import tkinter as tk
from tkinter import messagebox

def submit_report():
    name = name_entry.get()
    email = email_entry.get()
    report = report_entry.get("1.0", tk.END)
    # You can process the report data here
    messagebox.showinfo("Report Submitted", "Thank you for your report!")

# Create the main window
root = tk.Tk()
root.title("Bug Report")

# Create and place the labels and text boxes
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Report:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.NW)
report_entry = tk.Text(root, height=10, width=40)
report_entry.grid(row=2, column=1, padx=10, pady=5)

# Create and place the Submit button
submit_button = tk.Button(root, text="Submit", command=submit_report)
submit_button.grid(row=3, column=1, padx=10, pady=10, sticky=tk.E)

# Run the main loop
root.mainloop()
