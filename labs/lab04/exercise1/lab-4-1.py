kwh = float(input())
if kwh >= 100:
    if kwh > 100 and kwh <= 200:
        fee = 0.5
    else:
        if kwh > 200:
            fee = 0.75
else:
    fee = 0.3
totalBill = fee * kwh
print(totalBill)
