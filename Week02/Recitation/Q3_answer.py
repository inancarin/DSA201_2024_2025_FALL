f = open("bike_sales_100k.txt")

locations = set()
prices = {}
for line in f.readlines()[1:]:
    line = line.strip()
    info = line.split(",")
    loc = info[6]
    locations.add(loc) # it will handle uniqueness
    price = float(info[4])
    model = info[3]
    if model not in prices:
        prices[model] = [price]
    else:
        prices[model].append(price)

f.close()

print("Number of unique locations is", len(locations))

# calculate average price for each model
for k,v in prices.items():
    avg = sum(v) / len(v)
    prices[k] = avg

for i in range(5):
    maxVal = max(prices.values())
    for k,v in prices.items():
        if v == maxVal:
            maxKey = k
            print(k, v)
            break
    prices.pop(maxKey)