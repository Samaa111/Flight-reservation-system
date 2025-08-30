import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
from database import get_flights, delete_flight


class ReservationsPage(tk.Frame):
    def __init__(self, parent, root, showFrame):
        super().__init__(parent)
        self.root = root
        self.showFrame = showFrame

        # --- Configure grid ---
        for i in range(10):
            self.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.grid_columnconfigure(j, weight=1)

        # --- Title ---
        self.icon = tk.PhotoImage(file='program/airplane.png')
        tk.Label(
            self, text='Your Reservations',
            font=('Helvetica', 18, 'bold'),
            fg='#000080', anchor='center',
            image=self.icon, compound='left'
        ).grid(row=1, column=0, columnspan=3, pady=20)

        # --- Treeview ---
        columns = ('ID', 'Name', 'Flight No', 'Departure',
                   'Destination', 'Date', 'Seat')

        self.tree = ttk.Treeview(self, columns=columns, show='headings', height=10)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor='center')

        self.tree.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # --- Buttons ---
        btn_frame = tk.Frame(self, bg="#f8f9fa")
        btn_frame.grid(row=3, column=0, columnspan=3, pady=10)

        tk.Button(
            btn_frame, text='Edit', width=12, font=('Helvetica', 12),
            fg='#ffffff', bg="#000080", activebackground="#000050",
            command=self.on_edit
        ).grid(row=0, column=0, padx=10, pady=5)

        tk.Button(
            btn_frame, text='Delete', width=12, font=('Helvetica', 12),
            fg='#ffffff', bg="#FF0000", activebackground="#500000",
            command=self.on_delete
        ).grid(row=0, column=1, padx=10, pady=5)

        tk.Button(
            btn_frame, text='Back', width=12, font=('Helvetica', 12),
            fg='#ffffff', bg="#949494", activebackground="#474747",
            command=lambda: self.showFrame(self.root.pages['HomePage'])
        ).grid(row=0, column=2, padx=10, pady=5)

        # Load reservations initially
        self.refresh_table()

    # --------------------------
    # Methods
    # --------------------------

    def refresh_table(self):
        """Reload all reservations"""
        for row in self.tree.get_children():
            self.tree.delete(row)

        flights = get_flights()
        for flight in flights:
            self.tree.insert('', 'end', values=flight)

    def on_delete(self):
        """Delete selected reservation"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning('Warning', 'Please select a reservation to delete.')
            return

        flight_id = self.tree.item(selected_item[0])['values'][0]

        confirm = messagebox.askyesno('Confirm Deletion',
                                      f'Are you sure you want to delete flight ID {flight_id}?')
        if confirm:
            try:
                delete_flight(flight_id)
                messagebox.showinfo('Success', 'Reservation deleted successfully.')
                self.refresh_table()
            except Exception as e:
                messagebox.showerror('Error', f'Failed to delete reservation: {e}')

    def on_edit(self):
        """Open EditPage for selected reservation"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning('Warning', 'Please select a reservation to edit.')
            return

        flight_id = self.tree.item(selected_item[0])['values'][0]
        edit_page = self.root.pages['EditPage']
        edit_page.load_flight(flight_id)
        self.showFrame(edit_page)
