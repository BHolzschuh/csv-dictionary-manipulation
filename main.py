import csv

#print top 5 sorting from rated value        
def print5r(_dict):
    '''Print statement prints a value passed to it.
        Takes 1 arg:
            dictionary object
        Sorts based on the first value of the dictionary (rated) and prints it to the screen'''
    t5 = (sorted(_dict.items(), key=lambda x: x[1], reverse=True)[:5])
    for i in t5:
        print(i[0])

#print top 5 sorting from gross value        
def print5g(_dict):
    '''Print statement prints a value passed to it.
        Takes 1 arg:
            dictionary object
        Sorts based on the second value of the dictionary (gross) and prints it to the screen'''
    t5 = (sorted(_dict.items(), key=lambda x: x[1][1], reverse=True)[:5])
    for i in t5:
        print(i[0])

#declare dictionaries
cast = {}
gross = {}
rated = {}
actor = {}
director = {}

#open casts csv and create dictionary
creader = csv.reader(open("imdb-top-casts.csv", "r"))
for x in creader:
    cast[(x[0], x[1])] = [x[2], x[3], x[4], x[5], x[6], x[7]]
    
#open gross csv and create dictionary    
greader = csv.DictReader(open("imdb-top-grossing.csv", "r"))
for i,x in enumerate(greader):
    if i != 0:
        gross[(x['Title'], x['Year'])] = float(x['USA Box Office'])
        
#open rated csv and create dictionary   
frated = csv.DictReader(open("imdb-top-rated.csv", "r"))
for i,x in enumerate(frated):
    if i != 0:
        rated[(x['Title'], x['Year'])] = float(x['IMDb Rating'])
        
#Initialize top actor dictionary with first value for rated and second for grossing
for key in cast:
    director[cast[key][0]] = [0, 0]

#Increment dict every time director name is in top rated    
for key in rated:
    if key in cast:
        director[cast[key][0]][0] += 1
        
#Increment dict every time director name is in top grossing        
for key in gross:
    if key in cast:
        director[cast[key][0]][1] += 1

#Initialize top actor dictionaries listing every movie theyve been in
for key in cast:
    for name in cast[key][1:]:
        if name not in actor:
            actor[name] = [0, 0, [key]]
        elif name in actor:
            actor[name][2].append(key)

#Increment dict every time actor name is in top rated          
for key in rated:
    if key in cast:
        for name in cast[key][1:]:
            if name in actor:
                actor[name][0] += 1

#Add $$ each actor made from each movie in top grossing                
for key in gross:
    if key in cast:
        money = gross[key]
        for i,name in enumerate(cast[key][1:]):
            if name in actor:
                if i==0:
                    actor[name][1] += 16*money/31
                elif i==1:
                    actor[name][1] += 8*money/31
                elif i==2:
                    actor[name][1] += 4*money/31
                elif i==3:
                    actor[name][1] += 2*money/31
                else:
                    actor[name][1] += money/31

#print top 5 for rated and gross from actors and directors
print("Top 5 Directors in Rated:")
print5r(director)
print("\nTop 5 Directors in Grossing:")    
print5g(director)
print("\nTop 5 Actors in Rated:")
print5r(actor)
print("\nTop 5 Actors in Grossing")
print5g(actor)