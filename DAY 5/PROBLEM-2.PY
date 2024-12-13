def is_palindrome_number(num):
    num_str = str(num)
    return num_str == num_str[::-1]
number = 123
print(f"Is {number} a palindrome? {is_palindrome_number(number)}")

