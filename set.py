fruit={"apple","banana","orange","grapes","mango"}
food={"pizza","burger","pasta","orange","mango"}
print(fruit)
print(food)
for i in fruit:
    print(i)
for i in food:
    print(i)
#adding elements
fruit.add("pear")
food.add("taco")
print(fruit)
print(food)
fruit.remove("banana")
print(fruit)
if "banana" in fruit:
    print("banana is present")
else:
    print("banana is not present")
# set operations
union=fruit.union(food)
print("union of fruit and food:",union)
print("intersection of fruit and foods",fruit.intersection(food))
seperate=fruit.difference(food)
print("seperate elements in fruit and foods:",seperate)
symetric_difference=fruit.symmetric_difference(food)
print("symetric difference of fruit and food:",symetric_difference)
