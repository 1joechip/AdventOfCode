inp = "puzzle input here"
fishes = {}
for i in range(9):
    fishes[i] = inp.split(",").count(str(i))
# Change value in range for number of days (80 for pt1, 256 for pt2)
for i in range(256):
    zeros = fishes[0]
    for i in range(0, 8):
        fishes[i] = fishes[i+1]
    fishes[6] += zeros
    fishes[8] = zeros
    
print(sum([fishes[i] for i in range(9)]))
