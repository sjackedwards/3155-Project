import json
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from api_call import API_call
from ttkthemes import ThemedStyle

# for testing GUI changes without logging in
def load_demo_result(file_name):
    with open(file_name, "r") as file:
        return json.load(file)
demo = False

class Core(tk.Toplevel):
    def __init__(self, master=None, username=None, api_key=None):
        super().__init__(master)

        self.title("Flight Search")
        self.geometry("760x550")    
        self.configure(relief='groove', background="#D9DDDC")
        self.username = username
        self.api_key = api_key
        self.create_widgets()

    def lookup_airport_code(self):
        airport_code = API_call.search_airport(self.entered_city.get())
        self.lbl_airport_code["text"] = f"Airport Code: {airport_code}"      

    def create_widgets(self):
        
        style = ThemedStyle()
        style.theme_use("clam")
        lbl_bg = "#D9DDDC"

        # Welcome label
        self.lbl_username = ttk.Label(self, text=f"Welcome, {self.username}", background=lbl_bg)
        self.lbl_username.place(x=25, y=10)
        self.lbl_api_key = ttk.Label(self, text=f"API KEY loaded:  {self.api_key}", background=lbl_bg)
        self.lbl_api_key.place(x=25, y=515)

        # Carrier dropdown menu
        self.carrier_var = tk.StringVar(self)
        #self.carrier_var.set("Choose Airline")
        self.carrier_menu = ttk.OptionMenu(self, self.carrier_var,"Choose Airline", "Any", "Southwest", "Delta", "United Airlines", "jetBlue", "American Airlines", "Spirit")
        self.carrier_menu.config(width=22)
        self.carrier_menu.place(x=25, y=45)

        # Number of passengers
        self.pass_var = tk.StringVar(self)
        self.pass_menu = ttk.OptionMenu(self, self.pass_var,"# of Passengers", "1", "2", "3", "4")
        self.pass_menu.config(width=22)
        self.pass_menu.place(x=235, y=45)

        # Departure date label and input
        self.lbl_start_date = ttk.Label(self, text="Depart Date:", background=lbl_bg)
        self.lbl_start_date.place(x=25, y=85)
        self.start_date = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.start_date.place(x=105, y=85)

        # Return date label and input
        self.lbl_end_date = ttk.Label(self, text="Return Date:", background=lbl_bg)
        self.lbl_end_date.place(x=25, y=110)
        self.end_date = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.end_date.place(x=105, y=110)

        # Departing airport label and input
        self.lbl_departing_airport = ttk.Label(self, text="Departing Airport:", background=lbl_bg)
        self.lbl_departing_airport.place(x=235, y=85)
        self.departing_airport_var = tk.StringVar()
        self.entry_departing_airport = tk.Entry(self, textvariable=self.departing_airport_var)
        self.entry_departing_airport.config(width= 10)
        self.entry_departing_airport.place(x=340, y=85)

        # Arriving airport label and input
        self.lbl_arriving_airport = ttk.Label(self, text="Arriving Airport:", background=lbl_bg)
        self.lbl_arriving_airport.place(x=235, y=110)
        self.arriving_airport_var = tk.StringVar()
        self.entry_arriving_airport = tk.Entry(self, textvariable=self.arriving_airport_var)
        self.entry_arriving_airport.config(width= 10)
        self.entry_arriving_airport.place(x=340, y=110)

        # Making tabbable area for TreeView widget
        self.notebook = ttk.Notebook(self)
        self.notebook.place(x=25, y=155, width=705, height=350)
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
        style.configure("b.TButton", padding=(5, 3), focuscolor=style.configure(".")["background"])
        style.configure("s.TButton", padding=(0, 12),focuscolor=style.configure(".")["background"])
        style.configure("r.TButton", padding=(0, 5),focuscolor=style.configure(".")["background"])
        style.configure("i.TButton", padding=(0, 0),focuscolor=style.configure(".")["background"])

        # Submit button
        self.submit_button = ttk.Button(self, text="Search Now", command=self.submit, style="s.TButton", width=15)
        self.submit_button.place(x=420, y=85)

        # Info button
        self.info_button = ttk.Button(self, text="Info", command=self.open_info_window, style="i.TButton", width=8)
        self.info_button.place(x=685, y=515)

        # Reset button
        self.reset_button = ttk.Button(self, text="Reset", command=self.reset, style="r.TButton", width=15)
        self.reset_button.place(x=420, y=45)

        # Exit button
        self.exit_button = ttk.Button(self, text="Exit", command=self.close_app, style="b.TButton", width=5)
        self.exit_button.place(x=685, y=10)

        # Lookup lable
        self.lbl_lookup = ttk.Label(self, text="Enter city to look up Airport Code", background=lbl_bg)
        self.lbl_lookup.place(x=535, y=57)
        
        # City label
        self.lbl_city = ttk.Label(self, text="City:", background=lbl_bg)
        self.lbl_city.place(x=535, y=85)

        # City entry
        self.city_var = tk.StringVar()
        self.entered_city = tk.Entry(self, textvariable=self.city_var)
        self.entered_city.config(width= 15)
        self.entered_city.place(x=570, y=85)

        # Lookup button
        self.lookup_button = ttk.Button(self, text="Lookup", command=self.lookup_airport_code, style="s.TButton", width=8)
        self.lookup_button.place(x=675, y=85)

        # Airport code label
        self.lbl_airport_code = ttk.Label(self, text="Airport Code:", background=lbl_bg)
        self.lbl_airport_code.place(x=535, y=110)

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
                result = API_call.get_flight_destinations(self.api_key, departing_airport, arriving_airport, departure_date, return_date, passengers)
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

        treeview.place(x=10, y=10, width=660, height=300)

        return treeview
    
    def create_scrollbar(self, parent, tree):
        scrollbar = tk.Scrollbar(parent, command=tree.yview)
        scrollbar.place(x=670, y=35, height=275)
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

    def update_flight_listbox(self, flight_data, carrier):

        flights = flight_data['data']

        for index, flight in enumerate(flights):

            airline = flight['legs'][0]['carriers'][0]['name']
            if carrier != "Any" and carrier != airline:
                continue

            # Probably can work this into the API call instead and return a tuple.
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
