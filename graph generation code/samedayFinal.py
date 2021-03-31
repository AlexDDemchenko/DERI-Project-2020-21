#this isloates all data into shared days so the dataset is comparable
from difflib import SequenceMatcher
import csv
import math

users = {}
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio() # check for exact meaning

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


with open("mega_conserv.csv",encoding="utf-8") as infile:
    reader = csv.reader(infile)
    for row in reader:
        if row[0] not in users and hasNumbers(row[2]) and len(row[2]) >= 18 and len(row) == 4:
            users[row[0]] = {str(row[2][5:10]):[str(row[3])]}
            
            #print(users[row[0]][str(row[2][5:10])])
        elif hasNumbers(row[2]) and len(row[2]) >= 18:
            if str(row[2][5:10]) in users[row[0]]:

                #print(users[row[0]][str(row[2][5:10])])

                
                users[row[0]][str(row[2][5:10])] = users[row[0]][str(row[2][5:10])] + [str(row[3])]

                
                
                #print(users[row[0]][str(row[2][5:10])])
            else:
                users[row[0]][str(row[2][5:10])] = [str(row[3])]
names = []
with open('outSDC.csv','w+',encoding="utf-8",newline="\n") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["FROM","TO","NUM"])
    for x in users:
        for y in users:
            if x != y:
                for z in users[x]:
                    if z in users[y] and len(users[y]) > 10 and len(users[x]) > 10:
                        nam = 100*similar(users[x][z], users[y][z])
                        if nam > 30:
                            print(x + ' ' + y + ' == ' + str(nam)) #for testing only
                            names.append(x)
                            writer.writerow([(x),(y),int(nam)])




print(len(names))
