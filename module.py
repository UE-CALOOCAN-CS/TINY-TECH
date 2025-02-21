import tkinter as tk
import webbrowser
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk

def toggle_menu():
    if main_menu.winfo_ismapped():
        main_menu.place_forget()
        module_menu.place(x=0, y=40, width=150, height=765)
    else:
        module_menu.place_forget()
        main_menu.place(x=0, y=40, width=150, height=765)

def open_survey():
    webbrowser.open("https://www.tiktok.com/@parenghayb")

def show_module(module_name):
    # Pause any currently playing video
    for name, controls in video_controls.items():
        if controls["cap"] is not None and not controls["paused"]:
            controls["paused"] = True  # Pause the video
    
    # Switch module display
    for frame in module_frames.values():
        frame.place_forget()
    module_frames[module_name].place(x=160, y=50, width=1290, height=900)

def logout():
    root.quit()

def select_video(module_canvas, module_name):
    video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")])
    if video_path:
        cap = cv2.VideoCapture(video_path)
        video_controls[module_name]["cap"] = cap  # Store video capture object
        video_controls[module_name]["paused"] = False  # Reset pause state
        play_video(module_name)

def play_video(module_name):
    controls = video_controls[module_name]
    cap = controls["cap"]
    
    if cap is None or controls["paused"]:
        return  # Stop updating if paused

    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (800, 450))  # Resize video
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)

        module_canvas = controls["canvas"]
        module_canvas.create_image(0, 0, anchor=tk.NW, image=frame)
        module_canvas.image = frame  # Keep reference
        
        root.after(25, lambda: play_video(module_name))  # Refresh at ~40 FPS
    else:
        cap.release()

def toggle_play_pause(module_name):
    controls = video_controls[module_name]
    controls["paused"] = not controls["paused"]

    if not controls["paused"]:  # Resume playback
        play_video(module_name)

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
video_controls = {}  # Store video state for each module

module_descriptions = {
    "Module 1": "This is the description for module 1. This is the description for module 1. This is the description for module 1. This is the description for module 1.",
    "Module 2": "This is the description for module 2. This is the description for module 2. This is the description for module 2.",
    "Module 3": "This is the description for module 3. This is the description for module 3. This is the description for module 3."
}

for i in range(1, 4):
    module_name = f"Module {i}"
    frame = tk.Frame(root, bg="white", relief="solid")
    label = tk.Label(frame, text=f"{module_name} Content", font=("Arial", 18), bg="white")
    label.pack(pady=20)
    
    description = tk.Label(frame, text=module_descriptions[module_name], font=("Arial", 12), bg="white", wraplength=1200, justify="left")
    description.pack(pady=10)
    
    subheading = tk.Label(frame, text="Video Player for Module", font=("Arial", 12), bg="white")
    subheading.pack(pady=10)
    
    canvas = tk.Canvas(frame, width=800, height=450, bg="black")
    canvas.pack()
    
    button_frame = tk.Frame(frame)
    button_frame.pack(pady=10)
    
    play_pause_button = tk.Button(button_frame, text="Play/Pause", font=("Arial", 12), command=lambda m=module_name: toggle_play_pause(m))
    play_pause_button.pack(side="left", padx=5)

    load_video_button = tk.Button(button_frame, text="Load Video", font=("Arial", 12), command=lambda c=canvas, m=module_name: select_video(c, m))
    load_video_button.pack(side="left", padx=5)

    module_frames[module_name] = frame
    video_controls[module_name] = {"cap": None, "paused": True, "canvas": canvas}

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
