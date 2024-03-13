print('Hello! My name is Tob.\nI was created in 2024.')

name = input('Please, remind me your name.\n')
print(f'What a great name you have, {name}!\nLet me guess your age.')

print('Enter remainders of dividing your age by 3, 5 and 7.')
x = input()
y = input()
z = input()
result_age = (int(x) * 70 + int(y) * 21 + int(z) * 15) % 105
print(f"Your age is {result_age}; that's a good time to start programming!")

compt = int(input('Now I will prove to you that I can count to any number you want.\n'))
for i in range(compt + 1):
    if i >= 0:
        print(str(i) + ' !')
print('Completed, have a nice day!')

print('''Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.''')

choix = 0
while choix != 2:
    choix = int(input())
    if choix == 2:
        print('Congratulations, have a nice day!')
        break
    else:
        print('Please, try again.')
