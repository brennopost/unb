# %% QUESTAO A

n = int(input())
g = int(input())
while n != g:
    if g < n:
        print("O número correto é maior.")
    else:
        print("O número correto é menor.")
    g = int(input())
print("Parabéns! Você acertou.")


# %% QUESTAO B

n = []
i = int(input())
while i != 0:
    n.append(i)
    i = int(input())

print("{}\n{}\n{:.2f}".format(len(n), max(n), sum(n)/len(n)))

# %% QUESTAO C

t = int(input())

x = []
i = 0
while i < t:
    a, n = input().split()
    a, n = [int(a), int(n)]

    y = []

    for j in range(abs(n)):
        y.append(a)
        a += 1

    x.append(y)
    i += 1

for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j],end=" ")
    print("\n{}".format(sum(x[i])))

# %% QUESTAO D

n = int(input())
b = []

for i in range(n):
    x, y = input().split()
    x, y = [int(x), int(y)]

    if x % 2 == 0:
        x += 1

    a = 0
    for j in range(y):
        a += x + j*2
    print(a)
    b.append(a)

print("{}\n{}\n{:.2f}".format(max(b), min(b), (max(b)+min(b))/2))

# %% QUESTAO E
from math import factorial

n = int(input())

a = 1
b = 1
s = 0
if n > 2:
    for i in range(n - 2):
        s = a + b
        b = a
        a = s
print("{} {} {k} ".format(s, factorial(n), k = b if s % 2 == 0 else ""))

# %% QUESTAO F

n, m = input().split()
n, m = [int(n), int(m)]

def MDC(a ,b):
    if b == 0:
        return a
    else:
        return MDC(b, a % b)

print(MDC(n, m))

# %% QUESTAO G

n = int(input())

def getMinunumM(a):
    k = 0
    for i in range(n):
        k = n * i + 1
        for j in range(2, k - 1):
            p = k % j
            if p == 0:
                return i

print(getMinunumM(n))
