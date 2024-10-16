f = open("block_profile", "r")
lines = []
for line in f:
    lines.append(list(filter(lambda a: a != "" and  a != "\n", line.split(" "))))
total =0 
b = 0
for line in lines:
    total+=1
    if line[0] == "B":
        b+=1
print(b/total)