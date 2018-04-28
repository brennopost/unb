# %% QUESTAO A

x = int(input())
y = int(input())

if x < y:
    print("{} e menor que {}".format(x, y))
if x == y:
    print("{} e igual a {}".format(x, y))
if x > y:
    print("{} e maior que {}".format(x, y))

# %% QUESTAO B

y = []
for i in range(10):
    a = int(input())
    y.append(a)

print(max(y))
if max(y) % y[0] == 0:
    print(y[0])

# %% QUESTAO C

x = int(input())

if x > 0:
    while x > 1:
        print(x // 2  * 2)
        x -= 2
else:
    print(0)

# %% QUESTAO D

n = int(input()) // 2 * 2

def soma(x):
    if x == 0:
        return 0
    else:
        return x + soma(x - 2)

print(soma(n) - n)

# %% QUESTAO E



def even_square(x):
    if x > 1:
        print("{}^2 = {}".format(x, x ** 2))
        return even_square(x - 2)

while True:
    n = int(input())
    if n != 0:
        even_square(n // 2 * 2)
    else:
        break

# %% QUESTAO F
while True:
    a, b = input().split()
    a, b = [int(a), int(b)]

    if a > 0 and b > 0:

        def mdc(x, y):
            if y == 0:
                return x
            else:
                return mdc(y, x % y)

        print(int(abs((a * b)) / mdc(a, b)))
    else:
        break

# %% QUESTAO G
def concat(s1, s2):
    if not s1:
        return s2
    else:
        return s1[0:1] + concat(s1[1:], s2)

def inverse(s):
    if not s:
        return s
    else:
        return concat(inverse(s[1:]), s[0:1])

def prefix(s1, s2):
    if not s1 and s2:
        return True
    elif s1 == s1[0:1] + s1[1:] and s2 == s2[0:1] + s2[1:]:
        return prefix(s1[1:], s2[1:])
    else:
        return False

s1 = input()
s2 = input()

print(concat(s1, s2))
print(inverse(s1))
print(prefix(s1, s2))
