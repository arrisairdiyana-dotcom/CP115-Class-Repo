# Without \n - everything prints on one line
coffee = 3.50
muffin = 2.10
water = 1.05
quantity1 = 2
quantity2 = 3
quantity3 = 4
totalcoffee = coffee*quantity1
totalmuffin = muffin*quantity2
totalwater =  water*quantity3
subtotal = totalcoffee + totalmuffin + totalwater
tax = subtotal*0.06
total = subtotal+tax
print("========== RECEIPT ==========")
print("item\t price\tquantity total")
print(f"Coffee\t {coffee} \t{quantity1} {totalcoffee}")
print(f"Muffin\t {muffin} {quantity2} {totalmuffin}")
print(f"Water\t {water}  {quantity3} {totalwater}")
print(f"Subtotal \t {subtotal}")
print(f"Tax(6%) \t {tax}")
print(f"Total\t\t {total}")