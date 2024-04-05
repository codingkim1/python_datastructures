#dictionary methods
cars = {'toyota': 'premio', 'nissan': 'xtrail', 'mazda': 'axela', 'honda': 'fit'}
cars['porsch']= 'cayenne'  #add a car
cars['nissan']= 'murano'   #change value
print(cars['toyota'])      #access value of a key

#membership test
print('toyota' in cars)   
print('benz' not in cars)

#iterate thr using for loop
for i in cars:
    print(cars[i])  

print (cars)