
#for loop in python
people = ["Caleb", "Chris", "Jane"]
for x in people:
  print(x)


#range function
for x in range(2,6,2):
      print(x)

#else is satisfied when the while loop is done with the first condition
x=1
while x<=5:
    if x ==2:
        break
    print("python")
    x+=1
else:
    print("finished")

    #nested loop
adj =["blue", "red", "green", "yellow"]
cars = ["audi", "bmw", "subaru", "toyota"]
for x in adj:
    print(x)
    for y in cars:
        print(x,y)
        for z in range(3):
            print(x,y)

