import tkinter as tk
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditPage


def showFrame(frame):
    frame.tkraise()

    if hasattr(frame, "refresh_table"):
        frame.refresh_table()

root = tk.Tk()
root.title('Flight Reservation System') 
root.configure(bg= "#f8f9fa")
root.geometry('700x500')
icon = tk.PhotoImage(file='program/airplane.png')
root.iconphoto(True , icon)

# Create frames
container = tk.Frame(root)
container.pack(side='top' , fill='both' , expand=True)
root.pages = {}

for pageClass in (HomePage ,BookingPage ,ReservationsPage ,EditPage) : 
    page = pageClass(container , root , showFrame)
    root.pages[pageClass.__name__] = page
    page.grid(row=0 , column =0 , sticky = 'nsew')


showFrame(root.pages["HomePage"])
root.mainloop()