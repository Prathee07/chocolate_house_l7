import sqlite3

# It is a database connection ...

def connect_db():
    return sqlite3.connect('chocolate_house_l7.db')

# This function adds a seasonal flavor...

def add_seasonal_flavor(flavor_name, description):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Seasonal_flavor_offerings (flavor_name, description)VALUES (?, ?)''', (flavor_name, description))
    conn.commit()
    conn.close()
    print(f"Seasonal flavor '{flavor_name}' added.")

# This function is to add an ingredient to the inventory....

def add_ingredient(ingredient_name, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Ingredient_inventory(ingredient_name, quantity)VALUES (?, ?)''', (ingredient_name, quantity))
    conn.commit()
    conn.close()
    print(f"Ingredient '{ingredient_name}' with quantity {quantity} added.")

# This function is for customer suggestion / allergy concern...

def add_customer_suggestion(customer_name, suggested_flavor, allergy_concern):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Customer_suggestions (customer_name, suggested_flavor, allergy_concern)VALUES (?, ?, ?)''', (customer_name, suggested_flavor, allergy_concern))
    conn.commit()
    conn.close()
    print(f"Customer suggestion from '{customer_name}' added.")

# This function fetches all seasonal flavors....

def fetch_seasonal_flavors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Seasonal_flavor_offerings')
    flavors = cursor.fetchall()
    conn.close()
    return flavors

# This function fetches all ingredients..

def fetch_ingredients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Ingredient_inventory')
    ingredients = cursor.fetchall()
    conn.close()
    return ingredients

#This function fetches  all the customer suggestions

def fetch_customer_suggestions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Customer_suggestions')
    suggestions = cursor.fetchall()
    conn.close()
    return suggestions

#Main function to show or display the functionality....

def main():
    print("1. Add Seasonal Flavor")
    print("2. Add Ingredient")
    print("3. Add Customer Suggestion/Allergy Concern")
    print("4. View Seasonal Flavors")
    print("5. View Ingredients")
    print("6. View Customer Suggestions")
    print("7. Exit")

    while True:
        choice=input("\nEnter your choice: ")

        if choice=='1':
            flavor_name =input("Enter the flavor name: ")
            description=input("Enter description: ")
            add_seasonal_flavor(flavor_name, description)
        elif choice=='2':
            ingredient_name= input("Enter ingredient name: ")
            quantity =int(input("Enter quantity: "))
            add_ingredient(ingredient_name, quantity)
        elif choice=='3':
            customer_name = input("Enter customer name: ")
            suggested_flavor =input("Enter suggested flavor (or leave empty): ")
            allergy_concern= input("Enter allergy concern (or leave empty): ")
            add_customer_suggestion(customer_name, suggested_flavor, allergy_concern)
        elif choice=='4':
            flavors=fetch_seasonal_flavors()
            print("Seasonal Flavors:")
            for flavor in flavors:
                print(flavor)
        elif choice=='5':
            ingredients= fetch_ingredients()
            print("Ingredients Inventory:")
            for ingredient in ingredients:
                print(ingredient)
        elif choice =='6':
            suggestions= fetch_customer_suggestions()
            print("Customer Suggestions/Allergy Concerns:")
            for suggestion in suggestions:
                print(suggestion)
        elif choice=='7':
            print("Ohhh!!!Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again......!!!")

if __name__ == "__main__":
    main()
