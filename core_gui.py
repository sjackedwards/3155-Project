import tkinter as tk
from tkcalendar import DateEntry
from api_call import get_flight_destinations

class Core(tk.Toplevel):
    def __init__(self, master=None, username=None, api_key=None):
        super().__init__(master)

        self.title("Flight Searcher")
        self.geometry("1000x650")
        self.username = username
        self.api_key = api_key

        self.create_widgets()

        for i in range(15):
            self.columnconfigure(i, weight=15)


    # TODO 1: Clean literally everything up. Lets make a second listbox for return flights instead of lumping them all into one.
    # TODO 2: I dont think I would like to book a flight that is leaving 45 mins after mine lands, lets implement a sort by time button.
    # TODO 3: Change some button names, think of some new buttons we can add, maybe sort buttons. Need to look into tkinter capabilities. 
    def create_widgets(self):
        # Welcome label
        self.lbl_username = tk.Label(self, text=f"Welcome, {self.username}")
        self.lbl_username.place(x=200, y=10)

        self.lbl_api_key = tk.Label(self, text=f"API KEY loaded:  {self.api_key}")
        self.lbl_api_key.place(x=400, y=10)

        # Carrier dropdown menu
        self.carrier_var = tk.StringVar(self)
        self.carrier_var.set("Any Airline")
        self.carrier_menu = tk.OptionMenu(self, self.carrier_var, "Any Airline", "Southwest", "Delta", "United Airlines", "jetBlue", "American Airlines", "Spirit")
        self.carrier_menu.config(width=22)
        self.carrier_menu.place(x=25, y=45)

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

        # # Flight listbox with scrollbar
        # self.flight_listbox = tk.Listbox(self, height=20, width=40)
        # self.flight_listbox.grid(row=4, column=0, padx=5, pady=5, columnspan=2, sticky='nsew')
        # self.scrollbar = tk.Scrollbar(self, command=self.flight_listbox.yview)
        # self.scrollbar.grid(row=4, column=2, sticky='ns', pady=5)
        # self.flight_listbox.config(yscrollcommand=self.scrollbar.set)

        # # Return flight listbox with scrollbar
        # self.ret_flight_listbox = tk.Listbox(self, height=20, width=40)
        # self.ret_flight_listbox.grid(row=4, column=3, padx=5, pady=5, columnspan=2, sticky='nsew')
        # self.ret_scrollbar = tk.Scrollbar(self, command=self.ret_flight_listbox.yview)
        # self.ret_scrollbar.grid(row=4, column=5, sticky='ns', pady=5)
        # self.ret_flight_listbox.config(yscrollcommand=self.ret_scrollbar.set)



        # # Submit button
        # self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        # self.submit_button.grid(row=5, column=0, padx=5, pady=5)

        # Exit button
        self.exit_button = tk.Button(self, text="Exit", command=self.close_app)
        self.exit_button.place(x=250, y=550)

        

    def close_app(self):
        quit()

    # TODO : Lets add a dropdown for # of people flying to pass to the api call.
    
    def submit(self):
        departure_date = self.start_date.get_date().strftime('%Y-%m-%d')
        return_date = self.end_date.get_date().strftime('%Y-%m-%d')
        departing_airport = self.departing_airport_var.get()
        arriving_airport = self.arriving_airport_var.get()
        carrier = self.carrier_var.get()

        try:
            result = get_flight_destinations(self.api_key, departing_airport, arriving_airport, departure_date, return_date, adults="1")
            self.update_flight_listbox(result, carrier)

        except Exception as e:
            self.flight_listbox.insert(tk.END, f"Error: {e}\n")

    # TODO 1: I want the list box to clear after every search.
    # TODO 2: Maybe attempt storing in a database again for better sorting functionality.
    # TODO 3: Sort buttons???
    # TODO 4: This looks like crap, but I dont think a method would make it any better. Maybe split this if we make a return flight list box.
    def update_flight_listbox(self, flight_data, carrier):
        flights = flight_data['data']
        for index, flight in enumerate(flights):
            departure_time = flight['legs'][0]['departure'][12:18]
            origin = flight['legs'][0]['origin']['alt_id']
            destination = flight['legs'][0]['destination']['alt_id']
            price = flight['price']['amount']
            airline = flight['legs'][0]['carriers'][0]['name']
            stops = flight['legs'][0]['stop_count']

            ret_departure_time = flight['legs'][1]['departure'][12:18]
            ret_origin = flight['legs'][1]['origin']['alt_id']
            ret_destination = flight['legs'][1]['destination']['alt_id']
            ret_price = flight['price']['amount']
            ret_airline = flight['legs'][1]['carriers'][0]['name']            
            
            if stops == 0:
                if carrier == airline:
                    self.flight_listbox.insert(tk.END, f"Flight {index+1} departure from {origin} to {destination} at {departure_time} with {airline} for ${price}. Non-stop.")
                    self.flight_listbox.insert(tk.END, f"----Return from {ret_origin} to {ret_destination} at {ret_departure_time} with {ret_airline} for ${ret_price}.")
                    self.flight_listbox.insert(tk.END, f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                else:
                    if carrier == 'Any Airline':
                        self.flight_listbox.insert(tk.END, f"Flight {index+1} departure from {origin} to {destination} at {departure_time} with {airline} for ${price}. Non-stop.")
                        self.flight_listbox.insert(tk.END, f"----Return from {ret_origin} to {ret_destination} at {ret_departure_time} with {ret_airline} for ${ret_price}.")
                        self.flight_listbox.insert(tk.END, f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            if stops == 1:
                stoploc = flight['legs'][0]['stops'][0]['alt_id']
                if carrier == airline:
                    self.flight_listbox.insert(tk.END, f"Flight {index+1} from {origin} to {destination} at {departure_time} with {airline} for ${price}. It has 1 stop in: {stoploc}")
                    self.flight_listbox.insert(tk.END, f"----Return from {ret_origin} to {ret_destination} at {ret_departure_time} with {ret_airline} for ${ret_price}.")
                    self.flight_listbox.insert(tk.END, f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                else:
                    if carrier == 'Any Airline':
                        self.flight_listbox.insert(tk.END, f"Flight {index+1} from {origin} to {destination} at {departure_time} with {airline} for ${price}. It has 1 stop in: {stoploc}")
                        self.flight_listbox.insert(tk.END, f"----Return from {ret_origin} to {ret_destination} at {ret_departure_time} with {ret_airline} for ${ret_price}.")
                        self.flight_listbox.insert(tk.END, f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else:
                if carrier == airline:
                    self.flight_listbox.insert(tk.END, f"Flight {index+1} from {origin} to {destination} at {departure_time} with {airline} for ${price}. It has multiple stops.")
                    self.flight_listbox.insert(tk.END, f"----Return from {ret_origin} to {ret_destination} at {ret_departure_time} with {ret_airline} for ${ret_price}.")
                    self.flight_listbox.insert(tk.END, f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                else:
                    if carrier == 'Any Airline':
                        self.flight_listbox.insert(tk.END, f"Flight {index+1} from {origin} to {destination} at {departure_time} with {airline} for ${price}. It has multiple stops.")
                        self.flight_listbox.insert(tk.END, f"----Return from {ret_origin} to {ret_destination} at {ret_departure_time} with {ret_airline} for ${ret_price}.")
                        self.flight_listbox.insert(tk.END, f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = Core(root, username="Demo", api_key="DEMO_API_KEY")
    root.mainloop()
