import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fungsi untuk menampilkan konten berdasarkan pilihan di sidebar
def show_content(content):
    for frame in frames.values():
        frame.grid_forget()  # Sembunyikan semua frame
    frames[content].grid(row=0, column=0, sticky="nsew")  # Tampilkan frame yang dipilih
    
    update_active_button(content)  # Perbarui status aktif tombol sidebar

# Fungsi untuk mengatur ulang ukuran sidebar dan content saat jendela diubah ukurannya
def resize(event):
    sidebar_width = 300  # Sidebar width tetap 264 px
    window_width = event.width
    content_width = window_width - sidebar_width

    # Atur ulang ukuran sidebar dan content frame
    sidebar.config(width=sidebar_width)
    content_frame.config(width=content_width)

# Fungsi untuk memperbarui status aktif tombol sidebar
def update_active_button(active_content):
    # Reset semua tombol sidebar ke ikon dan warna default
    dashboard_button.config(image=icon_home, style="Inactive.TButton")
    running_button.config(image=icon_loader, style="Inactive.TButton")
    users_button.config(image=icon_users, style="Inactive.TButton")
    
    # Tentukan tombol mana yang aktif berdasarkan konten yang sedang ditampilkan
    if active_content == "dashboard":
        dashboard_button.config(image=icon_home_active, style="Active.TButton")
    elif active_content == "running":
        running_button.config(image=icon_loader_active, style="Active.TButton")
    elif active_content == "users":
        users_button.config(image=icon_users_active, style="Active.TButton")

# Membuat jendela utama menggunakan ttkbootstrap
root = ttk.Window(themename="litera")
root.title("Dashboard")

# Memaksimalkan jendela saat aplikasi dimulai
root.state('zoomed')  # Menggunakan 'zoomed' untuk memaksimalkan pada Windows

# Membuat layout grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Sidebar
sidebar = tk.Frame(root, bg="lightgray", width=300, height=600)  # Sidebar width tetap 264 px
sidebar.grid(row=0, column=0, sticky="ns")
sidebar.grid_propagate(False)  # Mencegah pengubahan ukuran otomatis

# Load icons from assets (both active and inactive)
icon_home = ImageTk.PhotoImage(Image.open("assets/home.png").resize((20, 20)))
icon_loader = ImageTk.PhotoImage(Image.open("assets/loader.png").resize((20, 20)))
icon_users = ImageTk.PhotoImage(Image.open("assets/users.png").resize((20, 20)))
icon_arrow = ImageTk.PhotoImage(Image.open("assets/arrow_right.png").resize((35, 35)))
user_plus = ImageTk.PhotoImage(Image.open("assets/user-plus.png").resize((20, 20)))

icon_home_active = ImageTk.PhotoImage(Image.open("assets/home_active.png").resize((20, 20)))
icon_loader_active = ImageTk.PhotoImage(Image.open("assets/loader_active.png").resize((20, 20)))
icon_users_active = ImageTk.PhotoImage(Image.open("assets/users_active.png").resize((20, 20)))

# Styling for the sidebar buttons
style = ttk.Style()
style.configure("Inactive.TButton", font=("Poppins", 14, "bold"), anchor="w", 
                padding=(12, 8), background='#f4f4f4', foreground='#333', borderwidth=0, relief="flat")
style.configure("Active.TButton", font=("Poppins", 14, "bold"), anchor="w", 
                padding=(12, 8), background='#007bff', foreground='white', borderwidth=0, relief="flat")

# Fungsi untuk membuat tombol sidebar dengan ikon dan teks
def create_sidebar_button(text, icon, command=None):
    button = ttk.Button(sidebar, text=f" {text}", image=icon, compound="left",
                        style="Inactive.TButton", command=command, takefocus=False)
    button.pack(fill='x', padx=10, pady=5)
    return button

# Create sidebar buttons with icons and text
dashboard_button = create_sidebar_button("Dashboard", icon_home, lambda: show_content("dashboard"))
running_button = create_sidebar_button("Running", icon_loader, lambda: show_content("running"))
users_button = create_sidebar_button("Users", icon_users, lambda: show_content("users"))

# Frame konten utama
content_frame = tk.Frame(root)
content_frame.grid(row=0, column=1, sticky="nsew")

# Membuat fungsi untuk menambahkan header dan area konten
def create_page(frame, header_text):
    # Header dengan warna font biru
    header = tk.Label(frame, text=header_text, bg="white", fg="#007bff", font=("Poppins", 24, "bold"))
    header.pack(pady=20)

    # Area konten tanpa outline (border)
    content_area = tk.Frame(frame, bg="white")  # Menghilangkan border dan relief
    content_area.pack(fill="both", expand=True, padx=20, pady=10)
    
    return content_area

