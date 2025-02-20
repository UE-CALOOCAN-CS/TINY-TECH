import tkinter as tk
import webbrowser
from PIL import Image, ImageTk  # Import Pillow for image handling

def toggle_menu():
    if main_menu.winfo_ismapped():
        main_menu.place_forget()
        module_menu.place(x=0, y=40, width=150, height=765)
    else:
        module_menu.place_forget()
        main_menu.place(x=0, y=40, width=150, height=765)

def open_module_1():
    webbrowser.open("https://www.tiktok.com/@parenghayb")

def show_module(module_name):
    for frame in module_frames.values():
        frame.place_forget()
    module_frames[module_name].place(x=160, y=50, width=1290, height=900)

def logout():
    root.quit()

root = tk.Tk()
root.title("Module")
root.geometry("1300x950")

menu_button = tk.Button(root, text="☰", font=("Arial", 14), command=toggle_menu)
menu_button.place(x=5, y=5)

main_menu = tk.Frame(root, bg="lightgray", relief="raised")
module_menu = tk.Frame(root, bg="lightgray", relief="raised")

button_frame = tk.Frame(main_menu, bg="lightgray")
button_frame.pack(fill="both", expand=True)

main_items = [
    ("Home", lambda: print("Home Clicked")),
    ("Profile", lambda: print("Profile Clicked")),
    ("Settings", lambda: print("Settings Clicked")),
]

for text, command in main_items:
    btn = tk.Button(button_frame, text=text, font=("Arial", 12), width=15, relief="flat", bg="white", command=command)
    btn.pack(pady=5, padx=5, fill="x")

logout_button = tk.Button(main_menu, text="Logout", font=("Arial", 12), width=15, relief="flat", bg="white", command=logout)
logout_button.pack(side="bottom", pady=50)

module_frames = {}

module1_frame = tk.Frame(root, bg="white", relief="solid")
module1_label = tk.Label(module1_frame, text="Module 1 Content", font=("Arial", 18), bg="white")
module1_label.pack(pady=20)

module1_subheading = tk.Label(
    module1_frame, 
    text=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse enim arcu, "
          "iaculis at pulvinar quis, suscipit tincidunt tortor. Duis viverra feugiat porttitor. "
          "Curabitur iaculis nisl quis neque scelerisque rutrum. Curabitur at nisi vitae lacus "
          "hendrerit sollicitudin. Nunc sollicitudin mollis sapien id laoreet. Quisque faucibus "
          "venenatis ultricies. Pellentesque ac finibus ligula. Fusce ac ipsum eget sapien dictum "
          "rhoncus. Vestibulum consequat a sapien dictum posuere. Aenean vitae leo eget est placerat "
          "euismod. Integer sollicitudin, ipsum in finibus semper, lectus tortor bibendum nunc, viverra "
          "hendrerit diam neque et enim. Quisque consequat maximus ipsum sit amet hendrerit. In varius "
          "felis a tellus sodales, nec scelerisque lacus viverra. Ut at nisl pellentesque, vestibulum "
          "eros quis, eleifend lacus. Aenean aliquam imperdiet massa, ullamcorper lacinia tellus ornare non. "
          "Aliquam condimentum nibh eu pulvinar faucibus.\n\n"
          "Nam sed erat leo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque euismod sapien "
          "lacus, in ultricies arcu euismod sit amet. Cras vitae mauris enim. Morbi sodales felis neque, sed "
          "viverra sapien fermentum quis. In hac habitasse platea dictumst. Nulla placerat euismod ipsum, ac "
          "venenatis elit. Quisque pharetra, nunc nec eleifend suscipit, orci dui commodo dui, nec accumsan turpis "
          "augue in dolor. Aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus "
          "porta tortor eget mauris efficitur fringilla."),
    font=("Arial", 12),
    wraplength=1200,
    justify="left",
    bg="white"
)
module1_subheading.pack(pady=10)

module1_button = tk.Button(module1_frame, text="Open TikTok", font=("Arial", 14), command=open_module_1)
module1_button.pack(pady=10)

module_frames["Module 1"] = module1_frame

module2_frame = tk.Frame(root, bg="white", relief="solid")
module2_label = tk.Label(module2_frame, text="Module 2 Content", font=("Arial", 18), bg="white")
module2_label.pack(pady=20)

