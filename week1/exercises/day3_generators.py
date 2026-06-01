
# A function that prodeuces one value at a time- that way only one number exisits 
# in memory at a given moment

def count_up():
    i = 0
    while True:
        yield i  # what value should be produced here?
        i += 1
    

counter = count_up()  # create generator object
print(next(counter))  # ask for first value
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 


