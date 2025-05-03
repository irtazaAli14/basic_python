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

def extent_method(values):
    # values <--- values should be an array --->
    cities.extend(values)

extent_method(["Aptabad" , "Naran Kaghan"])

# print(cities)







# pr_languages = ['python' , 'c++' , 'java' , 'javascript' , 'ruby' , 'c#' ]

numbers = [3, 7, 2, 9, 4, 5]

# Find the Maximum and minimum number from this list

def find_max_val(my_list):
    max_val = my_list[0]
    for i in range(len(my_list)):
        # max_val = i if i > max_val
        if my_list[i] > max_val:
            max_val = my_list[i]
    return max_val  
    

def find_min_val(my_list):
    min_val = my_list[0]
    for i in range(len(my_list)):
        my_list_val = my_list[i]
        if my_list_val < min_val:
            min_val = my_list_val
    return min_val
    
my_max_val =  find_max_val(numbers)
my_min_val =  find_min_val(numbers)
# print(f'Maximum value from numbers : {my_max_val}')
# print(f'Minimum value from numbers : {my_min_val}')


# Remove the duplicate elements from the list  

# elements = [1, 2, 2, 3, 4, 4, 5]

def remove_duplicate():
    elements = [1, 2, 2, 3, 4, 4, 5]
    list_len = len(elements)
    for i in range(list_len):
        # print(elements[i] , 'main loop')
        for j in range(list_len):
            if i != j:
                # print(elements[j] , '----------------inner loop')
                if elements[i] == elements[j]:
                    # elements.remove(elements[j])
                    # elements_copy.pop(j)
                    elements[j : j+1]  = []
                    list_len -= 1
                    # print(elements[j])
    
    print(elements)

# remove_duplicate()
# print(elements)   
# for i in elements:
#         print(elements[i])
my_list_numbers = [1, 2, 75, 3, 4, 4, 5]

# my_list.pop(2)  #  i can delete the value by passing the index number of value that i want to delete
# my_list.remove(5)  #  i can delete the value by passing the exact value that i want to delete from a list
# my_list[2:3] = []
# print(my_list)

my_list_numbers = [1, 2, 75, 3, 4, 4, 5]
def remove_duplicate2(numbers):
    # convert into set
    my_set = set(numbers)
    print(list(my_set))
    

# remove_duplicate2(my_list_numbers)
# print(my_list_numbers)
    

my_list_numbers = [1, 2, 4 ,  75, 3, 4, 4, 5 , 1 , 75 ,75 , 75]

def remove_duplicates3(numbers):
    new_numbers = []
    for num in numbers:
        if num not in new_numbers:
            new_numbers.append(num)
            # print(num)
    
    # print(new_numbers , 'unique')
        
remove_duplicates3(my_list_numbers)

def reverse_list():
    my_list_new = [1, 2, 2, 3, 4, 4, 5]
    reversed_list = []

    for i in range(len(my_list_new ) - 1 , -1 , -1):
        reversed_list.append(my_list_new[i])
        # print(my_list[i])
        # print(i)
    
    print(reversed_list , 'List is Reversed')

# reverse_list()

def count_unique_elements():
    my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    duplicates_list = []
    for i in range(len(my_list)):
        # print(my_list[i])
        for j in range(len(my_list)):
            # print(my_list[j])
            if i != j:
                # print()
                if my_list[i] == my_list[j]:
                    duplicates_list.append(my_list[j])
    
    duplicated_list_new1 = list(set(duplicates_list))
    duplicated_list_new2 = list(set(my_list))
    for item in duplicated_list_new2:
        if item not in duplicated_list_new1:
            print(item)
    # print(duplicated_list_new1)
    # print(duplicated_list_new2)

# count_unique_elements()


def merge_sorted_list():
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    list1 = list1 + list2
    list_sroted = list(set(list1))
    print(list_sroted)

# merge_sorted_list()



def palindrome_check():
    my_list = [1, 2, 3, 2, 1]
    length =  len(my_list)
     
    
    odd_even = length % 2
    list_half_length  = length / 2
    #  if its 1 so the list is odd 
    loop_refrence = 0
    if odd_even == 1:
        loop_refrence = list_half_length - 0.5
    else:
        loop_refrence = list_half_length - 1

    # print(val)
    first_half = []
    second_half = []
    for i in range(0 , 3):
        # print(my_list[i])
        first_half.append(my_list[i])

    for i in range(2 , length):
        second_half.append(my_list[i])
    # print(87.5 + 87.5 == 175)
    print(set(first_half))
    print(set(second_half))
    print(set(first_half) == set(second_half))
palindrome_check()



