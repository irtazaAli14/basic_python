cities = ['karachi' , 'lahore' , 'islamabad' , 'multan' , 'mansaira' , 'muree' , 'naran kaghan']  

# Slicing dicing 


# print(cities[0:3])
# Expected Output ----- ['karachi', 'lahore', 'islamabad']


# print(cities[0:6:2])
# Expected Output ----- ['karachi' , 'islamabad' , 'mansaira' ]

if not cities : 
    print(cities)

# print(cities[-2])

lenght = len(cities) -1
# print(lenght)
for i in range(lenght ,-(lenght + 1 + 1) , -1):
    print(cities[i])