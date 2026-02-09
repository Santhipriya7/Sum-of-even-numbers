min = 1
max = 10
sum = 0
while min <= max:
    if min % 2 == 0:
        sum = sum + min 
        min = min + 1
    else:
        min = min + 1
print("Sum of even numbers from 1 to 10 is: ", sum)