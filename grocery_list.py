import sqlite3

#database set
ingredients = [
    "chicken",
    "pork",
    "ham",
    "meatball",
    "vegetarian",
    "headcheese",
    "mayo",
    "veggies",
    "pate",
    "egg"
]

ingredients = sorted(ingredients) 


connection = sqlite3.connect("ingredients.db")

cursor = connection.cursor()

cursor.execute("create table ingredient (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

for i in range(len(ingredients)):
    cursor.execute("insert into ingredient (name) values (?)",[ingredients[i]])
    print("Add ", ingredients[i])
    
connection.commit()
connection.close()