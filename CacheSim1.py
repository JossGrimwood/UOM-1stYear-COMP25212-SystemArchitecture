import matplotlib.pyplot as plt
x = []
y = []

f = open("block_profile", "r")
lines = []
for line in f:
    lines.append(list(filter(lambda a:a != " " and a != "", line.split(" "))))

for cachesize in range(1, 500, 25):
    noPenalty = 0 
    penalty = 0
    cycle = 0
    cache = []
    for i in range(cachesize):
        cache.append(None)

    def searchCache(key): 
        global cycle, cachesize, cache
        for entry in cache:
            if entry == key:
                return True
        return False

    def addCache(key):  #cycle cache replacement
        global cycle, cachesize, cache
        cache[cycle] = key
        cycle += 1
        if cycle == cachesize:
            cycle = 0

    for line in lines:
        if line[0] == "B":
            hit = searchCache(line[2])
            if hit:
                if line.count("not") == 0:
                    noPenalty += 1  #cache hit and taken
                else:
                    penalty += 1    #cache hit but not taken
            else:
                if line.count("not") > 0:
                    noPenalty += 1  #no cache hit not taken
                else:
                    penalty += 1 #no cache hit is taken
                    addCache(line[2]) #no hit and taken so store in cache
        else:
            if line.count("not") > 0:
                noPenalty += 1  # not invariant and not taken
            else:
                penalty += 1    #not invariant is taken
    y.append(((2*penalty) + 3423933)/(3423933))
    x.append(cachesize)
    print(penalty)
plt.plot(x, y, color = 'r')

x2 = []
y2 = []
print("----------------------------------------------------")

for cachesize in range(1, 500, 25):
    noPenalty = 0 
    penalty = 0
    cycle = 0
    cache = []
    for i in range(cachesize):
        cache.append([None, 0])

    def searchCache(key, taken): 
        global cycle, cachesize, cache
        for entry in cache:
            if entry[0] == key:
                prediction = entry[1] >= 2
                if taken and entry[1] < 3:
                    entry[1] += 1
                elif not taken and entry[1] > 0:
                    entry[1] -= 1
                return taken == prediction
        cache[cycle] = [key, 2]
        cycle += 1
        if cycle == cachesize:
            cycle = 0
        return not taken


    for line in lines:
        if line[0] == "B":
            hit = searchCache(line[2], (True if line.count("not") == 0 else False))
            if hit:
                noPenalty += 1 
            else:
                penalty += 1 #no cache hit is taken
        else:
            if line.count("not") > 0:
                noPenalty += 1  # not invariant and not taken
            else:
                penalty += 1    #not invariant is taken
    y2.append(((2*penalty) + 3423933)/(3423933))
    x2.append(cachesize)
    print(penalty)
plt.plot(x2, y2, color = 'g')
plt.show()