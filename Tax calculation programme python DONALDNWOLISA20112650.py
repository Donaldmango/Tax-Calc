# Donald Nwolisa
# Tax Caculation
# 05/12/24

def get_tax_brackets():
    """Allow the user to input tax brackets dynamically."""
    brackets = []
    print("\nEnter tax brackets. Type 'done' when finished.")
    
    while True:
        try:
            bracket = input("Enter income threshold (or 'done' to finish): ")
            if bracket.lower() == 'done':
                break
            bracket_limit = float(bracket)
            tax_rate = float(input(f"Enter tax rate for income up to ${bracket_limit}: "))
            brackets.append((bracket_limit, tax_rate))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Ensure the brackets are sorted
    brackets.sort()
    return brackets

def calculate_tax(income, brackets):
    """Calculate tax based on progressive tax brackets."""
    tax = 0
    previous_bracket_limit = 0
    
    for bracket_limit, rate in brackets:
        if income > previous_bracket_limit:
            taxable_income = min(income, bracket_limit) - previous_bracket_limit
            tax += taxable_income * rate
            previous_bracket_limit = bracket_limit
        else:
            break
            
    return tax

def get_user_income():
    """Get income input from the user."""
    while True:
        try:
            income = float(input("Enter your income: $"))
            if income < 0:
                print("Income cannot be negative. Please enter a valid amount.")
            else:
                return income
        except ValueError:
            print("Invalid input. Please enter a numeric value for your income.")

def print_tax_details(income, tax, brackets):
    """Print a detailed tax breakdown."""
    print(f"\nDetailed Tax Calculation for Income: ${income:.2f}")
    
    previous_bracket_limit = 0
    for bracket_limit, rate in brackets:
        if income > previous_bracket_limit:
            taxable_income = min(income, bracket_limit) - previous_bracket_limit
            tax_in_bracket = taxable_income * rate
            print(f"Income taxed at {rate*100}% for ${taxable_income:.2f}: ${tax_in_bracket:.2f}")
            previous_bracket_limit = bracket_limit
        else:
            break
    
    print(f"\nTotal Tax: ${tax:.2f}")
    
def main():
    """Main function to run the tax calculator."""
    print("Welcome to the Tax Calculator!")
    
    brackets = get_tax_brackets()# Get dynamic tax brackets from the user
    income = get_user_income()     # Get income from the user
    
    tax = calculate_tax(income, brackets)  # Calculate the tax based on the inputted brackets
    print_tax_details(income, tax, brackets)  # Print detailed breakdown of the tax
    
    print(f"\nYour total tax on an income of ${income:.2f} is: ${tax:.2f}")

# Run the program
if __name__ == "__main__":
    main()
