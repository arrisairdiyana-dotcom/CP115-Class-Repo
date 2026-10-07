sales = int(input())
count = 0
record_days = 0
highest_sales = 0

while sales ! = 0 :
    count +=1
if count == 1 :
    record_days +=1 
    highest_sales = sales
elif sales > highest_sales :
    record_days +=1

sales = int(input())

print(count)
print(record_days)
