import sqlite3

# Connection to SQLite database

conn = sqlite3.connect('chocolate_house_l7.db')
cursor = conn.cursor()

# Creation of table for seasonal flavor offerings

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Seasonal_flavor_offerings(id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_name TEXT NOT NULL,
        description TEXT)
''')

# Creation of table for ingredient inventory

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ingredient_inventory (id INTEGER PRIMARY KEY AUTOINCREMENT,
        ingredient_name TEXT NOT NULL,
        quantity INTEGER NOT NULL)
''')

# Creation of table for customer flavor suggestions and allergy concerns

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customer_suggestions(id INTEGER PRIMARY KEY AUTOINCREMENT,
          customer_name TEXT NOT NULL,
         suggested_flavor TEXT,
           allergy_concern TEXT)
''')
conn.commit()
conn.close()
print("Database setup is completed.")

