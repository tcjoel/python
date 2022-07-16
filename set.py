# set doesn't duplucate element
my_set = {"january", "february", "march", "march"}
print(my_set)
for element in my_set:
    print(element)
    
# to add element in the set we use the fonction add
my_set.add("april")
print(my_set)

# to remove element in the set() or list() but for list it just remove the first occurence of the element
my_set.remove("january")
print(my_set)

print(set([10, 2, 4, 2]))