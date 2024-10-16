f = open("instr_profile", "r")
lines = []
for line in f:
    lines.append(list(filter(lambda a: a != "" and  a != "\n", line.split(" "))))
lines = list(filter(lambda a: a != [] and a !=['Profile', 'of', 'espresso', 'dc2'] and a!=['Total', 'number', 'of', 'accesses:', '3423933\n'],lines))
total = 0
for line in lines:
    total += int(line[0])

def sortFunc(a):
    return int(a[0])
lines.sort(reverse=True, key=sortFunc)

instructions = 0
tally = 0
for line in lines:
    tally += int(line[0])
    instructions += 1
    if tally >= 0.9 * (total):
        break

print(total)
print(instructions / 37232)