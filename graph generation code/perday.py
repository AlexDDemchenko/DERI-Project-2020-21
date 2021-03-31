#check the similarity between bots to see if any are identical
import csv
import math
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
users = {}

#looking at time stamps
with open("mega_conserv.csv",encoding="utf-8") as infile:
    reader = csv.reader(infile)
    for row in reader:
        if row[0] not in users and hasNumbers(row[2]) and len(row[2]) >= 18 and len(row) == 4:
            #print(str(row[2].split(' ')[1]))
            #print(row[0])
            users[row[0]] = [str(row[2])]
        elif hasNumbers(row[2]) and len(row[2]) >= 18:
            users[row[0]].append(str(row[2]))


nope = """

dates = []
for x in users:
    switch = True
    for z in users[x]:
        p = z.split('-')
        #print(z)
        if len(p) != 3:
            continue
        y = int(p[0])*10000 + int(p[1])*100 + int(p[2])
        #print(y)
        if switch == True:
            maxT = y
            minT = y
            switch = False
        if y > maxT:
            maxT = y
        if y < minT:
            minT = y
    dates.append(math.floor((float(maxT) / 100 - 20200000)) - math.floor((float(minT) / 100 - 20200000)) )
above = 0
for t in dates:
    #if t != 0:
     #   above = above + 1
    #print(t)
#print(above)

for key in users:
    print(key)
    print(len(users[key]))
"""

gaps = []
nope = """
for key in users:
        last = 99999999
        for x in users[key]:
            month = x.split(" ")[0][5:7]
            time = x.split(" ")[1][0:5]
            #print(month + " " + time)
            if last != 99999999:
                print(time)
                gaps.append( int(time[0:2]*60 + [3:5]) - int(last) )
            last = time

    

print(gaps)

"""

days = {}

for key in users:
    days[key] = {}
    for x in users[key]:
        #print(days['criteria681'])
        #print(x[5:10])
        if x[5:10] in days[key]:
            days[key][x[5:10]].append(x[11:16])
        else:
            days[key][x[5:10]] = [x[11:16]]
#print(len(days['criteria681']['12-30']))

#print(days['jcmarbury'])
with open('outPC.csv','w+',encoding="utf-8",newline="\n") as outfile:
    writer = csv.writer(outfile)
    for y in days:
        
        #print(y) names
        liz = []
        for x in days[y]:
            #print(len(days[y][x]))
            liz.append(len(days[y][x]))
        
        if len(liz) > 0:
            writer.writerow([float(sum(liz)/len(liz))])
            #writer.writerow([float(min(liz)/60)])
            #print(sum(liz)/len(liz) * -1)
            #print(min(liz)*-1)


outfile.close()
