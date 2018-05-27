# %% QUESTAO A
N = int(input())
games = []
for  i in range(N):
    game = input()
    games.append(game)

for i in range(len(games) - 1):
    print(games[-i], end=', ')
print(games[-1], end='')

# %% QUESTAO B

C = int(input())
inv = []

for i in C:
    inv.append()

if "André" in inv:
    print("Cuidado!")
else:
    print("Seguro")

# %% QUESTAO C
F, P = input().split()
F, P = [int(F), int(P)]

cake = []
winner = ""

for j in range(F):
    cake.append(j)

for i in range(F):
    N, E = input().split()
    E = int(E)
    if P == cake[E]:
        winner = N
    cake.pop(E)

print(winner)

# %% QUESTAO D
N = int(input())

toys = input().split()
toys_ = toys

for i in range(5):
    toy, dir, steps = input().split()
    toy_pos = toys.index(toy)
    move = 0

    if dir == 'D':
        move = int(steps)
    else:
        move = int(steps) * -1

    # move the toy on the list
    toys.insert(toy_pos + move, toys.pop(toy_pos))

# diff checker
diff = 0
for j in range(N):
    if toys[j] != toys_[j]:
        diff += 1

print(diff)

# %% QUESTAO E REFAZIDA
N = int(input())
line = []

# get input
for _ in range(N):
    current_line = input()
    line.append(current_line)

# runs for every line (i)
for i in range(N):
    # runs for every char (j)
    for j in range(N):
        # checks if current char is a '.' underneath a 'o'
        if i > 0 and line[i][j] == '.' and line[i-1][j] == 'o':
            print('o', end="")
        # cheks if current char is a 'o' above a '.'
        elif N-1 > i and line[i][j] == 'o' and line[i+1][j] == '.':
            print('.', end="")
        # prints o resto
        else:
            print(line[i][j], end="")
    print()

# %% QUESTAO F
input_string = input().split('_')
for i in input_string:
    print(i.capitalize(), end='')
    
# %% QUESTAO G
H, P = input().split()

# creates towers and populates tower A
A = []
B = []
C = []

for i in range(int(H)):
    A.append(i+1)

# main loop

def move(n, source, target, auxiliary):
    if n > 0:
        # move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, auxiliary, target)

        # move the nth disk from source to target
        target.append(source.pop())

        # move the n - 1 disks that we left on auxiliary onto target
        move(n - 1, auxiliary, target, source)


move(int(P), A, C, B)
print("{} {} {}".format(len(A), len(B), len(C)))

# %% QUESTAO G-AMBIARRA
H, P = input().split()

A, B, C = [],[],[]
a,b,c = [],[],[]
x,y,z = [],[],[]
for i in range(int(H)):
    A.append(i+1)

def move(n, source, target, auxiliary):
    if n > 0:
        move(n - 1, source, auxiliary, target)
        a.append(len(A))
        b.append(len(B))
        c.append(len(C))
        target.append(source.pop())
        move(n - 1, auxiliary, target, source)

move(int(H), A, C, B)
for i in range(0,int(P)+1):
    x.append(a[i + 1] - a[i])
    y.append(b[i + 1] - b[i])
    z.append(c[i + 1] - c[i])

print("{} {} {}".format(int(H) + sum(x[:int(P)]), sum(y[:int(P)]), sum(z[:int(P)])))
