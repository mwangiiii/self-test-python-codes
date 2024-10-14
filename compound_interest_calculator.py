#the interest that not only applies to the principle of a loan but also to the accumulated interest from previous periods.

#principle is the money set = P
# A = final amount 
# r = the interest rate
# n =number of times interest applied per time period
# t= number of time periods elapsed.


principle = 0
rate = 0
time = 0
#prompting the user to enter the principle value that can be a float
while  True:
    principle=float(input("Enter the principle value of the client: "))
    if principle<=0:
        print("Principle cannot be less than or equal to 0")
    else:
        break
print()

while  rate<=0 or True:
    rate=float(input("Enter the rate value of the client: "))
    if rate<=0:
        print("Rate cannot be less than or equal to 0")
    else:
        break
print()


while  time<=0 or True:
    time=int(input("Enter the time in years of the client to pay the loan: "))
    if time<=0:
        print("Time cannot be less than or equal to 0")
    else:
        break


print()
total=principle* pow((1+rate/100), time)
print(f"The total amount to be paid is: {total: .3f}")