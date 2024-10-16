import re
f = open("block_profile", "r")
lines = []
for line in f:
    lines.append(list(filter(lambda a:a == "F" or a == "?" or a == "taken\n" or a == "not", line.split(" "))))

print(lines.count(["F","?","taken\n"]))
print(lines.count(["F","?","not","taken\n"]))
f.close()
f = open("block_profile", "r")
nottaken = 0
taken = 0
for line in f:
    r = re.search("B\s\?\snot",line)
    if bool(r):
        nottaken +=1
    r = re.search("B\s\?\staken",line)
    if bool(r):
        taken +=1
print(taken)
print(nottaken)