n = int(input())
arr = list(map(int, input().split()))
max_value = max(arr)

print(max(list(filter(lambda i: i!=max_value, arr))))