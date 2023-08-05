def computePay(h, r):
    if h < 40:
        gross_pay = h * r
    else:
        regular_pay = 40 * r
        overtime_pay = (h -40) * r * 1.5
        gross_pay = regular_pay + overtime_pay
    return gross_pay


hrs = input("Enter Hours:")
rate = input("Enter the rate")

h = float(hrs)
r = float(rate)

p = computePay(h, r)
print("Pay", p)