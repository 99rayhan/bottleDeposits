"""In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them.
In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit,and drink
containers holding more than one liter have a $0.25 deposit.

=> Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be received
for returning those containers. Format the output so that it includes a dollar sign and
always displays exactly two decimal places."""

#taking variable for deposit value
one_litre_bottle_deposit = 0.01
more_than_one_litre_bottle_deposit = 0.25

# Read the number of containers of each size
total_one_litre_bottle_return = int(input("How many one litre bottle have been deposited? "))
total_more_than_one_litre_bottle_return = int(input("How many more than one litre bottle have been deposited? "))

## Calculate the refund for each size

for_one_litre = total_one_litre_bottle_return*one_litre_bottle_deposit
for_more_than_one_litre = total_more_than_one_litre_bottle_return*more_than_one_litre_bottle_deposit

#total refund for returning bottles

total_refund = for_one_litre+for_more_than_one_litre

print(f"Your total refund will be ${total_refund:.2f}.")