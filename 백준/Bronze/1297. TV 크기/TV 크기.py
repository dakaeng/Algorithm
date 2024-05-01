D, H, W = map(int, input().split())

n = D**2 / (H**2 + W**2)
height = H * (n**0.5)
width = W * (n**0.5)

print(int(height), int(width))