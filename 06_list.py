cities = ['karachi' , 'lahore' , 'islamabad' , 'multan' , 'mansaira' , 'muree' , 'naran kaghan']  

# Slicing dicing 


# print(cities[0:3])
# Expected Output ----- ['karachi', 'lahore', 'islamabad']


# print(cities[0:6:2])
# Expected Output ----- ['karachi' , 'islamabad' , 'mansaira' ]

if not cities : 
    print(cities)

# print(cities[-2])

def print_list_from_decending_to_accending():
    lenght = len(cities) -1
    print(lenght)
    for i in range(lenght ,-(lenght + 1 + 1) , -1):
        print(cities[i])
    
# print_list_from_decending_to_accending()

# slicing and dicing 
def slicing_dicing():
    # print(cities[3 : 4])
    new_val = ['Pindi']
    cities[3 : 4] = new_val
    # print(cities[3 : 4])


slicing_dicing()

def inserting_value():
    cities.insert( 4 ,'Faislabad')

inserting_value()

def remove_value():
    cities.remove('naran kaghan')

remove_value()

def pop_method():
    cities.pop(3)

pop_method()


def count_method(value):
    return cities.count(value)

# print(count_method('karachi' ))


def reverse_method():
    cities.reverse()

reverse_method()
print(cities)