class Pizza:
    def _init_(self, name, crust, sauce, topping):
        self.name = name
        self.crust = crust
        self.sauce = sauce
        self.topping = topping
    def display_info(self):
        print(f"{self.name} - {self.crust} crust, {self.sauce} sauce, {self.topping} topping")


class PizzaOrder:
    def _init_(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def display_order(self):
        print("Your order:")
        for pizza in self.pizzas:
            pizza.display_info()


def main():
    print("Welcome to the Pizza Terminal App!")

    pepperoni_pizza = Pizza("Pepperoni", "Thin", "Tomato", "Pepperoni")
    bbq_pizza = Pizza("Barbecue", "Thick", "BBQ", "Chicken, Bacon")
    seafood_pizza = Pizza("Seafood", "Regular", "White Garlic", "Shrimp, Calamari, Mussels")

    order = PizzaOrder()

    while True:
        print("\nChoose a pizza to add to your order:")
        print("1. Pepperoni")
        print("2. Barbecue")
        print("3. Seafood")
        print("4. Checkout and exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            order.add_pizza(pepperoni_pizza)
        elif choice == "2":
            order.add_pizza(bbq_pizza)
        elif choice == "3":
            order.add_pizza(seafood_pizza)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid number.")

    order.display_order()
    print("Thank you for visiting!")

if __name__ == "__main__":
    main()