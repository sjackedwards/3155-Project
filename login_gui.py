import tkinter as tk
from tkinter import messagebox
from authentication import register, login
from core_gui import Core

class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Flight Searcher Login")
        self.geometry("250x150")

        self.create_widgets()

    def create_widgets(self):
        self.lbl_username = tk.Label(self, text="Username:")
        self.lbl_username.grid(row=0, column=0, padx=(15,10), pady=(18,7))

        self.ent_username = tk.Entry(self)
        self.ent_username.grid(row=0, column=1,pady=(18,7))

        self.lbl_password = tk.Label(self, text="Password:")
        self.lbl_password.grid(row=1, column=0, padx=(15,10), pady=10)

        self.ent_password = tk.Entry(self, show="•")
        self.ent_password.grid(row=1, column=1)

        self.btn_register = tk.Button(self, text="Register", command=self.register_user)
        self.btn_register.grid(row=2, column=0, padx=(50,0), pady=(12,0))

        self.btn_login = tk.Button(self, text="Login", command=self.login_user)
        self.btn_login.grid(row=2, column=1, padx=5, pady=(12,0))

    def register_user(self):
        username = self.ent_username.get()
        password = self.ent_password.get()

        if username and password:
            success, message = register(username, password)
        if success:
            messagebox.showinfo("Registration Success", message)
        else:
            messagebox.showerror("Registration Failure", message)

                

    def login_user(self):
        username = self.ent_username.get()
        password = self.ent_password.get()

        if username and password:
            token = login(username, password)
            if token:
                messagebox.showinfo("Login", "Login successful.")
                
                self.create_core_window(username)
                
            else:
                messagebox.showerror("Login", "Incorrect username or password.")
        else:
            messagebox.showerror("Login", "Both fields are required.")

    def create_core_window(self, username):
        self.username = username
        core_window = Core()
        core_window.mainloop()


def main():
    app = Login()
    app.mainloop()

if __name__ == "__main__":
    main()
