# %% QUESTAO 1
# usando dicionários
N = int(input())
crit = []
ok = True

for _ in range(N):
    pair = input().split()
    crit.append(pair)

sentence = input()
dic = dict(crit)
crit_end = []

for i in dic:
    if i in sentence:
        crit_end.append(dic[i])
        ok = False
output = " ".join(crit_end)
if ok:
    print("Tude bem!")
else:
    print(output[:-1])

# %% QUESTAO 2
# usando dicionários
N = int(input())
depita = {}

for i in range(N):
    marmita = input()

    # find first ' ' then bind all characters till ' ' to *key*
    key = marmita[:marmita.index(' ')]
    # associate the rest of the characters, excluding ' ', to *meal*
    meal = marmita[marmita.index(' ') + 1:]
    # update the dictonary. if key is nonexistent, append
    depita.update([(key, meal)])

print(len(depita))
for i in depita:
    print(depita[i])

# %% QUESTAO 3
# "A primeira entrada consiste em um número N" -Toda questão de icc

# usando dict
N = int(input())
ex_machina = {}

for i in range(N):
    no_problemo, solution, difficulty = input().split()
    ex_machina.update([(int(difficulty), solution)])

for i in sorted(ex_machina.keys(), reverse=True):
    print(ex_machina[i],end='')

# usando tuple \\ nao funciona :(
N = int(input())
ex_machina = []

for i in range(N):
    deus = input().split()
    ex_machina.append(tuple(deus))

for i in sorted(ex_machina, key=lambda dif: dif[2], reverse=True ):
    print(i[1],end='')
