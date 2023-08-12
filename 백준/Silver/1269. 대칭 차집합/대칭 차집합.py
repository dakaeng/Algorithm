A, B = map(int, input().split())
As = set(map(int, input().split()))
Bs = set(map(int, input().split()))

sub1 = (As - Bs)
sub2 = (Bs - As)
print(len(sub1) + len(sub2))