module2_subheading = tk.Label(
    module2_frame, 
    text=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse enim arcu, "
          "iaculis at pulvinar quis, suscipit tincidunt tortor. Duis viverra feugiat porttitor. "
          "Curabitur iaculis nisl quis neque scelerisque rutrum. Curabitur at nisi vitae lacus "
          "hendrerit sollicitudin. Nunc sollicitudin mollis sapien id laoreet. Quisque faucibus "
          "venenatis ultricies. Pellentesque ac finibus ligula. Fusce ac ipsum eget sapien dictum "
          "rhoncus. Vestibulum consequat a sapien dictum posuere. Aenean vitae leo eget est placerat "
          "euismod. Integer sollicitudin, ipsum in finibus semper, lectus tortor bibendum nunc, viverra "
          "hendrerit diam neque et enim. Quisque consequat maximus ipsum sit amet hendrerit. In varius "
          "felis a tellus sodales, nec scelerisque lacus viverra. Ut at nisl pellentesque, vestibulum "
          "eros quis, eleifend lacus. Aenean aliquam imperdiet massa, ullamcorper lacinia tellus ornare non. "
          "Aliquam condimentum nibh eu pulvinar faucibus.\n\n"
          "Nam sed erat leo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque euismod sapien "
          "lacus, in ultricies arcu euismod sit amet. Cras vitae mauris enim. Morbi sodales felis neque, sed "
          "viverra sapien fermentum quis. In hac habitasse platea dictumst. Nulla placerat euismod ipsum, ac "
          "venenatis elit. Quisque pharetra, nunc nec eleifend suscipit, orci dui commodo dui, nec accumsan turpis "
          "augue in dolor. Aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus "
          "porta tortor eget mauris efficitur fringilla."),
    font=("Arial", 12),
    wraplength=1200,
    justify="left",
    bg="white"
)
module2_subheading.pack(pady=10)

module2_button = tk.Button(module2_frame, text="Say Hello", font=("Arial", 14))
module2_button.pack(pady=10)

module_frames["Module 2"] = module2_frame

module3_frame = tk.Frame(root, bg="white", relief="solid")
module3_label = tk.Label(module3_frame, text="Module 3 Content", font=("Arial", 18), bg="white")
module3_label.pack(pady=20)

module3_subheading = tk.Label(
    module3_frame, 
    text=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse enim arcu, "
          "iaculis at pulvinar quis, suscipit tincidunt tortor. Duis viverra feugiat porttitor. "
          "Curabitur iaculis nisl quis neque scelerisque rutrum. Curabitur at nisi vitae lacus "
          "hendrerit sollicitudin. Nunc sollicitudin mollis sapien id laoreet. Quisque faucibus "
          "venenatis ultricies. Pellentesque ac finibus ligula. Fusce ac ipsum eget sapien dictum "
          "rhoncus. Vestibulum consequat a sapien dictum posuere. Aenean vitae leo eget est placerat "
          "euismod. Integer sollicitudin, ipsum in finibus semper, lectus tortor bibendum nunc, viverra "
          "hendrerit diam neque et enim. Quisque consequat maximus ipsum sit amet hendrerit. In varius "
          "felis a tellus sodales, nec scelerisque lacus viverra. Ut at nisl pellentesque, vestibulum "
          "eros quis, eleifend lacus. Aenean aliquam imperdiet massa, ullamcorper lacinia tellus ornare non. "
          "Aliquam condimentum nibh eu pulvinar faucibus.\n\n"
          "Nam sed erat leo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque euismod sapien "
          "lacus, in ultricies arcu euismod sit amet. Cras vitae mauris enim. Morbi sodales felis neque, sed "
          "viverra sapien fermentum quis. In hac habitasse platea dictumst. Nulla placerat euismod ipsum, ac "
          "venenatis elit. Quisque pharetra, nunc nec eleifend suscipit, orci dui commodo dui, nec accumsan turpis "
          "augue in dolor. Aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus "
          "porta tortor eget mauris efficitur fringilla."),
    font=("Arial", 12),
    wraplength=1200,
    justify="left",
    bg="white"
)
module3_subheading.pack(pady=10)

module3_button = tk.Button(module3_frame, text="Print to Console", font=("Arial", 14), command=lambda: print("Module 3 Clicked"))
module3_button.pack(pady=10)

module_frames["Module 3"] = module3_frame

top_buttons = [
    ("Module 1", lambda: show_module("Module 1")),
    ("Module 2", lambda: show_module("Module 2")),
    ("Module 3", lambda: show_module("Module 3")),
]

for text, command in top_buttons:
    btn = tk.Button(module_menu, text=text, font=("Arial", 12), width=15, relief="flat", bg="white", command=command)
    btn.pack(pady=2, padx=5, fill="x")

main_menu.place(x=0, y=40, width=150, height=765)

root.mainloop()
