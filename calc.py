def convert_to_words(num):
  """Converts a number into words.

  Args:
    num: The number to convert.

  Returns:
    The number in words.
  """

  ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
  thousands = ["", "thousand", "million", "billion", "trillion"]

  if num == 0:
    return "zero"

  words = ""
  while num > 0:
    hundreds = num // 100
    num %= 100
    if hundreds > 0:
      words = ones[hundreds] + " hundred " + words
    tens_digit = num // 10
    ones_digit = num % 10
    if tens_digit > 0:
      if tens_digit == 1:
        words += tens[ones_digit + 10]
      else:
        words += tens[tens_digit] + " " + ones[ones_digit]
    num %= 10
    if words and num > 0:
      words += " "
    words += thousands[num // 1000]
  return words

def main():
  number = int(input("Enter a number between 1 and 1000: "))
  print(f"{number} in words is: {convert_to_words(number)}")

if __name__ == "__main__":
  main()