# Membuat frame untuk setiap konten
frames = {
    "dashboard": tk.Frame(content_frame, bg="white"),
    "running": tk.Frame(content_frame, bg="white"),
    "users": tk.Frame(content_frame, bg="white")
}

# Menambahkan header dan area konten untuk setiap halaman
dashboard_content_area = create_page(frames["dashboard"], "Dashboard")
running_content_area = create_page(frames["running"], "Running")
users_content_area = create_page(frames["users"], "Users")

# Box 1 di dalam dashboard_content_area, yang akan dibagi menjadi 2 sub-box
box1 = tk.Frame(dashboard_content_area, bg="#d3d3d3", width=200, height=300, bd=2, relief="groove")
box1.pack(side="left", padx=10, pady=10, fill="both", expand=True)

# Membagi Box 1 menjadi dua sub-box
subbox1 = tk.Frame(box1, height=150, bd=2, relief="flat")  # Sub-box pertama di atas
subbox1.pack(fill="x", pady=5)
# subbox1_label = tk.Label(subbox1, text="Sub-Box 1", bg="#a9a9a9", font=("Poppins", 14))
# subbox1_label.pack(pady=20)

subbox2 = tk.Frame(box1, bg="#bfbfbf", width=150, bd=2, relief="groove")  # Sub-box kedua di bawah
subbox2.pack(pady=5, fill="both", expand=True)

def create_pie_chart(frame):
    # Data untuk diagram pie
    labels = ['Sukawati', 'Blahbatuh', 'Gianyar', 'Tampaksiring', 'Ubud', 'Tegallalang', 'Payangan']
    sizes = [10, 10, 10, 9, 5, 3, 11]
    colors = plt.cm.Paired(range(len(labels)))  # Warna yang berbeda untuk setiap bagian
    
    # Membuat diagram pie
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))
    wedges, _, _ = ax.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=140)
    
    # Menambahkan keterangan
    legend_labels = [f'{label}: {size}' for label, size in zip(labels, sizes)]
    ax.legend(wedges, legend_labels, loc="center left", bbox_to_anchor=(1, 0, 0.3, 1), frameon=False)
    
    # Menghilangkan border
    fig.patch.set_visible(False)
    ax.axis('off')

    # Menggunakan tight_layout untuk mengoptimalkan ruang
    plt.tight_layout()

    # Menambahkan canvas matplotlib ke frame Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    
    # Tempatkan canvas menggunakan pack
    canvas.get_tk_widget().pack(side="left", fill="both", expand=True)



# Memanggil fungsi untuk membuat pie chart di box2
create_pie_chart(subbox2)

# Membagi Sub-Box 1 menjadi dua sub-sub-box dengan posisi kiri dan kanan
subsubbox1 = tk.Frame(subbox1, bg="#808080", width=150, height=350, 
                      highlightbackground="#007bff", highlightthickness=2)  # Sub-Sub-Box 1 di kiri, kotak dengan outline biru
subsubbox1.pack(side="left", padx=(0, 5), fill="both", expand=True)

# Menambahkan teks "70 Users" di tengah Sub-Sub-Box 1
subsubbox1_label_users = tk.Label(subsubbox1, text="70 Users", bg="#808080", font=("Poppins", 20, "bold"))
subsubbox1_label_users.place(relx=0.5, rely=0.4, anchor="center")

# Menambahkan teks "User list" dengan ikon panah di bawah teks "70 Users"
# subsubbox1_label_list = tk.Label(subsubbox1, text="User list", bg="#808080", font=("Poppins", 20), image=icon_arrow, compound="right")
# subsubbox1_label_list.place(relx=0.5, rely=0.5, anchor="center") 

# Membuat frame untuk menampung teks dan ikon
frame_with_icon = tk.Frame(subsubbox1, bg="#808080")
frame_with_icon.place(relx=0.5, rely=0.5, anchor="center")

# Label untuk teks
label_text = tk.Label(frame_with_icon, text="User list", bg="#808080", font=("Poppins", 18))
label_text.pack(side="left", padx=(0, 5))  # Padding antara teks dan ikon

# Label untuk ikon
label_icon = tk.Label(frame_with_icon, bg="#808080", image=icon_arrow)
label_icon.pack(side="left")


style.configure("Blue.TFrame", background="#007bff")

