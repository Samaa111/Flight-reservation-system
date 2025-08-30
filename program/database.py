# Setup database connection
import sqlite3 as sq

def create_conn(): 
    return sq.connect('flights.db') 

def init_db():
    with create_conn() as conn:
        conn.execute('''
                        CREATE TABLE IF NOT EXISTS flights(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT ,
                            name TEXT NOT NULL ,
                            Flight_number TEXT NOT NULL ,
                            departure TEXT NOT NULL , 
                        destination TEXT NOT NULL , 
                        date TEXT NOT NULL , 
                        seat_number INTEGER NOT NULL 
                        );
                    ''')
        
def insert_flight(name , flightno , dep , des , date , seatno):
    with create_conn() as conn:
        conn.execute('''
                    INSERT INTO flights (name ,Flight_number , departure , destination , date , seat_number )
                    VALUES (?, ?, ?, ?, ?, ?)
                     ''', (name , flightno , dep , des , date , seatno))

def get_flights():
    with create_conn() as conn:
       cursor = conn.execute('SELECT * FROM flights')
       return cursor.fetchall()
    
def get_flight_by_id(flight_id):
    with create_conn() as conn:
       cursor = conn.execute('SELECT * FROM flights WHERE ID = ?', (flight_id,))
       return cursor.fetchone()
    
def delete_flight(flight_id):
    with create_conn() as conn:
        conn.execute('DELETE FROM flights WHERE ID = ?', (flight_id,))

def update_flight(flight_id , name, flight_number, departure, destination, date, seat_number):
    with create_conn() as conn:
        conn.execute('''
                    UPDATE flights
                    SET name = ?, Flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
                    WHERE ID = ?
                    ''', (name, flight_number, departure, destination, date, seat_number, flight_id))


init_db()