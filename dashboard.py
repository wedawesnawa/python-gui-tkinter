import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Fungsi untuk menampilkan konten berdasarkan pilihan di sidebar
def show_content(content):
    for frame in frames.values():
        frame.grid_forget()  # Sembunyikan semua frame
    frames[content].grid(row=0, column=0, sticky="nsew")  # Tampilkan frame yang dipilih

# Membuat jendela utama
root = ttk.Window(themename="flatly")
root.title("Dashboard")

# Memaksimalkan jendela saat aplikasi dimulai
root.state('zoomed')  # Menggunakan 'zoomed' untuk memaksimalkan pada Windows

# Membuat layout grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Sidebar
sidebar = tk.Frame(root, bg="#f4f4f4", width=264, height=600)
sidebar.grid(row=0, column=0, sticky="ns")
sidebar.grid_propagate(False)

# Load icons from assets
icon_home = ImageTk.PhotoImage(Image.open("assets/home.png").resize((20, 20)))
icon_loader = ImageTk.PhotoImage(Image.open("assets/loader.png").resize((20, 20)))
icon_users = ImageTk.PhotoImage(Image.open("assets/users.png").resize((20, 20)))

# Styling for the sidebar buttons
buttons = [("Dashboard", "dashboard", icon_home), 
           ("Running", "running", icon_loader), 
           ("Users", "users", icon_users)]

def create_sidebar_button(text, icon, command=None):
    button = ttk.Button(sidebar, text=f" {text}", image=icon, compound="left",
                        style="Sidebar.TButton", command=command)
    button.pack(fill='x', padx=10, pady=5)
    return button

# Styling for buttons (padding, focus, and color)
style = ttk.Style()
style.configure("Sidebar.TButton", font=("Arial", 12, "bold"), 
                background="#f4f4f4", foreground="#333",
                anchor="w", padding=(12, 8))
style.map("Sidebar.TButton",
          background=[('active', '#007bff'), ('!active', '#f4f4f4')],
          foreground=[('active', 'white'), ('!active', '#333')])

# Create sidebar buttons with icons and text
dashboard_button = create_sidebar_button("Dashboard", icon_home, lambda: show_content("dashboard"))
running_button = create_sidebar_button("Running", icon_loader, lambda: show_content("running"))
users_button = create_sidebar_button("Users", icon_users, lambda: show_content("users"))

# Main content area
content_frame = tk.Frame(root, bg="white")
content_frame.grid(row=0, column=1, sticky="nsew")

# Membuat frame untuk setiap konten
frames = {
    "dashboard": tk.Frame(content_frame, bg="white"),
    "running": tk.Frame(content_frame, bg="white"),
    "users": tk.Frame(content_frame, bg="white")
}

# Mengisi konten untuk setiap frame
for frame in frames.values():
    frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(frames["dashboard"], text="Dashboard", font=("Arial", 20, "bold"), foreground="#007bff").pack(pady=20)
ttk.Label(frames["running"], text="Running", font=("Arial", 20), foreground="#333").pack(pady=20)
ttk.Label(frames["users"], text="Users", font=("Arial", 20), foreground="#333").pack(pady=20)

# Tampilkan konten pertama kali
frames["dashboard"].grid(row=0, column=0, sticky="nsew")

# Mengatur grid pada content_frame untuk mengisi penuh ruang
content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_columnconfigure(0, weight=1)

# Menjalankan aplikasi
root.mainloop()
