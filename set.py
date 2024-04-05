#create a set
ages= {20,30,35,40,50}
print(ages)

#empty set & dictionary
empty_dict= {}
print(type(empty_dict))
empty_set= set()
print(type(empty_set))

#add item to set
numbers={1,2,3,3,4,5,5}
numbers.add(6)  
print(numbers)

#updating set & remove item 
companies= {'nike','zara'}
tech_companies={'google', 'saf'}
companies.update(tech_companies)   #update
companies.discard('nike')   #remove 
print(companies)

#set union = all elements in A and B
A={1,2,3,}
B={4,5,6}
print(A|B)  #method 1
print(A.union(B))  #method 2

#set intersection = common elements
A={4,6,3,}
B={4,5,6}
print(A & B)  #method 1
print(A.intersection(B))  #method 2

#difference btn sets = elements in A not in B
A={2,3,5}
B={1,2,6}
print(A - B)  #method 1
print(A.difference(B))  #method 2

#symmetric difference = all elements in A nd B without common elements
A={2,3,5}
B={1,2,6}
print(A ^ B)  #method 1
print(A.symmetric_difference(B))  #method 2 

#Check if two sets are equal =  have same elements
A={2,3,5}
B={1,2,6}
if A == B:
    print('are equal')
else:
    print('not equal')



