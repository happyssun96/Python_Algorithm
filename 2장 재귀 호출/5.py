# 예제 5-1 최대공약수 구하기
def gcd(a,b):
    i = min(a,b)
    while True:
        if a % i == 0 and b % i ==0:
            return i
        i = i - 1
print(gcd(1,5)) # 1
print(gcd(3,6)) # 3
print(gcd(81, 27)) # 27

# 예제 5-2 유클리드 방식을 이용해 최대공약수 구하기
def gcd2(a,b):
    if b == 0:
        return a
    return gcd2(b, a % b)
print(gcd2(60, 24)) # 12
print(gcd2(81,27)) # 27

# 연습문제 5-1
# 피보나치 수열 문제
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-2) + fibo(n-1)
print(fibo(7)) # 13
