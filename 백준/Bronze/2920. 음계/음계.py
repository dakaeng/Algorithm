pitch = list(map(int, input().split()))
if pitch == sorted(pitch) :
    print('ascending')
elif pitch == sorted(pitch, reverse = True) :
    print('descending')
else :
    print('mixed')