import csv

year = 20

rows = []
#with open(str(3) + ".csv", 'r') as infile:
#with open("SvA" + str(year) + ".csv", 'r') as infile:
#with open("Iterative-score-users-20" + str(year) + ".csv", 'r') as infile:
#with open("ascore" + str(year) + "-" + str(year + 1) + ".csv", 'r') as infile:
#with open("20" + str(year) + "-to-20" + str(year + 1) + ".csv", 'r') as infile:
import math

with open("mega_lib_tpd.csv", 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        if len(row) > 0: #og 1
        #if len(row) > 1 and "score" not in row:# and float(row[2]) >= 3000: # og = 1
            rows.append(int(math.floor(float(row[1])))) #og = 1

    infile.close()

#print(rows[1])

count = 0# og = 0
bins = {}

delta = 5 # normally .04
while count <= 100: #normally 1

    bins[count] = []

    for x in rows:
        x = float(x)
        if x >= count and x < count + delta: #and x != 0.0 and x != 1.0:
            bins[count].append(x)

    count = round(count + delta,2)

#print(bins[24])
for y in bins:
    print(str(round(y, 2)) + ' ' + str(len(bins[y])))
#print('1 0')
total = 0
for y in bins:
    total = total + len(bins[y])
#print(total)
