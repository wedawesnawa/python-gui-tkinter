import tkinter as tk

root = tk.Tk()

root.geometry("1440x1024")
root.title("Sistem Informasi Statistics Broadcasting (SISBRO)")

frame_username = tk.Frame(root)
frame_username.pack(padx=10, pady=10)

label_username = tk.Label(frame_username, text="Username", font=('Poppins', 16))
label_username.pack(side="left", padx=20, pady=20)

username_admin = tk.Entry(frame_username, font=('Poppins', 16))
username_admin.pack(side="left")

frame_password = tk.Frame(root)
frame_password.pack(padx=10, pady=10)

label_password = tk.Label(frame_password, text="Password", font=('Poppins', 16))
label_password.pack(side="left", padx=20, pady=20)

password_admin = tk.Entry(frame_password, font=('Poppins', 16))
password_admin.pack(side="left")

root.mainloop()
