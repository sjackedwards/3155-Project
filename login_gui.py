import tkinter as tk
from tkinter import messagebox
from authentication import Authentication
from core_gui import Core
from database import Database


# TODO: Lets stylize this like the main window.
class LoginGui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("300x200")

        self.create_widgets()

    def create_widgets(self):

        # Username entry
        self.lbl_username = tk.Label(self, text="Username:")
        self.lbl_username.grid(row=0, column=0, padx=5, pady=5)
        self.ent_username = tk.Entry(self)
        self.ent_username.grid(row=0, column=1, padx=5, pady=5)

        # Password entry
        self.lbl_password = tk.Label(self, text="Password:")
        self.lbl_password.grid(row=1, column=0, padx=5, pady=5)
        self.ent_password = tk.Entry(self, show="•")
        self.ent_password.grid(row=1, column=1, padx=5, pady=5)

        # Login button
        self.btn_login = tk.Button(self, text="Login", command=self.login_user)
        self.btn_login.grid(row=2, column=1, padx=5, pady=5)

        # Password confirmation for registration
        self.lbl_confirm_password = tk.Label(self, text="Confirm Password:")
        self.lbl_confirm_password.grid(row=3, column=0, padx=5, pady=5)
        self.ent_confirm_password = tk.Entry(self, show="•")
        self.ent_confirm_password.grid(row=3, column=1, padx=5, pady=5)

        # API Key entry for registration
        self.lbl_api_key = tk.Label(self, text="API Key")
        self.lbl_api_key.grid(row=4, column=0, padx=5, pady=5)
        self.ent_api_key = tk.Entry(self)
        self.ent_api_key.grid(row=4, column=1, padx=5, pady=5)

        # Register Button
        self.btn_register = tk.Button(self, text="Register", command=self.register_user)
        self.btn_register.grid(row=5, column=1, padx=5, pady=5)

        # For pressing 'Enter' after entering credentials.
        self.bind("<Return>", self.login_user_event)

    # Python wants to automatically login after binding 'Enter', this seems to work.
    def login_user_event(self):
        self.login_user()

    # Registers user by passing items in the entry boxes to register() which is handled by authentication. 
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

        success, message = Authentication.register(username, password, api_key)
        if success:
            messagebox.showinfo("Registration Success", message)
        else:
            messagebox.showerror("Registration Failure", message)

    # Logs in user by passing items in the entry boxes to login() which is handled by authentication. 
    def login_user(self):
        username = self.ent_username.get()
        password = self.ent_password.get()

        if username and password:
            auth = Authentication()
            token, api_key = auth.login(username, password)
            if token:
                messagebox.showinfo("Login", "Login successful.")
                self.api_key = api_key
                self.create_core_window(username, api_key)

            else:
                messagebox.showerror("Login", "Incorrect username or password.")
        else:
            messagebox.showerror("Login", "Both fields are required.")

    # Creates the GUI. TODO: refine this.
    def create_core_window(self, username, api_key):
        self.username = username
        self.api_key = api_key
        core_window = Core(self, username=username, api_key=api_key)
        self.withdraw()
        core_window.protocol("WM_DELETE_WINDOW", self.destroy_core_window)
        core_window.mainloop()

    # Closes the window after login has been successful. 
    def destroy_core_window(self):
        self.destroy()



def main():
    Database.setup_database()
    app = LoginGui()
    app.mainloop()

if __name__ == "__main__":
    main()