# Membuat frame subsubbox2 dengan style latar belakang biru
subsubbox2 = ttk.Frame(subbox1, style="Blue.TFrame", width=150, height=150)
subsubbox2.pack(side="left", padx=(0, 5), fill="both", expand=True)

# Menambahkan teks di tengah frame dengan warna putih
label_users = ttk.Label(subsubbox2, text="Latest Running", foreground="white", font=("Poppins", 16, "bold"), background="#007bff")
label_users.place(relx=0.5, rely=0.4, anchor="center")

label_list = ttk.Label(subsubbox2, text="20-04-2024", foreground="white", font=("Poppins", 16, "bold"), background="#007bff")
label_list.place(relx=0.5, rely=0.5, anchor="center")

# Box 2 di dashboard_content_area
box2 = tk.Frame(dashboard_content_area, bg="#d3d3d3", width=200, height=150, bd=2, relief="groove")
box2.pack(side="left", padx=10, pady=10, fill="both", expand=True)

# Membagi Box 1 menjadi dua sub-box
subbox2 = tk.Frame(box2, bg="#a9a9a9", height=150, bd=2, relief="groove")  # Sub-box pertama di atas
subbox2.pack(fill="x", pady=5)
subbox2_label = tk.Label(subbox2, text="Preferensi", bg="#a9a9a9", font=("Poppins", 18, "bold"))
subbox2_label.pack(pady=20)

subbox2 = tk.Frame(box2, bg="#bfbfbf", height=150, bd=2, relief="groove")  # Sub-box kedua di bawah
subbox2.pack(fill="x", pady=5, anchor="w")
# subbox2_label = tk.Label(subbox2, text="Sub-Box 2", bg="#bfbfbf", font=("Poppins", 14))
# subbox2_label.pack(pady=20, padx=(0, 10), anchor="w")


# Fungsi untuk menghapus teks dari entry
def clear_search():
    search_entry.delete(0, tk.END)
    search_entry.insert(0, 'Find something...')
    search_entry.config(fg='grey')

# Fungsi untuk menampilkan placeholder
def on_focus_in(event):
    if search_entry.get() == 'Find something...':
        search_entry.delete(0, tk.END)
        search_entry.config(fg='black')

def on_focus_out(event):
    if search_entry.get() == '':
        search_entry.insert(0, 'Find something...')
        search_entry.config(fg='grey')

# Ikon pencarian
icon_search = ImageTk.PhotoImage(Image.open("assets/search.png").resize((20, 20)))  # Sesuaikan jalur gambar

# Label untuk ikon search
icon_label = ttk.Label(subbox2, image=icon_search)
icon_label.pack(side=tk.LEFT, padx=(5, 0))

# Membuat entry dengan placeholder
search_entry = ttk.Entry(subbox2, font=("Poppins", 12), width=70)
search_entry.insert(0, 'Find something...')
search_entry.config(foreground='grey')
search_entry.bind("<FocusIn>", on_focus_in)
search_entry.bind("<FocusOut>", on_focus_out)
search_entry.pack(side=tk.LEFT, fill=tk.X, padx=(5, 5))

# Membuat tombol clear
clear_button = ttk.Button(subbox2, text="X", command=clear_search)
clear_button.pack(side=tk.RIGHT, padx=(0, 5))


# Menambahkan dua kotak abu-abu tanpa outline di halaman running
box_running_2 = tk.Frame(running_content_area, bg="#d3d3d3", width=200, height=150, bd=2, relief="groove")
box_running_2.pack(side="left", padx=10, pady=10, fill="both", expand=True)
# box2_label = tk.Label(box2, text="Box 1", bg="#d3d3d3", font=("Poppins", 16))
# box2_label.pack(pady=20)

subbox_running_2 = tk.Frame(box_running_2, bg="#a9a9a9", height=150, bd=2, relief="groove")  # Sub-box pertama di atas
subbox_running_2.pack(fill="x", pady=5)

subbox_running_2.grid_columnconfigure(0, weight=1)  # First column
subbox_running_2.grid_columnconfigure(1, weight=1)  # Second column

# Create the labels and entry fields for Start date and End date
start_date_label = tk.Label(subbox_running_2, text="Start date  :", bg="#a9a9a9", font=("Poppins", 14), anchor="e")
start_date_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

start_date_entry = ttk.Entry(subbox_running_2, font=("Poppins", 12), width=30)
start_date_entry.insert(0, "ex: dd-mm-yyyy")
start_date_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

end_date_label = tk.Label(subbox_running_2, text="End date    :", bg="#a9a9a9", font=("Poppins", 14), anchor="e")
end_date_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

