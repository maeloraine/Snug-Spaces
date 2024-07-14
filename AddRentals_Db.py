import sqlite3
from contextlib import closing

# Database Connection
def connect():
    conn = sqlite3.connect('Tenant_Data.db')
    conn.execute('PRAGMA foreign_keys = ON;')  # Enable foreign key constraints
    return conn


# Database Schema Management
def drop_table():
    conn = connect()
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS Tenant')
    c.execute('DROP TABLE IF EXISTS Rental')
    c.execute('DROP TABLE IF EXISTS Room')
    c.execute('DROP TABLE IF EXISTS Payment')
    conn.commit()
    conn.close()

def create_table():
    conn = connect()
    c = conn.cursor()

    # CREATE TENANT TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS Tenant (
            TenantID INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName TEXT NOT NULL,
            MiddleName TEXT,
            LastName TEXT NOT NULL,
            Birthday DATE NOT NULL,
            Email TEXT,
            ContactNo TEXT NOT NULL,
            Gender TEXT NOT NULL,
            Street TEXT NOT NULL,
            Barangay TEXT NOT NULL,
            City TEXT NOT NULL,
            Province TEXT NOT NULL,
            ZipCode TEXT NOT NULL
        )
    ''')

    # CREATE ROOM TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS Room (
            RoomID INTEGER PRIMARY KEY AUTOINCREMENT,
            RoomNo INTEGER NOT NULL UNIQUE,
            RoomRate DECIMAL(10, 2) NOT NULL DEFAULT 5000.00,
            RoomStatus TEXT NOT NULL 
        )
    ''')

    # CREATE RENTAL TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS Rental (
            RentalID INTEGER PRIMARY KEY AUTOINCREMENT,
            TenantID INTEGER NOT NULL,
            RoomID INTEGER,
            Start_Date DATE NOT NULL,
            End_Date DATE NOT NULL,
            FOREIGN KEY (TenantID) REFERENCES Tenant(TenantID) ON DELETE CASCADE ON UPDATE NO ACTION,
            FOREIGN KEY (RoomID) REFERENCES Room(RoomID) ON DELETE CASCADE ON UPDATE NO ACTION
        )
    ''')

    # CREATE PAYMENT TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS Payment (
            PaymentID INTEGER PRIMARY KEY AUTOINCREMENT, 
            TenantID INTEGER NOT NULL,
            Amount DOUBLE,
            PaymentDate DATE,
            FOREIGN KEY (TenantID) REFERENCES Tenant(TenantID) ON DELETE CASCADE ON UPDATE NO ACTION
        )
    ''')

    conn.commit()
    conn.close()


