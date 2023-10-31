spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [ n["name"] for n in spicy_foods ]

def get_spiciest_foods(spicy_foods):
    return [ n for n in spicy_foods if n["heat_level"] > 5 ]

def print_spicy_foods(spicy_foods):
    for n in spicy_foods:
        name = n["name"]
        cuisine = n["cuisine"]
        spice = n["heat_level"] * "🌶"
        print(f"{name} ({cuisine}) | Heat Level: {spice}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for n in spicy_foods:
        if n["cuisine"] == cuisine:
            return n
    

def print_spiciest_foods(spicy_foods):
    spicy_list = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spicy_list)

def get_average_heat_level(spicy_foods):
    base = 0
    for n in spicy_foods:
        base += n["heat_level"]
    return base / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
