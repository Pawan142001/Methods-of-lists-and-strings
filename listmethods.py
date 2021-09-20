List methods :-
thislist = ["North","South","East","West"]
thislist.append("Northeast")
print(thislist)

thislist = ["Forty","Fifty","eighty","Ninety"]
thislist.insert(2,"Twenty")
print(thislist)

thislist = ["dog","cat","bear"]
foods = ["bone","mouse","leaf"]
thislist.extend(foods)
print(thislist)

thislist = ["Goa","Ooty","Shimla"]
thislist.remove("Shimla")
print(thislist)

thislist = ["Goa","Ooty","Shimla"]
thislist.pop(2)
print(thislist)

games = ["Volleyball","Football","Basketball"]
games.clear()

games = ["Volleyball","Football","Basketball"]
x = games.copy()
print(x)

games = ["Volleyball","Football","Basketball"]
x = games.count("Football")
print(x)

games = ["Volleyball","Football","Basketball"]
x = games.index("Basketball")
print(x)

destination = ["Kolhapur","Igatpuri","Tryambakeshwar"]
destination.sort()
print(destination)

destination = ["Kolhapur","Igatpuri","Tryambakeshwar"]
destination.sort(reverse=True)
print(destination)

def myFunc(e) :
    return len (e)
bikes = ["Yamaha","Splendor","KTM"]
bikes.sort(key=myFunc)
print(bikes)

trees = ["Mango","Guava","Apple"]
trees.reverse()
print(trees)
