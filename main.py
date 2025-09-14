from pyscript import display

# string data
restaurant_name = "HamHamPangPang"
owner_name = "Carl Joseph Rufo"

#  data
year_established = 2018

#float data 
tax_rate = 0.08

# boolean data
has_delivery = True 

# list
product_names = ["Club Sandwhich", "BLT Sandwhich", "Grilled-Cheese Sandwhich", "Steak-Melt Sandwhich", "Egg-Salad Sandwhich"]
days = ["Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday"]
food_allergies = ["Egg", "Chicken", "Tomato", "dairy"]

# Dictionary
buisness_hours = {
    "open": "10:00 AM",
    "close": "11:00 PM"
}
menu_prices = {
    "Club Sandwhich": 250.67,
    "BLT Sandwhich": 230.67,
    "Grilled-Cheese Sandwhich": 205.67,
    "Steak-Melt Sandwhich": 367.67,
    "Egg-Salad Sandwhich": 245.67
}


# Display values
display(restaurant_name, target="restaurant_name")
display(owner_name, target="owner_name")
display(year_established, target="year_established")

display(f"Delivery Services Available?:{has_delivery}", target="delivery_status")
display(f"{buisness_hours['open']} - {buisness_hours['close']}", target="buisness_hours")

index = 1
for x in menu_prices:
    display(x, target=f"product{index}A")
    display(menu_prices[x], target=f"price{index}A")
    index += 1
