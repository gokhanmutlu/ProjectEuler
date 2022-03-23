# 20x20 lik yolda kaç farklı gidilebilir.

def fact(n):
    multiplication = 1
    while 0 < n:
        multiplication = multiplication * n
        n -= 1
    return multiplication

result = int((fact(40)/(fact(20)*fact(20))))
print(result)

