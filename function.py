"""
This script defines a function to calculate a discounted price
and then uses it to prompt the user for input and display the result.
"""

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount, but only if the
    discount percentage is 20% or higher.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after the discount, or the original price
               if the discount is less than 20%.
    """
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

if __name__ == "__main__":
    # This block of code will only run when the script is executed directly
    try:
        # Prompt the user to enter the original price
        original_price = float(input("Enter the original price: "))

        # Prompt the user to enter the discount percentage
        discount_percentage = float(input("Enter the discount percentage: "))

        # Calculate the final price by calling the function
        final_price = calculate_discount(original_price, discount_percentage)

        # Check if a discount was applied
        if final_price < original_price:
            print(f"A discount of {discount_percentage:.2f}% was applied.")
            print(f"The final price is: ${final_price:.2f}")
        else:
            print("No discount was applied.")
            print(f"The original price remains: ${original_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter numbers for the price and discount percentage.")