# %% QUESTAO A
N = int(input())
games = []
for  i in range(N):
    game = input()
    games.append(game)

games.reverse()
print(", ".join(games))

# %% QUESTAO B

C = int(input())
inv = []

for i in range(C):
    name = input()
    inv.append(name)

if "André" in inv:
    print("Cuidado!")
else:
    print("Seguro!")

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
toys_ = list(toys) # prevents referencing

for i in range(5):
    toy, dir, steps = input().split()
    toy_pos = toys.index(toy)
    move = 0

    if dir == 'D':
        move = int(steps)
    else:
        move = int(steps) * -1

    # move the toy on the list
    toys.insert((toy_pos + move) % N, toys.pop(toy_pos))

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
    line.append(list(current_line))

for _ in range(N):
    newline = []
    # runs for every line (i)
    for i in range(N):
        newline.append([])
        # runs for every char (j)
        for j in range(N):
            # checks if current char is a '.' underneath a 'o'
            if i > 0 and line[i][j] == "." and line[i-1][j] == 'o':
                newline[i].append('*')
            # cheks if current char is a 'o' above a '.'
            elif N-1 > i and line[i][j] == 'o' and line[i+1][j] == ".":
                newline[i].append('.')
            else:
                newline[i].append(line[i][j])
    line = newline[:]

for k in newline:
    for l in k:
        if l == '*':
            print('o', end='')
        else:
            print(l, end='')
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

# %% QUESTAO G binária
h, p = input().split()
h, p = int(h), int(p)
hanoi = [h,0,0]

if p > 2**h-1:
    p = 2**h-1

for x in range(p + 1):
    hanoi[(x&x-1)%3] -= 1
    hanoi[((x|x-1)+1)%3] += 1

if h % 2 == 0:
    print("{} {} {}".format(hanoi[0], hanoi[2], hanoi[1]))
else:
    print(" ".join([str(i) for i in hanoi]))
