import random

letter = ['a','b','c','d','e','f','g','h','i',
          'j','k','l','m','n','o','p','q','r']
number = ['1','2','3','4','5','6','7','8','9','0']
symbol = ['/','!','?','&']

j_letter = 6
i_number = 1
h_symbol = 2

password=''
for char in range(1,j_letter + 1):
    random_character = random.choice(letter)
    password += random.choice(letter)

for char in range(1,i_number + 1):
    random_num = random.choice(number)
    password += random.choice(number)

for char in range(1,h_symbol + 1):
    random_symbol = random.choice(symbol)
    password += random.choice(symbol)
print(f' your password = {password}')

passs =[] 

for char in range (1,j_letter +1) :
    passs.append(random.choice(letter))

for char in range (1,i_number + 1) :
    passs.append(random.choice(letter))

for char in range (1,h_symbol + 1):
    passs.append(random.choice(symbol))
print(passs)
random.shuffle(passs)


kata_sandi = ''
for char in passs:
    kata_sandi+= char
print(f' pasword kamu adalah {kata_sandi}')


