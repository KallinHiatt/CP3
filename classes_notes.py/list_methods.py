mylist = [ 4, 6, 8, 1.5, 5, 10, 7]

newlist = ["", "Argentina", "", "Brazil", "Chile", "", "Columbia", "", "Ecuador", "", "Venezuela"]

print(list(filter(None, newlist)))\

for num in mylist:
    newlist.append(num+1)

print(mylist)
print(newlist)
#this works, but there is a better way to create the code:

mylist = [ 4, 6, 8, 1.5, 5, 10, 7]
newlist = []

def increase(num):
    newlist.append(num+1)

print(list(map(increase, mylist)))

print(mylist)
print(newlist)

#Now we can also filter through values that we want:

def multiple(num):
    if num % 3==0:
        return num
    
print(list(filter(multiple, mylist)))
print(list(filter(lambda num: num %3, mylist)))