import tkinter as tk

class Core(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Terminal")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        self.console = tk.Text(self, wrap=tk.WORD, height=15, width=60)
        self.console.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_var)
        self.entry.bind('<Return>', self.submit)
        self.entry.pack(expand=True, fill=tk.X, padx=5, pady=5)

    def submit(self, event):
        user_input = self.entry_var.get()
        self.console.insert(tk.END, f"> {user_input}\n")
        self.entry_var.set("")

def main():
    app = Core()
    app.mainloop()

if __name__ == "__main__":
    main()