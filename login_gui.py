import tkinter as tk
from tkinter import messagebox
from authentication import register, login
from core_gui import Core
from database import setup_database



class LoginGui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("300x200")

        self.create_widgets()

    def create_widgets(self):
        self.lbl_username = tk.Label(self, text="Username:")
        self.lbl_username.grid(row=0, column=0, padx=5, pady=5)

        self.ent_username = tk.Entry(self)
        self.ent_username.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_password = tk.Label(self, text="Password:")
        self.lbl_password.grid(row=1, column=0, padx=5, pady=5)

        self.ent_password = tk.Entry(self, show="•")
        self.ent_password.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_confirm_password = tk.Label(self, text="Confirm Password:")
        self.lbl_confirm_password.grid(row=3, column=0, padx=5, pady=5)

        self.ent_confirm_password = tk.Entry(self, show="•")
        self.ent_confirm_password.grid(row=3, column=1, padx=5, pady=5)

        self.lbl_api_key = tk.Label(self, text="API Key")
        self.lbl_api_key.grid(row=4, column=0, padx=5, pady=5)

        self.ent_api_key = tk.Entry(self)
        self.ent_api_key.grid(row=4, column=1, padx=5, pady=5)

        self.btn_register = tk.Button(self, text="Register", command=self.register_user)
        self.btn_register.grid(row=5, column=1, padx=5, pady=5)

        self.btn_login = tk.Button(self, text="Login", command=self.login_user)
        self.btn_login.grid(row=2, column=1, padx=5, pady=5)

    def register_user(self):
        username = self.ent_username.get()
        password = self.ent_password.get()
        confirm_password = self.ent_confirm_password.get()
        api_key = self.ent_api_key.get()

        if not username or not password or not confirm_password:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        if not api_key:
            messagebox.showerror("Error", "Please enter your API Key.")
            return

        success, message = register(username, password, api_key)
        if success:
            messagebox.showinfo("Registration Success", message)
        else:
            messagebox.showerror("Registration Failure", message)

    def login_user(self):
        username = self.ent_username.get()
        password = self.ent_password.get()

        if username and password:
            token, api_key = login(username, password)
            if token:
                messagebox.showinfo("Login", "Login successful.")
                self.api_key = api_key
                self.create_core_window(username, api_key)
            else:
                messagebox.showerror("Login", "Incorrect username or password.")
        else:
            messagebox.showerror("Login", "Both fields are required.")

    def create_core_window(self, username, api_key):
        self.username = username
        core_window = Core(username=username, api_key=api_key)
        core_window.mainloop()


def main():
    setup_database()  # This line ensures the database is set up before the application starts
    app = LoginGui()
    app.mainloop()

if __name__ == "__main__":
    main()
























# class Login(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Flight Searcher Login")
#         self.geometry("250x175")

#         self.create_widgets()

#     def create_widgets(self):

#         self.lbl_api_key = tk.Label(self, text="Expedia API Key:")
#         self.lbl_api_key.grid(row=4, column=0, padx=5, pady=15)
#         self.entry_api_key_var = tk.StringVar()
#         self.entry_api_key = tk.Entry(self, textvariable=self.entry_api_key_var)
#         self.entry_api_key.grid(row=4, column=1, padx=5, pady=15)

#         self.lbl_username = tk.Label(self, text="Username:")
#         self.lbl_username.grid(row=0, column=0, padx=(15,10), pady=(18,7))

#         self.ent_username = tk.Entry(self)
#         self.ent_username.grid(row=0, column=1,pady=(18,7))

#         self.lbl_password = tk.Label(self, text="Password:")
#         self.lbl_password.grid(row=1, column=0, padx=(15,10), pady=10)

#         self.ent_password = tk.Entry(self, show="•")
#         self.ent_password.grid(row=1, column=1)

#         self.btn_register = tk.Button(self, text="Register", command=self.register_user)
#         self.btn_register.grid(row=2, column=0, padx=(50,0), pady=(12,0))

#         self.btn_login = tk.Button(self, text="Login", command=self.login_user)
#         self.btn_login.grid(row=2, column=1, padx=5, pady=(12,0))

#     def register_user(self):
#         username = self.ent_username.get()
#         password = self.ent_password.get()

#         if username and password:
#             success, message = register(username, password)
#         if success:
#             messagebox.showinfo("Registration Success", message)
#         else:
#             messagebox.showerror("Registration Failure", message)

                

#     def login_user(self):
#         username = self.ent_username.get()
#         password = self.ent_password.get()

#         if username and password:
#             token = login(username, password)
#             if token:
#                 messagebox.showinfo("Login", "Login successful.")

#                 self.create_core_window(username)
                
#             else:
#                 messagebox.showerror("Login", "Incorrect username or password.")
#         else:
#             messagebox.showerror("Login", "Both fields are required.")

#     def create_core_window(self, username):
#         self.username = username
#         core_window = Core()
#         core_window.mainloop()


# def main():
#     app = Login()
#     app.mainloop()

# if __name__ == "__main__":
#     main()
