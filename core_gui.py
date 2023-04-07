import tkinter as tk
from tkcalendar import DateEntry

class Core(tk.Toplevel):
    def __init__(self, master=None, username=None):
        super().__init__(master)

        self.title("Flight Searcher")
        self.geometry("800x600")
        #self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.username = username

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


    def submit(self):
        command = self.entry_var.get()
        if command:
            self.proof_of_command(command)

    def proof_of_command(self, command):
        tokens = command.split()

        if len(tokens) < 3:
            self.console.insert(tk.END, "Invalid command format. Please use 'add num1 num2' or 'subtract num1 num2'\n")
            return

        operation, num1, num2 = tokens[0], tokens[1], tokens[2]

        try:
            num1, num2 = float(num1), float(num2)
        except ValueError:
            self.console.insert(tk.END, "Invalid numbers provided. Please use valid numbers.\n")
            return

        if operation.lower() == "add":
            self.add(num1, num2)
        elif operation.lower() == "subtract":
            self.subtract(num1, num2)
        else:
            self.console.insert(tk.END, f"Invalid operation '{operation}'. Please use 'add' or 'subtract'.\n")

    def add(self, num1, num2):
        result = num1 + num2
        self.console.insert(tk.END, f"Result: {result}\n")

    def subtract(self, num1, num2):
        result = num1 - num2
        self.console.insert(tk.END, f"Result: {result}\n")

