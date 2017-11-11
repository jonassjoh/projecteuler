def name_score(name, i):
    print(int(name[0]))

names = None
with open('names.in') as f:
    for line in f:
        line = line.split('","')
        line[len(line)-1] = line[len(line)-1][:-1]
        line[0] = line[0][1:]
        names = line

names.sort()
print(names[:10])
print(name_score(names[938], 938))
