import csv

READ_PATH = 'C:\\Users\\mcse\\Documents\\GitHub\\US-fast-food\\datasets\\fast-food-rankings.csv'
WRITER_PATH = 'C:\\Users\\mcse\\Documents\\GitHub\\US-fast-food\\datasets\\rank-states.csv'
states= {}

with open(READ_PATH, 'r', newline='') as in_file:
    reader = csv.reader(in_file, delimiter = ',')
    header = reader.__next__()
    for row in reader:
        for c in range(len(row)):
            #check if on a ranking and add it
            if c % 2 != 0:
                if row[c-1] not in states:
                    states[row[c-1]] = {}
                states[row[c-1]][header[c]] = int(row[c])

favorites = {}

#find min
for state in states:
    #favorites[state] = min(states[state], key = states[state].get)
    fav = ""
    high = 51
    for store in states[state]:
        if states[state][store] < high:
            high = states[state][store]
            fav = store
        elif states[state][store] == high:
            fav += str("/"+store)
    favorites[state] = fav

favorites_items = favorites.items()
sorted_favorites = sorted(favorites_items)

with open(WRITER_PATH, 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["State", "Favorite"])
    for entry in sorted_favorites:
        writer.writerow([entry[0], entry[1]])
print(sorted_favorites)
