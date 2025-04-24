import sqlite3

def create_table():
    count = 0
    if count == 0 :
        count += 1
        conn = sqlite3.connect("data/country.db")
        cursor = conn.cursor()

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS country
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            code INTEGER NOT NULL)
            """
        )
        conn.commit()
        conn.close()
    else:
       print("Table already exists.")
def insert_data(name, code):
    conn = sqlite3.connect("data/country.db")  # Fixed typo in database name
    cursor = conn.cursor()
    cursor.execute("INSERT INTO country (name, code) VALUES (?, ?)", (name, code))
    conn.commit()
    conn.close()

def save_in_database():  
    postal_dic = {}
    with open("data/code_postal.txt", "r") as file:
        lines = file.readlines()  # Fixed variable name
        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(" ", 1)
                if len(parts) == 2:
                    city, code = parts 
                    if parts:
                        postal_dic[city] = code                     
    return postal_dic

# Create the table before starting
create_table()
# Save data in the database
postal_dic = save_in_database()
for city, code in postal_dic.items():
    insert_data(city, code)