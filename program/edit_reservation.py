import tkinter as tk
import tkinter.messagebox as messagebox
from database import get_flight_by_id , update_flight


class EditPage(tk.Frame):
    def __init__(self , parent , root , showFrame):
        super().__init__(parent)
        self.root = root
        self.showFrame = showFrame
        self.flight_id = None

    # --- Configure grid for EditPage to center content ---
        for i in range(10):   # 10 rows total
            self.grid_rowconfigure(i, weight=1)
        for j in range(3):   # 3 columns total
            self.grid_columnconfigure(j, weight=1)

    # ---Form fiels ---
    # Booking page
        self.icon = tk.PhotoImage(file='program/airplane.png')
        tk.Label(self , text = 'Edit your flight' ,
                font=('Helvetica', 18 , 'bold') , fg = '#000080' , anchor= 'center' ,
                image= self.icon , compound='left' 
                ).grid(row= 1 , column = 0 ,columnspan= 3 ,padx=0, pady=20)    
        
        self.name_entry = self.add_field('Name:' , 2)
        self.flightno_entry = self.add_field('Flight number:' , 3)
        self.departure_entry = self.add_field('Departure:' , 4)
        self.destination_entry = self.add_field('Destination:' , 5)
        self.date_entry = self.add_field('Date:' , 6)
        self.seatno_entry = self.add_field('Seat Number:' , 7)

        tk.Button(self , text='Cancel' , width=12 , pady=8 ,font=('Helvetica', 12) , 
                fg='#ffffff' , bg="#D30000" ,activebackground="#000050", anchor='center',
                    command= lambda : self.showFrame(root.pages['ReservationsPage'])
                    ).grid(row=8 , column=0 ,columnspan= 1 , pady=5)
        
        tk.Button(self , text='Update' , width=12 , pady=8 ,font=('Helvetica', 12) , 
                fg='#ffffff' , bg="#000080" ,activebackground="#000050", anchor='center',
                    command= self.update_record
                    ).grid(row=8 , column=1 ,columnspan= 3 , pady=10)

    
    def add_field(self , label_text , row_num):
        tk.Label(self , text= label_text , font=('Helvetica', 14), anchor='e' 
                 ).grid(row=row_num , column= 0 , sticky='e' , padx= (20,5))
        entry = tk.Entry(self , font=('Helvetica', 13) , bg= "#c2bcbc" , width=25)
        entry.grid(row=row_num , column= 1 ,sticky='w', padx=5)
        return entry   
    
    def load_flight(self , flight_id):
        self.flight_id = flight_id
        flight = get_flight_by_id(flight_id) # return by tuple

        if flight:
            self.name_entry.delete(0,tk.END)
            self.name_entry.insert(0 , flight[1])

            self.flightno_entry.delete(0,tk.END)
            self.flightno_entry.insert(0 , flight[2])

            self.departure_entry.delete(0,tk.END)
            self.departure_entry.insert(0 , flight[3])

            self.destination_entry.delete(0,tk.END)
            self.destination_entry.insert(0 , flight[4])

            self.date_entry.delete(0,tk.END)
            self.date_entry.insert(0 , flight[5])

            self.seatno_entry.delete(0,tk.END)
            self.seatno_entry.insert(0 , flight[6])

    def update_record(self):
        if self.flight_id is None:
            messagebox.showerror("Error" , "No flight loaded!")
            return

        try:
            update_flight(
                self.flight_id,
                self.name_entry.get().strip(),
                self.flightno_entry.get().strip(),
                self.departure_entry.get().strip(),
                self.destination_entry.get().strip(),
                self.date_entry.get().strip(),
                int(self.seatno_entry.get().strip())
            )
            messagebox.showinfo("Success", "Flight updated successfully!")
            self.showFrame(self.root.pages['ReservationsPage'])
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to update flight: {e}")  