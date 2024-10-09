print('welcome to the rollercoaster')
print('\n')
print(30*'=')
print('\n')

height = int(input('your Height(cm) = '))
age = int(input('your age(th) = '))


if height > 120:
    if age > 18 :
        bill = 12
        print(bill)
    elif 12<age<18 :
        bill = 7
        print(bill)
    else:
        bill = 5
        print(bill)
    want_photo = input('add photo ? y or n = ')
    if want_photo == 'y' :
      bill +=3
      total_bill = bill
    print(total_bill)
else:
     print('you can not ride')
    

