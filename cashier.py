class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        total = 0

        # Each Half-Dollars is 50 cents
        total += int(input("How many Half-Dollars?: ")) * 0.50
        # Each quarter is 25 cents
        total += int(input("How many quarters?: ")) * 0.25
        # Each dime is 10 cents
        total += int(input("How many dimes?: ")) * 0.1
        # Each nickel is 5 cents
        total += int(input("How many pennies?: ")) * 0.05
        # Each penny is 1 cent
        total += int(input("How many nickles?: ")) * 0.01
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##
