def currency_converter(amount, from_currency, to_currency):
    exchange_rate = {
        'USD': 1.0,
        'EUR': 0.86,
        'GBP': 0.76,
        'INR': 72.62
    }

    initial_amount = exchange_rate[from_currency] * amount
    final_amount = initial_amount / exchange_rate[to_currency]
    return final_amount

amount = float(input("Enter the amount: "))
from_currency = input("Enter the initial currency (USD, EUR, GBP, INR): ")
to_currency = input("Enter the target currency (USD, EUR, GBP, INR): ")

print(currency_converter(amount, from_currency, to_currency))
