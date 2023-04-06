import tkinter as tk
from tkinter import messagebox
from authentication import register, login

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Local App")
        self.geometry("300x150")

        self.create_widgets()

    def create_widgets(self):
        self.lbl_username = tk.Label(self, text="Username:")
        self.lbl_username.grid(row=0, column=0, padx=5, pady=5)

        self.ent_username = tk.Entry(self)
        self.ent_username.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_password = tk.Label(self, text="Password:")
        self.lbl_password.grid(row=1, column=0, padx=5, pady=5)

        self.ent_password = tk.Entry(self, show="*")
        self.ent_password.grid(row=1, column=1, padx=5, pady=5)

        self.btn_register = tk.Button(self, text="Register", command=self.register_user)
        self.btn_register.grid(row=2, column=0, padx=5, pady=5)

        self.btn_login = tk.Button(self, text="Login", command=self.login_user)
        self.btn_login.grid(row=2, column=1, padx=5, pady=5)

    def register_user(self):
        username = self.ent_username.get()
        password = self.ent_password.get()

        if username and password:
            if register(username, password):
                messagebox.showinfo("Registration", "User registered successfully.")
            else:
                messagebox.showerror("Registration", "Username already exists.")
        else:
            messagebox.showerror("Registration", "Both fields are required.")

    def login_user(self):
        username = self.ent_username.get()
        password = self.ent_password.get()

        if username and password:
            token = login(username, password)
            if token:
                messagebox.showinfo("Login", "Login successful.")
            else:
                messagebox.showerror("Login", "Incorrect username or password.")
        else:
            messagebox.showerror("Login", "Both fields are required.")

def main():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()
