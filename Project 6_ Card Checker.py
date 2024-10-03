
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    while True:
      card_number = input("Enter your 16-digit card number with dashes: ")
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)
      if verify_card_number(translated_card_number):
        if card_number == "0":
          print('INVALID!')
        else:
          print('VALID!')
          print("Card has been accepted!")
          break
      else:
          print('INVALID!')


main()
