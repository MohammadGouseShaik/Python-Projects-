def convert_number_to_words(number):
    if number < 0:
        return "minus " + convert_number_to_words(-number)
    if number == 0:
        return "zero"

    num_words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    words = ""
    if number < 20:
        words += num_words[number]
    elif number < 100:
        words += num_words[number // 10 * 10]
        if number % 10 != 0:
            words += " " + num_words[number % 10]
    elif number < 1000:
        words += num_words[number // 100] + " hundred"
        if number % 100 != 0:
            words += " " + convert_number_to_words(number % 100)
    elif number < 1000000:
        words += convert_number_to_words(number // 1000) + " thousand"
        if number % 1000 != 0:
            words += " " + convert_number_to_words(number % 1000)

    return words

print(convert_number_to_words(123))
