A, B, C = map(int, input().split())

def solve(A, B) :
  if B == 1 :
    return A % C

  result = solve(A, B//2)
  if B % 2 == 0 :
    return (result * result) % C
  else :
    return (result * result * A) % C
print(solve(A, B))