def sum_of_digits_recursive(number):
    if number < 10:
        return number
    else:
        # Get the last digit and add it to the sum of the rest of the digits
        last_digit = number % 10
        rest_of_digits = number // 10
        return last_digit + sum_of_digits_recursive(rest_of_digits)

# Input number
num = 12345

# Calculate the sum of its digits using the recursive function
result = sum_of_digits_recursive(num)

# Print the result
print("Sum of digits:", result)
