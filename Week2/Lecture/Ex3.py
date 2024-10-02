f = open("movies.txt")

s = set()
for line in f:
    line = line.strip() # removing all white-spaces (" ", "\t", "\n") from beginning and end
    info = line.split(", ")
    for elem in info[1:]:
        elem = elem.strip()
        s.add(elem)

f.close()
numMovies = len(s)
print("Number of distinct movies is", numMovies)

for i in range(5):
    minMovie = min(s)
    print(minMovie)
    s.remove(minMovie)
