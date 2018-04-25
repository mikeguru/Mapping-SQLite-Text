import sqlite3
import time

def sqliteconnector():

    inventory_data_file = 'inventory-data.txt'

    conn = sqlite3.connect(str(time.localtime()[0]) + str(time.localtime()[1]) + str(time.localtime()[2]) + ".sqlite3")

    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Inventory_Data')
    cur.execute(
        'CREATE TABLE Inventory_Data (Inventory_ID INTEGER, Inventory_Name TEXT, Price FLOAT, Length REAL, Width REAL,  Date TEXT, Description TEXT)')

    with open(inventory_data_file, 'r') as fhand:

        # move to next
        next(fhand)

        item_counter = 0

        for line in fhand:

            file_data = line.split('\t')

            ID = file_data[0].strip()
            Name = file_data[1].strip()
            Price = file_data[2].strip()
            Length = file_data[3].strip()
            Width = file_data[4].strip()
            Date = file_data[5].strip()
            Description = file_data[6].strip()

            # Insert a row of data
            cur.execute(
                'INSERT INTO Inventory_Data ( Inventory_ID,  Inventory_Name, Price, Length, Width, Date, Description) VALUES (?, ?, ?, ?, ?, ?, ?)',
                (str(ID), str(Name), float(Price), int(Length), int(Width), str(Date), str(Description)))

            item_counter = item_counter + 1

            # Save upto 100
            if (item_counter > 100):
                # Save (commit) the changes
                conn.commit()
                break

        # Save (commit) the changes
        conn.commit()

    # Print command
    cur.execute('SELECT * FROM Inventory_Data')

    # Print in Line or in Table

    # Print in Line Format
    # print(cur.fetchall())

    # Print in Table Format
    for row in cur:
        print(row)

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

def main():
    sqliteconnector()

if __name__ == '__main__':
    main()
