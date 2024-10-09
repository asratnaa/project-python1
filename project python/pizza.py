print("Thank you for choosing Python Pizza Deliveries!")
size = input(f'size = ') # What size pizza do you want? S, M, or L
print(size)
add_pepperoni = input(f'paperoni = ') # Do you want pepperoni? Y or N
print(add_pepperoni)
extra_cheese = input(f'extra = ') # Do you want extra cheese? Y or N
print(extra_cheese)

if size == 'S':
  bill = 15
  if add_pepperoni == 'Y' :
    bill += 1 
elif size == 'M' :
  bill = 20
  if add_pepperoni == 'Y' :
    bill += 3 
else:
  bill = 25
  if add_pepperoni == 'Y' :
    bill += 3
if extra_cheese == 'Y' :
  bill += 1



print(f'your bill = ${bill}')