def interest_rate_calculation(loan, interest_rate, years):
    return loan * (interest_rate / 100) * years

def hpp_calculation(price, service_fee):
    # Sepertinya rumus ini salah
    # hpp_calculation(price, loan, interest_rate, service_fee) - x
    # return price / (loan + interest_rate) + service_fee - x
    return price + service_fee

def instalment_calculation(loan, interest_rate, years):
    months = years * 12
    return (loan + interest_rate) / months