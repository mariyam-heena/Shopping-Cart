import csv
import os

def load_items():
    items = []
    if os.path.exists("cart.csv"):
        with open("cart.csv", "r", newline='') as file:
            reader = csv.reader(file)
            items = [row for row in reader]
    return items

def save_items(items):
    with open("cart.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(items)

def enter_data():
    with open("cart.csv","a") as f:
        w = csv.writer(f,lineterminator="\n")

        while True:
            item_id = int(input("Enter the ID of the item : "))
            name = input("Enter the name of the item : ").title().strip()
            price = float(input("Enter the price of the item : "))
            quantity = int(input("Enter the quantity of the item : "))
            discount = int(input("Enter the discount on the item : "))

            data = [item_id, name, price, quantity, discount]
            w.writerow(data)

            option = input("Do you want to shop more (y/n): ").lower().strip()
            if option == "n":
                print("Items added succesfully to cart.")
                break

def view():
    with open("cart.csv","r") as f:
        w = csv.reader(f)

        for i in w:
            print(f"Item ID: {i[0]}")
            print(f"Name of Item: {i[1]}")
            print(f"Price of Item: {i[2]}")
            print(f"Quantity of Item: {i[3]}")
            print(f"Discount on Item: {i[4]}%")
            print()

def delete_item():
    items = load_items()
    id = input("Enter ID of the Item you want to delete: ").strip()

    new_items = [item for item in items if item[0] != id]

    if len(new_items) < len(items): 
        save_items(new_items)
        print("\nItem removed successfully!\n")
    else:
        print("\nItem not found.\n")


def total_amount():
    with open("cart.csv","a") as f:
        w = csv.reader(f)
        sum = 0
        for i in w:
            sum += float(i[2])*float(i[3]) - float(i[2])*float(i[3])*(float(i[4])/100)
        else:
            print(f"Total payable amount after discount is {sum} INR.")
def cart():
    while True:
        print("""
    Welcome Dear Admin. What would you like to do?
    1)Shop for items.
    2)View Cart.
    3)Delete from cart.    
    4)Show total amount.   
    5)Exit.                    
    """)

        user = input("-----> ").strip()

        if user == "1":
            enter_data()
        elif user == "2":
            view()
        elif user == "3":
            delete_item()
        elif user == "4":
            total_amount()
        elif user == "5":
            print("Successfully exited the program.Please do visit us again.")
            break
        else:
            print("Invalid Input.Please try again.")

cart()
                    







