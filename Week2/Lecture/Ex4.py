f1 = open("hotels.txt")

d1 = {}
for line in f1.readlines():
    line = line.strip()
    info = line.split("\t")
    id = info[0]
    name = info[1]
    if id not in d1:
        d1[id] = name 
f1.close()

f2 = open("reviews.txt")
d2 = {}
for line in f2:
    line = line.strip()
    info = line.split("\t")
    id = info[1]
    rating = int(info[2])
    if id not in d2:
        d2[id] = [rating]
    else:
        d2[id].append(rating)

f2.close()

for k, v in d2.items():
    avg = sum(v) / len(v)
    d2[k] = avg

while len(d2) > 0:
    maxRating = max(d2.values())
    for k, v in d2.items():
        if v == maxRating:
            maxKey = k
            print(d1[maxKey], maxRating)
            break
    d2.pop(maxKey)