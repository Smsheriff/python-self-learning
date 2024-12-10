print("Hello, World!")

age= 20
name= "sheriff"
print("name:", name ,"\nage:",age)


""" Dynamic Assignment in Python"""

a=10
a="sheriff"
print(a) 


x=10
y=-10
z=x-y
print(z)



def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input from the user
num = int(input("Enter your number: "))

# Call the function and display the result
result = check_odd_even(num)
print(f"The number {num} is {result}.")





a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
  
  def check_vote(age):
    if age >= 18:
        return "eligible"
    else:
        return "not eligible"

# Accept input from the user
n = int(input("Enter your age: "))
print(check_vote(n))




