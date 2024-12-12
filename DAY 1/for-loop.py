fruits=["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
    
    
for i in range(5):
    print(i)
    
    
for i in range(2,12,2):
    print(i)
    
    
number=[1,2,3,4,5]
total=0
for num in number:
    total+=num
print("total:",total)



number=[1,2,3,4,5,6,7,8,9]
for num in number:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
 


arr=[1,2,3,4,5]
res=sum(arr)
print(res)        



def diffrence(n):
    sum=0
    product=1
    string=str(n)
    
    for i in string:  
        sum = sum + int(i)         
        product = product * int(i)
    print(product-sum)
    
diffrence(123)