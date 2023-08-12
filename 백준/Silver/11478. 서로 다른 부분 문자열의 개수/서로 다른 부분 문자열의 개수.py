S = input()
subset = set()
for i in range(len(S)) :
    for j in range(len(S)-i) :
        subset.add(S[j:(i+j+1)])
print(len(subset))