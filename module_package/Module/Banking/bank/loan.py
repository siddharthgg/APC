

def calculate_loan(principal, rate, years):
    interest = (principal * rate * years) / 100
    total_amount = principal + interest

    return interest, total_amount