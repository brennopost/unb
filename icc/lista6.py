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
