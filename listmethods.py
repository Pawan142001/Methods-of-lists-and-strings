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

String Methods :-
    
txt = "game is over"
x = txt.capitalize()
print(x)

txt = "Python is a Programming Language"
x = txt.casefold()
print(x)

txt = "Python"
x = txt.center(20)
print(x)

txt = "I like pizza,pizza is my favorite;izza pizza jizza"
x = txt.count("pizza")
print(x)

txt = "My name is Påwãn "
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

txt = "Namaste,aapka swagat hai"
x = txt.endswith(".")
print(x)

txt = "P\ta\tw\ta\tn"
x =  txt.expandtabs(2)
print(x)

txt = "Hello,welcome to india"
x = txt.find("welcome")
print(x)

txt = "Hello,welcome to india"
x = txt.find("e",5,8)
print(x)

txt = "For only {price:.2f} rupees!"
print(txt.format(price = 200))

txt = "Hello, welcome to india."
x = txt.index("welcome")
print(x)

txt = "Important234"
x = txt.isalnum()
print(x)

txt = "Important234"
x = txt.isalpha()
print(x)

txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)

txt = "2498"
x = txt.isdigit()
print(x)

a = "MyFile"
b = "Open002"
c = "2bars"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

txt = "hello guys!"
x = txt.islower()
print(x)

txt = "565543"
x = txt.isnumeric()
print(x)





