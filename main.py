import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    # Start a loop to continuously take orders
    while True:
        # Ask user for the size of the sandwich
        choice = input("What size sandwich would you like? (Small, Medium, Large): ").lower()

        #Validate choice
        if choice not in recipes:
            print("Sorry, that's not a valid choice. Please try again.")
            continue

        # Extract cost and ingredients from data
        sandwich_cost = recipes[choice]["cost"]
        sandwich_ingredients = recipes[choice]["ingredients"]

        # Check if there are enough resources to make sandwich
        if sandwich_maker_instance.check_resources(sandwich_ingredients):
            print(f"That sandwich will cost ${sandwich_cost:.2f}. Please insert coins.")
            # Process coin input
            inserted_coins = cashier_instance.process_coins()

            # Check if the transaction is successful
            if cashier_instance.transaction_result(inserted_coins, sandwich_cost):
                #Make the sandwich
                sandwich_maker_instance.make_sandwich(choice, sandwich_ingredients)
                print(f"Enjoy your {choice} sandwich!")
            else:
                print("Transaction failed. Please try again.")
        else:
            print("Not enough resources to make that sandwich.")

        # Ask if user would like another sandwich
        another = input("Would you like to order another sandwich? (Yes/No): ").lower()
        if another != "yes":
            print("Goodbye! Have a nice day!")
            break

if __name__=="__main__":
    main()
