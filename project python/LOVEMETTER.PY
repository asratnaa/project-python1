name1 = 'LYLyA'
name2 = 'NathaN'
combine = name1 + name2
print(combine)
combine_lower =combine.lower()
print(combine_lower)

# TRUE LOVE
T = combine_lower.count('t') 
R = combine_lower.count('r')
U = combine_lower.count('u') 
E = combine_lower.count('e') 
Total1 = (T+R+U+E)
print(Total1)

L = combine_lower.count('l') 
O = combine_lower.count('o') 
V = combine_lower.count('v')
E = combine_lower.count('e') 
Total2 = (L+O+V+E)
print(Total2)

love_score = (int(f'{Total1}{Total2}'))
print(love_score)
print(type(love_score))


if love_score < 10 or love_score> 90 :
    print(f"Your score is{love_score} , you go together like coke and mentos.")
elif 40<love_score<50 :
    print(f"Your score is {love_score}, you are alright together.")
else: 
    print (f"Your score is{love_score} .")

