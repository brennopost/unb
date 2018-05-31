# %% QUESTAO 1
# usando dicionários
'''
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

# %% QUESTAO 4
N = int(input())
pos = [0,0]
mov = {'N':0, 'S':0, 'L':0, 'O':0}
for i in range(N):
    dir, steps = input().split()
    mov[dir] += int(steps)
print("{} {} {} {}".format(max(mov['N'], mov['S']) - mov['N'],
                           max(mov['N'], mov['S']) - mov['S'],
                           max(mov['L'], mov['O']) - mov['L'],
                           max(mov['L'], mov['O']) - mov['O']))

# %% QUESTAO 5
# usar from collections import Counter para performance
text = input()


def getWords(inp):
    words = []
    buffer = []
    for i in inp:
        if i not in "., ":
            buffer.append(i.lower())
        else:
            if len(buffer) > 0:
                words.append("".join(buffer))
            buffer = []
    return words


wordList = getWords(text)
output = []
for i in wordList:
    if not any(i in x for x in output):
        output.append((i, wordList.count(i)))

#for i in output:
for i in sorted(output, key=lambda tup: tup[1], reverse=True):
    print("{} {}".format(i[0].capitalize(), i[1]))

# %% QUESTAO 6
N = int(input())
papers = []
for i in range(N):
    file, otherStuff = input().split(' ', 1)
    papers.append((file, otherStuff))

keywords = input().split()
for i in papers:
        if any(x in i[1] for x in keywords):
            print(i[0])

# %% QUESTAO 7
X, Y = input().split()
def ack(x, y):
    if x == 0:
        return y + 1
    elif y == 0:
        return ack(x - 1, 1)
    else:
        return ack(x -1, ack(x, y-1))

print(ack(int(X), int(Y)))

# %% QUESTAO 8
N = int(input())
plays = []
for i in range(N):
    player, index = input().split()
    plays.append((player, int(index)))

played = []
nxt_play = 0
lst_play = -1

while nxt_play not in played:
    played.append(lst_play)
    nxt_play = plays[nxt_play - 1][1]
    lst_play = nxt_play

print(plays[nxt_play][0])
'''
# %% QUESTAO 9
n = int(input())
activities = {}
for i in range(n):
    name, start, end = input().split()
    ## TODO verificar até onde é palavra e onde é horário
    start = start[:2] + start[2:] / 60
    end = end[:2] + end[2:] / 60

    activities.update({name:[start,end]})

print(activities)
