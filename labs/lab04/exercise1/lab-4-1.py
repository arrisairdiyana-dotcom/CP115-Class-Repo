kwh = float(input())
if kwh >= 100:
    if kwh >= 200:
        fee = 0.75
    else:
        fee = 0.5
else:
    fee = 0.3
totalBill = fee * kwh
print(totalBill)
