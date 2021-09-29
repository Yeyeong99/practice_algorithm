n = int(input())

for i in range(n):
    a = input().split()
    a.reverse()
    b = " ".join(a)
    print(f"Case #{i+1}: {b}")
