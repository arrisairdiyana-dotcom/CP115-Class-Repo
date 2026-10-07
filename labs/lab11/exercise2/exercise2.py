score = int(input())
total_a = 0
total_b = 0
turns = 1

while score != -1 :
    if score % 2 != 0 :
        total_a += 1
    else :
        total_b += 1

    turns += 1
    score = int(input())

if total_a > total_b :
    winner = "A"
if total_b > total_a :
    winner = "B"
else:
    winner = "Tie"

print(total_a)
print(total_b)
print(winner)
