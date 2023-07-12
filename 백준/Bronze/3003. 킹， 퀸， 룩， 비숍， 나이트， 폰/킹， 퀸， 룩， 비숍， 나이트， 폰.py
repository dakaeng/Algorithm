values = list(map(int, input().split()))

pieces = [1, 1, 2, 2, 2, 8]
result = [pieces[i]-values[i] for i in range(len(values))]
print(*result)