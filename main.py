import sqlite3

def my_choose():
    print("Choose the number:\n1-Search name of country(1)\n2-Search number of country(2)")
    try:
        conn = sqlite3.connect(r"data\country.db")
        cursor = conn.cursor()

        num = int(input(":"))
        if num == 1:
            my_country = input("Enter name of country: ").capitalize()
            # Query the database for the country
            cursor.execute("SELECT code FROM country WHERE name = ?", (my_country,))
            result = cursor.fetchone()

            if result:
                print(f"The code for {my_country} is {result[0]}")
            else:
                print("Country not found.")
        elif num == 2:
            my_code = input("Enter number of code: ")

            # Query the database for the code
            cursor.execute("SELECT name FROM country WHERE code = ?", (my_code,))
            result = cursor.fetchone()

            if result:
                print(f"The country with code {my_code} is {result[0]}")
            else:
                print("Code not found.")
        else:
            print("Please enter a valid number!")
    except ValueError:
        print("Please enter a valid number!")
    finally:
        conn.close()

# Run the program
my_choose()