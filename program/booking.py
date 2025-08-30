import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from database import insert_flight


class BookingPage(tk.Frame):
    def __init__(self , parent , root , showFrame):
        super().__init__(parent)



     # Configure grid to center content
        for i in range(10):   # 10 rows total
            self.grid_rowconfigure(i, weight=1)
        for j in range(3):   # 3 columns total
            self.grid_columnconfigure(j, weight=1)
        


    # Booking page
        self.icon = tk.PhotoImage(file='airplane.png')
        tk.Label(self , text = 'Book your flight' ,
                font=('Helvetica', 18 , 'bold') , fg = '#000080' , anchor= 'center' ,
                image= self.icon , compound='left' 
                ).grid(row= 1 , column = 0 ,columnspan= 3 ,padx=0, pady=20)    
        
        self.name_entry = self.add_field('Name:' , 2)
        self.flightno_entry = self.add_field('Flight number:' , 3)
        self.departure_entry = self.add_field('Departure:' , 4)
        self.destination_entry = self.add_field('Destination:' , 5)
        self.date_entry = self.add_field('Date:' , 6)
        self.seatno_entry = self.add_field('Seat Number:' , 7)

        tk.Button(self , text='Submit' , width=12 , pady=8 ,font=('Helvetica', 12) , 
                fg='#ffffff' , bg="#000080" ,activebackground="#000050", anchor='center',
                    command= lambda: self.submit_and_back(showFrame, root)
                    ).grid(row=8 , column=0 ,columnspan= 2 , padx= 10 , pady=10)
    
    def add_field(self , label_text , row_num):
        tk.Label(self , text= label_text , font=('Helvetica', 14), anchor='e' 
                 ).grid(row=row_num , column= 0 , sticky='e' , padx= (20,5))
        entry = tk.Entry(self , font=('Helvetica', 13) , bg= "#c2bcbc" , width=25)
        entry.grid(row=row_num , column= 1 ,sticky='w', padx=5)
        return entry   

    def reserve(self):
        name = self.name_entry.get()
        flightno = self.flightno_entry.get()
        departure = self.departure_entry.get()
        destination = self.destination_entry.get()
        date = self.date_entry.get()
        seatno = self.seatno_entry.get()

        # validate all required
        if not all([name , flightno , departure , destination , date , seatno]) : 
            messagebox.showerror('Input error' , 'Please fill the missing field')
            return
        
        if not seatno.isdigit() or int(seatno) <= 0 :
            messagebox.showerror('Input error' , 'Seat number must be a positive integer')
            return
        
        try:
            datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            messagebox.showerror('Input error', 'Date must be in format DD-MM-YYYY')
            return
        
        print("Reservation Details:")
        print(f"Customer name: {name}")
        print(f"Flight number: {flightno}")
        print(f"From: {departure} to {destination}")
        print(f"Date: {date} , Seat number: {seatno}")

        try:
            insert_flight(name, flightno, departure, destination, date, int(seatno))
            messagebox.showinfo("Reservation", "Reservation made successfully!")
            return True
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred while saving the reservation: {e}")
            return False


    def submit_and_back(self , showFrame , root):
        if self.reserve():
            self.clear_fields()
            showFrame(root.pages["ReservationsPage"])

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.flightno_entry.delete(0, tk.END)
        self.departure_entry.delete(0, tk.END)
        self.destination_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.seatno_entry.delete(0, tk.END)
