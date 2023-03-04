import tkinter as tk
from tkinter import messagebox
import pyqrcode


class LoginSystem:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.master.title("Login System")
        self.master.config(bg="#2c3e50")

        self.username_label = tk.Label(self.master, text="Username:", font=("Helvetica", 14), fg="white", bg="#2c3e50")
        self.username_label.pack(pady=10)
        self.username_entry = tk.Entry(self.master, font=("Helvetica", 14), bg="#34495e", fg="white")
        self.username_entry.pack()

        self.password_label = tk.Label(self.master, text="Password:", font=("Helvetica", 14), fg="white", bg="#2c3e50")
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.master, show="*", font=("Helvetica", 14), bg="#34495e", fg="white")
        self.password_entry.pack()

        self.login_button = tk.Button(self.master, text="Login", command=self.login, font=("Helvetica", 14), bg="#1abc9c", fg="white", relief="flat")
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            self.master.destroy()
            root = tk.Tk()
            app = GenerateQRCode(root)
            root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")


class GenerateQRCode:
    def __init__(self, master):
        self.master = master
        self.master.geometry("410x400")
        self.master.title("Generate QR Code")

        self.e1 = tk.Entry(self.master, font=22, bg='white', width=15)
        self.e1.grid(row=0, column=0, padx=10, pady=10)

        self.b1 = tk.Button(self.master, font=22, text='Generate QR code', command=self.generate_qr)
        self.b1.grid(row=0, column=1, padx=5, pady=10)

        self.l1 = tk.Label(self.master, text='QR code will display here')
        self.l1.grid(row=1, column=0, columnspan=2)

    def generate_qr(self):
        my_qr = pyqrcode.create(self.e1.get())
        my_qr.png('my_qr.png', scale=6,
                  module_color=[0, 0, 0, 128], background=[0xff, 0xcc, 0xcc])
        my_img = tk.PhotoImage(file='my_qr.png')
        self.l1.config(image=my_img)


root = tk.Tk()
app = LoginSystem(root)
root.mainloop()
