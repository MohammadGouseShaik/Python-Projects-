def count_capital_letters(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        capital_letters = sum(1 for char in text if char.isupper())
    return capital_letters
