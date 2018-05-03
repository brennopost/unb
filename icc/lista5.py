# %% QUESTA0 A
message = input()
crack = message.split()

for i in crack:
    print(i[2], end="")

# %% QUESTA0 B

message = input()
def p_translator(text):
    for i in text:
        if i.lower() in ['a','á','e','é','ê','i','í','o','ó','ô','ú','u',' ']:
            print(i, end="")
        else:
            print("p", end="")
p_translator(message)

# %% QUESTA0 C
A, B = input().split()
print("{x}".format(x="A" if max(A.lower(), B.lower()) == A else "B"))

# %% QUESTAO D
n = int(input())
p = 0
u = 0

def count(text, letter):
    n = 0
    for i in text:
        if i.lower() == letter:
            n += 1
    return n

for i in range(n):
    text = input()
    p += count(text, 'p')
    u += count(text, 'u')

print("{} {}".format(p, u))

# %% QUESTAO E
n = input().split('.')
print(n)
for i in n:
    print(i[0:3].title() + i[3:], end=".")

# %% QUESTAO F
a = input()
b = input()
def john(text):
    o = 0
    for i in "JOHN":
        o += text.count(i)
    return o
print("{} {}".format(john(a), john(b)))

# %% QUESTAO G
x = input()
for i in x:
    if i.isupper():
        print('U', end='')
    elif i.islower():
        print('L', end='')
    elif i == ' ':
        print('W', end='')
    else:
        print('D', end='')