end_date_entry = ttk.Entry(subbox_running_2, font=("Poppins", 12), width=30)
end_date_entry.insert(0, "ex: dd-mm-yyyy")
end_date_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Create the 'Run' button
run_button = ttk.Button(subbox_running_2, text="Run", style="TButton", width=10)
run_button.grid(row=2, column=1, padx=(200, 0), pady=10, sticky="w")

subbox_running_2 = tk.Frame(box_running_2, bg="#bfbfbf", height=150, bd=2, relief="groove")  # Sub-box kedua di bawah
subbox_running_2.pack(fill="x", pady=5)
subbox_running_2_label = tk.Label(subbox_running_2, text="Error Information", bg="#bfbfbf", font=("Poppins", 16, "bold"))
subbox_running_2_label.pack(pady=20)

subbox_running_2 = tk.Frame(box_running_2, bg="#bfbfbf", height=650, bd=2, relief="groove")  # Sub-box ketiga di bawah
subbox_running_2.pack(fill="x", pady=5)
# subbox_running_2_label = tk.Label(subbox_running_2, text="Sub-Box 3", bg="#bfbfbf", font=("Poppins", 14))
# subbox_running_2_label.pack(pady=20)





# Menambahkan dua kotak abu-abu tanpa outline di halaman users
box_users_1 = tk.Frame(users_content_area, bg="#d3d3d3", width=200, height=150, bd=2, relief="groove")
box_users_1.pack(side="left", padx=10, pady=10, fill="both", expand=True)
# box1_label = tk.Label(box1, text="Box 1", bg="#d3d3d3", font=("Poppins", 16))
# box1_label.pack(pady=20)
subbox_users_2 = tk.Frame(box_users_1, bg="#a9a9a9", bd=2, relief="groove")  # Sub-box pertama di atas
subbox_users_2.pack(fill="x", pady=5)


subsubbox_users_1 = tk.Frame(subbox_users_2, bg="#808080", width=150)  # Sub-Sub-Box 1 di kiri
subsubbox_users_1.pack(side="left", padx=(0, 5), fill="both", expand=True)

# Label untuk ikon search
icon_label = ttk.Label(subsubbox_users_1, image=icon_search)
icon_label.pack(side=tk.LEFT, padx=(5, 0))

# Membuat entry dengan placeholder
search_entry = ttk.Entry(subsubbox_users_1, font=("Poppins", 12), width=125)
search_entry.insert(0, 'Find something...')
search_entry.config(foreground='grey')
search_entry.bind("<FocusIn>", on_focus_in)
search_entry.bind("<FocusOut>", on_focus_out)
search_entry.pack(side=tk.LEFT, fill=tk.X, padx=(5, 5))

# Membuat tombol clear
clear_button = ttk.Button(subsubbox_users_1, text="X", command=clear_search)
clear_button.pack(side=tk.RIGHT, padx=(0, 5))

subsubbox_users_2 = tk.Frame(subbox_users_2, bg="#808080", width=150)  # Sub-Sub-Box 1 di kanan
subsubbox_users_2.pack(side="left", padx=(0, 5), fill="both", expand=True)
# Tambahkan tombol berwarna biru ke subsubbox_users_2 dengan ikon user_plus
button_user_plus = ttk.Button(subsubbox_users_2, text=" Add User", image=user_plus, compound="right", 
                              style="Blue.TButton", takefocus=False)

# Tempatkan tombol di subsubbox_users_2
button_user_plus.pack(side="left", padx=(10, 0), pady=10, fill="x", expand=True)

# Tambahkan konfigurasi gaya untuk tombol biru
style.configure("Blue.TButton", font=("Poppins", 14, "bold"), anchor="w", 
                padding=(12, 8), background='#007bff', foreground='white', borderwidth=0, relief="flat")


subbox_users_2 = tk.Frame(box_users_1, bg="#bfbfbf", height=860, bd=2, relief="groove")  # Sub-box kedua di bawah
subbox_users_2.pack(fill="x", pady=5)
# subbox_users_2_label = tk.Label(subbox_users_2, text="Sub-Box 2", bg="#bfbfbf", font=("Poppins", 14))
# subbox_users_2_label.pack(pady=20)


# Tampilkan konten dashboard pertama kali
show_content("dashboard")

# Mengatur grid pada content_frame untuk mengisi penuh ruang
content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_columnconfigure(0, weight=1)

# Bind event resize untuk mengatur ulang ukuran sidebar dan konten
root.bind('<Configure>', resize)

# Menjalankan aplikasi
root.mainloop()
