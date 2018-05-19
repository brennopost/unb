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
A, B = input().lower().split()
print("{x}".format(x="B" if B > A else "A"))

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
for i in n:
    print(i[0:2].title() + i[2:], end=".")

# %% QUESTAO E DENOVO
n = input()
m = []
for i in range(len(n)):
    if n[i-2] in "." and n[i-1] == ' ' or i == 0 or n[i-1] in ".":
        m.append(n[i].upper())
    else:
        m.append(n[i])
print("".join(m))

# %% QUESTAO F
a = input()
b = input()
def john(text):
    o = 0
    for i in "JOHN":
        o += text.count(i)
    return o
#print("{} {}".format(john(a), john(b)))
print("{} {}".format(john(a) - john(b), john(b)))

# %% QUESTA0 F DENOVO
a = input().upper()
b = input().upper()
x = [0, 0]
for i in a:
    if i in "JOHN":
        x[0] += 1
for i in b:
    if i in "JOHN":
        x[0] -= 1
        x[1] += 1

print("{} {}".format(x[0], x[1]))

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
