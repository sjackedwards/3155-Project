import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from api_call import get_flight_destinations
import json

def load_demo_result(file_name):
    with open(file_name, "r") as file:
        return json.load(file)
demo = False


bg_color = "#F5F5F5"
fg_color = "#333333"
button_bg = "#B3B3B3"
button_hover = "#8ACBF7"
button_font = ("Arial", 12)

class Core(tk.Toplevel):
    def __init__(self, master=None, username=None, api_key=None):
        super().__init__(master)

        self.title("Flight Search")
        self.geometry("835x550")
        self.configure(relief="groove")
        self.username = username
        self.api_key = api_key

        style = ttk.Style()
        style.theme_use("clam")  # You can also use other themes like 'aqua', 'default', 'alt'

        self.create_widgets()



    def create_widgets(self):
        
        style = ttk.Style()
        style.theme_use("clam")  # You can also use other themes like 'aqua', 'default', 'alt'

        # Welcome label
        self.lbl_username = tk.Label(self, text=f"Welcome, {self.username}")
        self.lbl_username.place(x=60, y=10)
        self.lbl_api_key = tk.Label(self, text=f"API KEY loaded:  {self.api_key}")
        self.lbl_api_key.place(x=240, y=10)

        # Carrier dropdown menu
        self.carrier_var = tk.StringVar(self)
        self.carrier_var.set("Choose Airline")
        self.carrier_menu = tk.OptionMenu(self, self.carrier_var, "Any", "Southwest", "Delta", "United Airlines", "jetBlue", "American Airlines", "Spirit")
        self.carrier_menu.config(width=22)
        self.carrier_menu.place(x=25, y=45)

        # Number of passengers
        self.pass_var = tk.StringVar(self)
        self.pass_var.set("# of Passengers")
        self.pass_menu = tk.OptionMenu(self, self.pass_var, "1", "2", "3", "4")
        self.pass_menu.config(width=22)
        self.pass_menu.place(x=235, y=45)

        # Departure date label and input
        self.lbl_start_date = tk.Label(self, text="Depart Date:")
        self.lbl_start_date.place(x=25, y=85)
        self.start_date = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.start_date.place(x=105, y=85)

        # Return date label and input
        self.lbl_end_date = tk.Label(self, text="Return Date:")
        self.lbl_end_date.place(x=25, y=110)
        self.end_date = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.end_date.place(x=105, y=110)

        # Departing airport label and input
        self.lbl_departing_airport = tk.Label(self, text="Departing Airport:")
        self.lbl_departing_airport.place(x=235, y=85)
        self.departing_airport_var = tk.StringVar()
        self.entry_departing_airport = tk.Entry(self, textvariable=self.departing_airport_var)
        self.entry_departing_airport.config(width= 10)
        self.entry_departing_airport.place(x=340, y=85)

        # Arriving airport label and input
        self.lbl_arriving_airport = tk.Label(self, text="Arriving Airport:")
        self.lbl_arriving_airport.place(x=235, y=110)
        self.arriving_airport_var = tk.StringVar()
        self.entry_arriving_airport = tk.Entry(self, textvariable=self.arriving_airport_var)
        self.entry_arriving_airport.config(width= 10)
        self.entry_arriving_airport.place(x=340, y=110)

        # Making tabbable area for TreeView widget
        self.notebook = ttk.Notebook(self)
        self.notebook.place(x=25, y=155, width=700, height=350)
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Departing Flights")
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Return Flights")

        # Creates TreeView widget inside the tabs
        self.dept_flight_tree = self.create_flight_treeview(self.tab1)
        self.create_scrollbar(self.tab1, self.dept_flight_tree)
        self.ret_flight_tree = self.create_flight_treeview(self.tab2)
        self.create_scrollbar(self.tab2, self.ret_flight_tree)




        # Set the padding for button height
        style.configure("b.TButton", padding=(5, 7), focuscolor=style.configure(".")["background"])
        style.configure("s.TButton", padding=(5, 10),focuscolor=style.configure(".")["background"])

        # Submit button
        self.submit_button = ttk.Button(self, text="Search Now", command=self.submit, style="s.TButton", width=15)
        self.submit_button.place(x=425, y=85)

        # Exit button
        self.exit_button = ttk.Button(self, text="Exit", command=self.close_app, style="b.TButton", width=8)
        self.exit_button.place(x=745, y=10)

        # Reset button
        self.reset_button = ttk.Button(self, text="Reset", command=self.reset, style="b.TButton", width=8)
        self.reset_button.place(x=670, y=10)

        # Info button
        self.info_button = ttk.Button(self, text="Info", command=self.open_info_window, style="b.TButton", width=8)
        self.info_button.place(x=595, y=10)

    def close_app(self):
        self.destroy()
        self.quit()

    def reset(self):
        self.destroy()
        new_app = Core(self.master, self.username, self.api_key)
        self.master.wait_window(new_app)

    def open_info_window(self):
        info_window = tk.Toplevel(self)
        info_window.title("Tutorial")
        info_window.geometry("400x300")

        info_label = tk.Label(info_window, text="How to use the flight search:", font=(16))
        info_label.pack(pady=10)

        instructions = ("1. Select the airline from the dropdown menu.\n"
                        "2. Choose the number of passengers.\n"
                        "3. Enter the departure and return dates.\n"
                        "4. Input the departure and arrival airport codes.\n"
                        "5. Click the 'Search Now' button to see the results.\n"
                        "6. Use the tabs to view departing and return flights.\n"
                        "7. Click column headers to sort the flight results.\n"
                        "8. Click 'Reset' to clear the results and start a new search.\n"
                        "9. Press 'Exit' to close the application.")

        instructions_label = tk.Label(info_window, text=instructions, justify=tk.LEFT, padx=10)
        instructions_label.pack()

        close_button = tk.Button(info_window, text="Close", command=info_window.destroy)
        close_button.pack(pady=10)


    
    def submit(self):
        departure_date = self.start_date.get_date().strftime('%Y-%m-%d')
        return_date = self.end_date.get_date().strftime('%Y-%m-%d')
        departing_airport = self.departing_airport_var.get()
        arriving_airport = self.arriving_airport_var.get()
        passengers = self.pass_var.get()
        carrier = self.carrier_var.get()

        try:
            if demo:
                result = load_demo_result("demo_results.json")
                self.update_flight_listbox(result, carrier)
            else:
                result = get_flight_destinations(self.api_key, departing_airport, arriving_airport, departure_date, return_date, passengers)
                self.update_flight_listbox(result, carrier)
        except Exception as e:
            print(e)

    def create_flight_treeview(self, parent):
        treeview = ttk.Treeview(parent, columns=("Airline", "Time", "Price", "Stops", "Flight Time"), show="headings", height=10)
        
        treeview.heading("Airline", text="Airline", command=lambda: self.treeview_sort_column(treeview, "Airline", False))
        treeview.heading("Time", text="Depart Time", command=lambda: self.treeview_sort_column(treeview, "Time", False))
        treeview.heading("Price", text="Price", command=lambda: self.treeview_sort_column(treeview, "Price", False))
        treeview.heading("Stops", text="Stops", command=lambda: self.treeview_sort_column(treeview, "Stops", False))
        treeview.heading("Flight Time", text="Flight Time", command=lambda: self.treeview_sort_column(treeview, "Flight Time", False))
        treeview.column("Airline", anchor=tk.W, width=200)
        treeview.column("Time", anchor=tk.W, width=100)
        treeview.column("Price", anchor=tk.W, width=100)
        treeview.column("Stops", anchor=tk.W, width=80)
        treeview.column("Flight Time", anchor=tk.W, width=80)

        treeview.place(x=10, y=10, width=650, height=270)

        return treeview
    
    def create_scrollbar(self, parent, tree):
        scrollbar = tk.Scrollbar(parent, command=tree.yview)
        scrollbar.place(x=660, y=12, height=270)
        tree.config(yscrollcommand=scrollbar.set)
        return scrollbar
    
    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        is_numeric = all(val.lstrip("$").replace(".", "", 1).isdigit() for val, k in l)

        if is_numeric:
            l.sort(key=lambda t: float(t[0].lstrip("$")), reverse=reverse)
        else:
            l.sort(key=lambda t: t[0], reverse=reverse)

        for index, (_, k) in enumerate(l):
            tv.move(k, '', index)

        for item_id in tv.get_children():
            tv.item(item_id, text='')

        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))


    # What has this become? Lets refine this a bit or get some good comments going. Maybe split this up?
    def update_flight_listbox(self, flight_data, carrier):

        flights = flight_data['data']

        for index, flight in enumerate(flights):

            airline = flight['legs'][0]['carriers'][0]['name']
            if carrier != "Any" and carrier != airline:
                continue

            departure_time = flight['legs'][0]['departure'][11:16]
            price = flight['price']['amount']
            airline = flight['legs'][0]['carriers'][0]['name']
            stops = flight['legs'][0]['stop_count']
            flt_time = flight['legs'][0]['duration']
            
            if stops == 1:
                stoploc = flight['legs'][0]['stops'][0]['alt_id']
                self.dept_flight_tree.insert("", tk.END, text=f"{index + 1}", values=(airline, departure_time, f"${price}", f"{stops} ({stoploc})", f"{flt_time}"))
            else:
                self.dept_flight_tree.insert("", tk.END, text=f"{index + 1}", values=(airline, departure_time, f"${price}", f"{stops}", f"{flt_time}"))

            ret_departure_time = flight['legs'][1]['departure'][11:16]
            ret_airline = flight['legs'][1]['carriers'][0]['name']
            ret_stops = flight['legs'][1]['stop_count']
            ret_flt_time = flight['legs'][1]['duration']
            
            if ret_stops == 1:
                ret_stoploc = flight['legs'][1]['stops'][0]['alt_id']
                self.ret_flight_tree.insert("", tk.END, text=f"{index + 1}", values=(ret_airline, ret_departure_time, f"${price}", f"{ret_stops} ({ret_stoploc})", f"{ret_flt_time}"))
            else:
                self.ret_flight_tree.insert("", tk.END, text=f"{index + 1}", values=(ret_airline, ret_departure_time, f"${price}", f"{ret_stops}", f"{ret_flt_time}"))

# For the demo window so I dont have to login
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = Core(root, username="Demo", api_key="DEMO_API_KEY")
    demo=True
    root.mainloop()


# TODO 3: Make save template button
# TODO 4: Stylize GUI if possible? Make an icon / borders / better buttons
