import tkinter as tk
from tkinter import messagebox

# Function to handle the color button click and simulate color detection
def search_color(color):
    notification_label.config(text=f"Searching for {color}...", fg="black")
    root.after(2000, detect_color, color)  # Simulate detection after 2 seconds

# Function to show detected notification
def detect_color(color):
    notification_label.config(text=f"{color} Detected, car stopped.", fg="green")
    messagebox.showinfo("Detection", f"{color} Detected. The car has stopped.")

# Create the main window
root = tk.Tk()
root.title("Team Dashboard")
root.geometry("550x550")
root.configure(bg='#ffffff')

# Add Team Name at the top
team_label = tk.Label(root, text="Team A", font=("Helvetica", 24, "bold"), bg='#ffffff', fg='#333')
team_label.pack(pady=20)

# Create a frame for the dashboard (control panel)
dashboard_frame = tk.Frame(root, bg="#f0f0f0", bd=4, relief=tk.RIDGE)
dashboard_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Button container for the color buttons
button_frame = tk.Frame(dashboard_frame, bg="#f0f0f0")
button_frame.pack(pady=20)

# Create Red, Blue, and Yellow buttons
red_button = tk.Button(button_frame, text="Red", bg="#e74c3c", fg="white", width=10, height=3, 
                       font=("Helvetica", 14), command=lambda: search_color("Red"))
red_button.grid(row=0, column=0, padx=10)

blue_button = tk.Button(button_frame, text="Blue", bg="#3498db", fg="white", width=10, height=3, 
                        font=("Helvetica", 14), command=lambda: search_color("Blue"))
blue_button.grid(row=0, column=1, padx=10)

yellow_button = tk.Button(button_frame, text="Yellow", bg="#f1c40f", fg="white", width=10, height=3, 
                          font=("Helvetica", 14), command=lambda: search_color("Yellow"))
yellow_button.grid(row=0, column=2, padx=10)

# Notification label to show detection status
notification_label = tk.Label(dashboard_frame, text="", font=("Helvetica", 12), bg="#f0f0f0")
notification_label.pack(pady=20)

# Run the application
root.mainloop()
