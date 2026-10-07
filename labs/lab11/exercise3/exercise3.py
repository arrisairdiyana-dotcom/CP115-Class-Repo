number = int(input())
count = 0
biggest_jump = 0
prev = -1

while number != 0 :
    count =1
    prev = number
    number = int(input())

    if number != 0 :
     count +=1
     prev = number


print(count)
print(biggest_jump)
