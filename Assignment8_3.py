def sumofDigit(number):
    if number < 10:
        return number
    else:
        # Get the last digit and add it to the sum of the rest of the digits
        last_digit = number % 10
        rest_of_digits = number // 10
        return last_digit + sumofDigit(rest_of_digits)

# Input number
num = int(input())

# Calculate the sum of its digits using the recursive function
result = sumofDigit(num)

# Print the result
print("Sum of digits:", result)