# Tenant Operations
def add_tenant(first_name, middle_name, last_name, birthday, email, contact_no,
               gender, street, barangay, city, province, zip_code, lease_start, lease_end):
    conn = connect()
    c = conn.cursor()

    try:
        # Add tenant
        c.execute('''
            INSERT INTO Tenant (FirstName, MiddleName, LastName, Birthday, Email, ContactNo, Gender,
                                Street, Barangay, City, Province, ZipCode) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (first_name, middle_name, last_name, birthday, email, contact_no, gender, street, barangay,
              city, province, zip_code))

        tenant_id = c.lastrowid  # Retrieve the last inserted TenantID

        # Add rental
        c.execute('''
            INSERT INTO Rental (TenantID, Start_Date, End_Date)
            VALUES (?, ?, ?)
        ''', (tenant_id, lease_start, lease_end))

        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()  # Roll back changes if an error occurs
        print(f"Error adding tenant and rental: {e}")
        tenant_id = None
    finally:
        conn.close()

    return tenant_id


def update_tenant(tenant_id, first_name, middle_name, last_name, birthday, email, contact_no, gender, street, barangay,
                  city, province, zip_code):
    conn = connect()
    c = conn.cursor()
    c.execute('''
        UPDATE Tenant
        SET FirstName = ?, MiddleName = ?, LastName = ?, Birthday = ?, Email = ?, ContactNo = ?,
            Gender = ?, Street = ?, Barangay = ?, City = ?, Province = ?, ZipCode = ?
        WHERE TenantID = ?
    ''', (
    first_name, middle_name, last_name, birthday, email, contact_no, gender, street, barangay, city, province, zip_code,
    tenant_id))

    conn.commit()
    conn.close()


def delete_tenant(tenant_id):
    conn = connect()
    c = conn.cursor()
    c.execute('DELETE FROM Tenant WHERE TenantID = ?', (tenant_id,))
    conn.commit()
    conn.close()

def fetch_total_tenants():
    conn = connect()
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM Tenant')
    total_tenants = c.fetchone()[0]
    conn.close()
    return total_tenants

def fetch_all_tenants():
    conn = connect()
    c = conn.cursor()
    c.execute('SELECT * FROM Tenant')
    records = c.fetchall()
    conn.close()
    return records


# Room Operations
def add_room(room_no, room_rate, room_status):
    try:
        conn = connect()
        c = conn.cursor()

        # Check if room_no already exists
        c.execute('SELECT RoomNo FROM Room WHERE RoomNo = ?', (room_no,))
        if c.fetchone():
            raise ValueError(f"Room number '{room_no}' already exists.")

        # Insert the new room
        c.execute('''
            INSERT INTO Room (RoomNo, RoomRate, RoomStatus) 
            VALUES (?, ?, ?)
        ''', (room_no, room_rate, room_status))

        room_id = c.lastrowid
        conn.commit()
        conn.close()
        return room_id
    except Exception as e:
        print(f"Error adding room: {e}")
        return None

def fetch_total_rooms():
    with closing(connect()) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM Room')
        total_rooms = cursor.fetchone()[0]
        return total_rooms

def fetch_available_rooms():
    with closing(connect()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Room WHERE RoomStatus = 'Available'")
        available_rooms = cursor.fetchall()
        return available_rooms

def fetch_available_roomNo():
    with closing(connect()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT RoomNo FROM Room WHERE RoomStatus = 'Available'")
        available_roomNo = cursor.fetchall()
        return [f"Room {room[0]}" for room in available_roomNo]

def fetch_occupied_rooms():
    with closing(connect()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Room WHERE RoomStatus = 'Occupied'")
        occupied_rooms = cursor.fetchone()[0]
        return occupied_rooms

def update_room_status(room_number, status):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Room SET RoomStatus = ? WHERE RoomNo = ?", (status, room_number))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating room status: {e}")
    finally:
        cursor.close()
        conn.close()

def fetch_pending_payments():
    # Assuming pending payments are derived from some rental conditions
    # Here just returning 0 for simplicity
    return 0

def update_room(room_id, room_no, room_rate, room_status):
    conn = connect()
    c = conn.cursor()
    c.execute('''
        UPDATE Room
        SET RoomNo = ?, RoomRate = ?, RoomStatus = ?
        WHERE RoomID = ?
    ''', (room_no, room_rate, room_status, room_id))
    conn.commit()
    conn.close()


def delete_room(room_id):
    conn = connect()
    c = conn.cursor()
    c.execute('DELETE FROM Room WHERE RoomID = ?', (room_id,))
    conn.commit()
    conn.close()

def fetch_all_rooms():
    conn = connect()
    c = conn.cursor()
    c.execute('''
        SELECT * FROM Room
        ORDER BY RoomID ASC
    ''')
    records = c.fetchall()
    conn.close()
    return records

def fetch_available_rooms():
    conn = connect()
    c = conn.cursor()
    c.execute('''
        SELECT * FROM Room
        WHERE RoomStatus = 'Available'
        ORDER BY RoomID ASC
    ''')
    records = c.fetchmany(5)  # Limit to 5 available rooms
    conn.close()
    return records

def fetch_one_room(room_no):
    conn = connect()
    c = conn.cursor()
    c.execute('''
            SELECT RoomNo, RoomRate, RoomStatus 
            FROM Room
            WHERE RoomNo = ?
        ''', (room_no,))
    records = c.fetchone()
    conn.close()
    return records

# def print_all_rooms():
#     conn = connect()
#     c = conn.cursor()
#     c.execute('SELECT RoomNo FROM Room')
#     rooms = c.fetchall()
#     conn.close()
#     print(f"All rooms in the Room table: {rooms}")
# print_all_rooms()

# Rental Operations
def update_rental(rental_id, tenant_id, lease_end):
    conn = connect()
    c = conn.cursor()
    try:
        c.execute('''
            UPDATE Rental
            SET TenantID = ?, End_Date = ?
            WHERE RentalID = ?
        ''', (tenant_id, lease_end, rental_id))

        conn.commit()
        print("Rental updated successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error updating rental: {e}")
    finally:
        conn.close()


def fetch_all_rental():
    conn = connect()
    c = conn.cursor()
    c.execute('''
        SELECT Rental.RentalID, Tenant.TenantID, Tenant.LastName, Tenant.FirstName, Tenant.MiddleName,
        Rental.Start_Date, Rental.End_Date
        FROM Rental
        INNER JOIN Tenant ON Rental.TenantID = Tenant.TenantID
    ''')
    records = c.fetchall()
    conn.close()
    return records
def fetch_one_rental(room_no):
    conn = connect()
    c = conn.cursor()
    try:
        c.execute('''
            SELECT Room.RoomNo
            FROM Rental
            INNER JOIN Room ON Rental.RoomID = Room.RoomID
            WHERE Room.RoomNo = ?
        ''', (room_no,))
        records = c.fetchone()
        print(f"fetch_one_rental - room_no: {room_no}, records: {records}")  # Debug print
    except sqlite3.Error as e:
        print(f"fetch_one_rental - error: {e}")  # Debug print
        records = None
    finally:
        conn.close()
    return records

def fetch_rental():
    conn = connect()
    c = conn.cursor()
    try:
        c.execute('''
            SELECT Rental.RentalID, Room.RoomNo, Tenant.FirstName, Tenant.MiddleName, Tenant.LastName, Rental.Start_Date, Rental.End_Date
            FROM Rental
            INNER JOIN Room ON Rental.RoomID = Room.RoomID
            INNER JOIN Tenant ON Rental.TenantID = Tenant.TenantID
        ''')
        rentals = c.fetchall()
        print(f"fetch_rental - rentals: {rentals}")  # Debug print
    except sqlite3.Error as e:
        print(f"fetch_rental - error: {e}")  # Debug print
        rentals = []
    finally:
        conn.close()
    return rentals


def delete_rental(rental_id):
    conn = connect()
    c = conn.cursor()
    c.execute('DELETE FROM Rental WHERE RentalID = ?', (rental_id,))
    conn.commit()
    conn.close()


# Payment Operations
def add_payment(tenant_ID, amount, lease_start, lease_end):
    conn = connect()
    c = conn.cursor()
    # Check if the tenant_ID exists in the Tenant table
    c.execute('SELECT COUNT(*) FROM Tenant WHERE TenantID = ?', (tenant_ID,))
    if c.fetchone()[0] == 0:
        print(f"TenantID {tenant_ID} does not exist.")
        conn.close()
        return  # Exit the function if tenant_ID is invalid

    # Insert the payment record into the Payment table
    c.execute('''
        INSERT INTO Payment (TenantID, Amount, PaymentDate)
        VALUES (?, ?, ?)
    ''', (tenant_ID, amount, lease_start))

    conn.commit()
    conn.close()
    print("Payment added successfully.")

def update_payment(payment_id, tenant_name, amount, payment_date):
    # Implement update_payment function in AddRentals_Db.py
    from AddRentals_Db import connect  # Assuming connect function is in AddRentals_Db.py

    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Payment
            SET TenantName = ?, Amount = ?, PaymentDate = ?
            WHERE PaymentID = ?
        ''', (tenant_name, amount, payment_date, payment_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error updating payment: {e}")
    finally:
        conn.close()

def fetch_payment():
    conn = connect()
    c = conn.cursor()
    c.execute('''
        SELECT Tenant.LastName, Tenant.FirstName, Tenant.MiddleName, Payment.Amount, Payment.PaymentDate
        FROM Payment
        INNER JOIN Tenant ON Payment.TenantID = Tenant.TenantID
    ''')
    records = c.fetchall()
    conn.close()
    return records

def payment_sum():
    conn = connect()
    c = conn.cursor()
    c.execute('''
        SELECT Tenant.LastName,  SUM(Payment.Amount) AS total_amount_paid
        FROM Tenant
        JOIN Payment on Tenant.TenantID = Payment.PaymentID
        GROUP BY Tenant.TenantID;
    ''')
    records = c.fetchall()
    conn.close()
    return records


# Initialize Tables
create_table()
#drop_table()