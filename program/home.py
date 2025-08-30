import tkinter as tk


class HomePage(tk.Frame):
    def __init__(self , parent , root , showFrame):
        super().__init__(parent)



     # Configure grid to center content
        for i in range(5):   # 5 rows total
            self.grid_rowconfigure(i, weight=1)
        for j in range(3):   # 3 columns total
            self.grid_columnconfigure(j, weight=1)

    # Homepage
        self.icon = tk.PhotoImage(file='airplane.png')
        tk.Label(self , text = 'Welcome to our flight reservation system.' ,
                font=('Helvetica', 18 , 'bold') , fg = '#000080' , anchor='center' ,
                image= self.icon , compound='left' 
                ).grid(row= 1 , column = 1 , columnspan= 3 ,padx=50, pady=20)
        tk.Button(self , text='Book flight' , width=20 , pady=10 ,font=('Helvetica', 12) , 
                fg='#ffffff' , bg="#000080" ,activebackground="#000050",
                    command= lambda : showFrame(root.pages["BookingPage"])  ).grid(row=2 , column=1 ,columnspan= 3 , padx=20)
        tk.Button(self , text='View Reservations' , width=20 , pady=10 ,font=('Helvetica', 12) , 
                fg='#ffffff' , bg="#000080" ,activebackground="#000050",
                    command= lambda : showFrame(root.pages["ReservationsPage"])  ).grid(row=3 , column=1 ,columnspan= 3 , padx=20 ,pady= 5)


