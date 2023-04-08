import sqlite3
import tkinter as tk
import os
from tkcalendar import DateEntry
from api_call import make_api_call

class Core(tk.Toplevel):
    def __init__(self, master=None, username=None, api_key=None):
        super().__init__(master)

        self.title("Flight Searcher")
        self.geometry("800x600")

        self.username = username
        self.api_key = api_key

        self.create_widgets()


    def create_widgets(self):
        self.lbl_username = tk.Label(self, text=f"Welcome, {self.username}")
        self.lbl_username.grid(row=0, column=0, padx=5, pady=5)

        self.carrier_var = tk.StringVar(self)
        self.carrier_var.set("Please Choose")
        self.carrier_menu = tk.OptionMenu(self, self.carrier_var, "Please Choose", "Southwest", "United Airlines", "American Airlines", "SPIRIT")
        self.carrier_menu.config(width=20)
        self.carrier_menu.grid(row=1, column=0, padx=5, pady=5)

        self.lbl_start_date = tk.Label(self, text="Depart Date:")
        self.lbl_start_date.grid(row=2, column=0, padx=5, pady=5)
        self.start_date = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.start_date.grid(row=2, column=1, padx=5, pady=5)

        self.lbl_end_date = tk.Label(self, text="Return Date:")
        self.lbl_end_date.grid(row=3, column=0, padx=5, pady=5)
        self.end_date = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.end_date.grid(row=3, column=1, padx=5, pady=5)

        self.lbl_departing_airport = tk.Label(self, text="Departing Airport:")
        self.lbl_departing_airport.grid(row=2, column=2, padx=5, pady=5)
        self.departing_airport_var = tk.StringVar()
        self.entry_departing_airport = tk.Entry(self, textvariable=self.departing_airport_var)
        self.entry_departing_airport.grid(row=2, column=3)

        self.lbl_arriving_airport = tk.Label(self, text="Arriving Airport:")
        self.lbl_arriving_airport.grid(row=3, column=2, padx=5, pady=5)
        self.arriving_airport_var = tk.StringVar()
        self.entry_arriving_airport = tk.Entry(self, textvariable=self.arriving_airport_var)
        self.entry_arriving_airport.grid(row=3, column=3)

        self.console = tk.Text(self, wrap=tk.WORD, height=15, width=60)
        self.console.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_var)
        self.entry.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=8, column=0, padx=5, pady=5)

        self.exit_button = tk.Button(self, text="Exit", command=self.close_app)
        self.exit_button.grid(row=8, column=1, padx=5, pady=5)

        self.lbl_api_key = tk.Label(self, text=f"API KEY loaded:  {self.api_key}")
        self.lbl_api_key.grid(row=9, column=1, padx=5, pady=5)

    def close_app(self):
        self.destroy()

    def submit(self):
        departure_date = self.start_date.get_date().strftime('%Y-%m-%d')
        departing_airport = self.departing_airport_var.get()
        arriving_airport = self.arriving_airport_var.get()

        db_conn = sqlite3.connect("local_app.db")
        cursor = db_conn.cursor()
        cursor.execute("SELECT api_key FROM users WHERE username = ?", (self.username,))
        api_key = cursor.fetchone()[0]
        db_conn.close()

        try:
            result = make_api_call(departure_date, departing_airport, arriving_airport, api_key)
            self.console.insert(tk.END, f"API call result: {result}\n")
        except Exception as e:
            self.console.insert(tk.END, f"Error: {e}\n")