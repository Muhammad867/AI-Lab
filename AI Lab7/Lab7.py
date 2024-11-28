class Packing():
    def pack(self) -> str:
        pass

class Wrapper(Packing):
    def pack(self) -> str:
        return "Wrapper"

class Bottle(Packing):
    def pack(self) -> str:
        return "Bottle"

class Item():
    def name(self) -> str:
        pass
    def packing(self) -> Packing:
        pass
    def price(self) -> float:
        pass

class Burger(Item):
    def packing(self) -> Packing:
        return Wrapper()
    def price(self):
        pass

class ColdDrink(Item):
    def packing(self) -> Packing:
        return Bottle()
    def price(self) -> float:
        pass

class VegBurger(Burger):
    def price(self) -> float:
        return 25.0
    def name(self) -> str:
        return "Veg Burger"

class ChickenBurger(Burger):
    def price(self) -> float:
        return 50.5
    def name(self) -> str:
        return "Chicken Burger"

class Coke(ColdDrink):
    def price(self) -> float:
        return 30.0
    def name(self) -> str:
        return "Coke"

class Pepsi(ColdDrink):
    def price(self) -> float:
        return 35.0
    def name(self) -> str:
        return "Pepsi"

class Meal:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def get_cost(self) -> float:
        cost = 0.0
        for item in self.items:
            cost += item.price()
        return cost
    def show_items(self):
        print(f"{'Item'.ljust(20)} {'Packing'.ljust(10)} {'Price'}")
        print("-" * 40)
        for item in self.items:
            print(f"{item.name().ljust(20)} {item.packing().pack().ljust(10)} ${item.price():.2f}")

class MealBuilder:
    def prepare_custom_meal(self, selected_items) -> Meal:
        meal = Meal()
        for item in selected_items:
            if item == "1":
                meal.add_item(VegBurger())
            elif item == "2":
                meal.add_item(ChickenBurger())
            elif item == "3":
                meal.add_item(Coke())
            elif item == "4":
                meal.add_item(Pepsi())
        return meal

def show_menu():
    print("Welcome to the Meal Builder!")
    print("Please choose your items:")
    print("1. Veg Burger - $25.0")
    print("2. Chicken Burger - $50.5")
    print("3. Coke - $30.0")
    print("4. Pepsi - $35.0")
    print("Enter the numbers of the items you want to order, separated by commas (e.g., 1,2,3).")

if __name__ == "__main__":
    show_menu()
    user_input = input("Your order: ")
    selected_items = user_input.split(",")

    meal_builder = MealBuilder()
    custom_meal = meal_builder.prepare_custom_meal(selected_items)

    print("\nYour Meal:")
    custom_meal.show_items()
    print(f"\nTotal Cost: ${custom_meal.get_cost():.2f}")
