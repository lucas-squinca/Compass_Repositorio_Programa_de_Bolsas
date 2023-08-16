for i in range(1, 11):
    print(f'i = {i}')

print('\n')

for j in range(10): # Como não demos início, partirá do 0 até o 9;
    print(f'j = {j}')

print('\n')

for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')
    print('\n')