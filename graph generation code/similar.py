#check the similarity between bots to see if any are identical
import csv
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio() # check for exact meaning

users = {}


with open("mega_conserv.csv",encoding="utf-8") as infile:
    reader = csv.reader(infile)
    for row in reader:
        if row[0] not in users:
            users[row[0]] = [str(row[3])]
        else:
            users[row[0]].append(str(row[3]))


#content similarity

#for x in users:
 #   for y in users:
  #      if x == y:
   #         continue
    #    res = len(set(users[x]) & set(users[y])) / float(len(set(users[x]) | set(users[y]))) * 100

       # if res > 100: #percentage
        #    print(x + ' ' + y + ' == ' + str(res))

#name similarity
names = []
count = 0
with open('outNC.csv','w+',encoding="utf-8",newline="\n") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["FROM","TO","NUM"])
    for x in users:
        count += 1
        for y in users:
            if x != y:
                nam = 100*similar(x, y)
                if nam > 50:
                    #print(x + ' ' + y + ' == ' + str(nam)) for testing only
                    names.append(x)
                    writer.writerow([(x),(y),int(nam)])


                    
print(len(names))
print("Total Users: " + str(count))
