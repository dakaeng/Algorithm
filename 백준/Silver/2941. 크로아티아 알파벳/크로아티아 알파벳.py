word = input()

cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
answer = 0
for i in cro_alpha :
    word = word.replace(i, ',')
print(len(word))