# 개미 전사 (p.220)

size = int(input())
dp = [0] * (size+1)
print(dp)
numbers = list(map(int, input().split()))
numbers.insert(0, 0)
print(numbers)

dp[1] = numbers[1]
print(dp)
for i in range(2, size+1):
    dp[i] = max(numbers[i]+dp[i-2], dp[i-1])

print(dp[size])
