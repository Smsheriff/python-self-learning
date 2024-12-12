# count the number of even number btn 1 to 10

count=0
for i in range(1,11):
    if i%2==0:
        count=count+1
print(count)  


# count the odd and even number from 1 to 10

count_even=0
count_odd=0
for i in range(1,11):
    if i % 2 == 0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1     
print(count_even)
print(count_odd)
