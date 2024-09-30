def main():
    cost_per_item = 19.99
    quantity = 5 
    # Part 1
    subtotal_cost = cost_per_item *quantity
    tax = subtotal_cost * 0.13
    total_cost = subtotal_cost + tax
 
    # Part 2
    print(f'cost_per_item = ${cost_per_item:0.2f}') # a sample for you to use for the other prices
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')

    # The Corrected Code
    # The Errors Are:
    # Trying to concatenate a float (investment) with a string, which will raise a TypeError.
    # The function main() is referenced but not defined.
    # It’s better to use a loop to avoid repeating the same line of code multiple times.
    # The :.2f in the f-string ensures the investment is displayed with two decimal places.

    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    
    # Apply interest 5 times for 5 years
    for _ in range(5):
        investment += investment * interest_rate
    
    # Use f-string for string formatting
    print(f'After 5 years, your investment will be worth {investment} dollars.')
if __name__ == "__main__":
    main()

