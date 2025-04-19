import sqlite3

def create_table():
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

def my_choose():
    print("Choose the number:\n1-Search name of country\n2-Search number of country")
    try:
        num = int(input(":"))
        if num == 1:
            my_country = input("Enter name of country: ").capitalize()
            postal_dic = save_in_database()
            if my_country in postal_dic:
                print(f"The code for {my_country} is {postal_dic[my_country]}")
                insert_data(my_country, postal_dic[my_country])
            else:
                print("Country not found.")
        elif num == 2:
            my_code = input("Enter number of code: ")
            postal_dic = save_in_database()
            for city, code in postal_dic.items():
                if code == my_code:
                    print(f"The country with code {my_code} is {city}")
                    insert_data(city, my_code)
                    break
            else:
                print("Code not found.")
        else:
            print("Please enter a valid number!")
    except ValueError:
        print("Please enter a valid number!")

# Create the table before starting
count = 0 
if count == 0:
    count += 1
    create_table()
else:
    print("Table already exists.")
# Save data in the database
postal_dic = save_in_database()
for city, code in postal_dic.items():
    insert_data(city, code)

# Run the program
my_choose()

