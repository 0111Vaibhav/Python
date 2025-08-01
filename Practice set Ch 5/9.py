
#Previous Questions Can Be answered by running th code in question 6

# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}
s = {8, 7, 12, "Harry", [1,2,3]} 
    
print(s) # it will show TypeError unhashable type: 'list' Because we cannot store a list inside a set