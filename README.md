# chocolate_house_l7
This is a Simple Python Application for a fictional chocolate house that uses SQLite to manage,
● Seasonal flavor offerings
● Ingredient inventory
● Customer flavor suggestions and allergy concerns

# Setup 
Make sure that u have Python 3.6 or later and SQLlite ,which will be installed along with it if we have python
where it can be verified using the command in command prompt as

python --version

Later create a directory where u need to store the files 
Example:
mkdir chocolate_house_l7

use that particular directory using the command,
cd chocolate_house_l7

Create a virtual Environment and activate it using commands:
python -m venv venv
venv\Scripts\activate

Create the files (database and the main application) by writing the code using VSCODE and run it .....! Thats it...........

we can aslo run it in command prompt too by setting up a path to particlar folder in our computer such as 
cd C:\Users\Pratheeksha\Desktop\chocolate_house_l7

# For first file
1) Run the database setup script in order to initialize the database using command:
   python database.py
where we will get the ouput as

Database setup is completed.

# For second file
2)Start the main application using the command as:
  python main_app.py
  
OUTPUT........
Here I have run this code 2 times and entered the inputs 


(venv) C:\Users\Pratheeksha\Desktop\chocolate_house_l7>python main_app.py
1. Add Seasonal Flavor
2. Add Ingredient
3. Add Customer Suggestion/Allergy Concern
4. View Seasonal Flavors
5. View Ingredients
6. View Customer Suggestions
7. Exit

Enter your choice: q
Invalid choice. Please try again......!!!

Enter your choice: 1
Enter the flavor name: Mango pulp
Enter description: A refreshing summer special
Seasonal flavor 'Mango pulp' added.

Enter your choice: 2
Enter ingredient name: Mango
Enter quantity: 4
Ingredient 'Mango' with quantity 4 added.

Enter your choice: 2
Enter ingredient name: Sugar
Enter quantity: 6
Ingredient 'Sugar' with quantity 6 added.

Enter your choice: 3
Enter customer name: Pradyumna
Enter suggested flavor (or leave empty): Mango Coconut
Enter allergy concern (or leave empty): Coconut
Customer suggestion from 'Pradyumna' added.

Enter your choice: 4
Seasonal Flavors:
(1, 'Gulkand chocolate', 'It gives flavour of Belgian dark chocolate')
(2, 'Mango pulp', 'A refreshing summer special')

Enter your choice: 5
Ingredients Inventory:
(1, 'Gulkand', 6)
(2, 'Chocolate', 8)
(3, 'Mango', 4)
(4, 'Sugar', 6)

Enter your choice: 6
Customer Suggestions/Allergy Concerns:
(1, 'Pratheeksha', 'Saffron', 'Turmeric')
(2, 'Pradyumna', 'Mango Coconut', 'Coconut')

Enter your choice: 7
Ohhh!!!Exiting the application.












  
