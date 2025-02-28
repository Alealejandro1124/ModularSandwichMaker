
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
      #Loop through each of the required ingredients
        for item, required_amount in ingredients.items():
            # Check if Machine has enough resources
            if self.machine_resources[item] < required_amount:
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
       """Deduct required ingredients from resources to make the sandwich."""
