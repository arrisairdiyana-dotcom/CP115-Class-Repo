kwh = float(input())
if kwh <= 100:
    totalBill = 0.3 * kwh
else:
    if kwh > 100 and kwh <= 200:
        totalBill = 0.5 * kwh
    else:
        if kwh > 200:
            totalBill = 0.75 * kwh
print(totalBill)
