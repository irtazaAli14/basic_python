# location = '            karachi     pakistan     '
location = 'karachi pakistan'

# slice_city = location[0:7]
print(location[0: 7])

# print(location.strip())
#  <-- this method remove spaces from sides --> 
#  

# print(location.lstrip()) 
# <-- this method remove spaces from starting lstrip() --> 

# print(location.rstrip())
# this method remove spaces from ending of the sentence ,, rstrip() 


# print(location)



mycity = 'karachi , sindh'
# These are some index finding method
# print(mycity.find('sindh'))
# print(mycity.rfind('sindh'))
# print(mycity.index('s'))
# print(mycity.rindex('s'))


# This is replacing the word or letter you giving in the argument
# first you tell the python  'sindh' replace this word to this 'Pakistan'
# print(mycity.replace('sindh' , 'Pakistan'))
# print(mycity.replace('s' , 'S'))


# The count method --- this method count the letter in the string , letter you are give in the argument
# my_new_city = ' karachi karachi pakistan '
# print(my_new_city.count('a'))


# The startswith method return true or false it depend on the string is starting from the given argument
# print(mycity.startswith('a'))

# The endswith method return true or false it depend on the string is ending from the given argument
# print(mycity.endswith('dh'))


# The most powerfull keyword is 'in' in python 
#  which is identify the finding word or letter is present in the string or not
# <<------- print('r' in mycity)  ------->>


# MODIFYING METHOD IN STRING   

punjab_city = 'islamabad lahore rawalpindi multan gujranwalan'

# Replace method replace the value into other value 

# new_punjab_city = punjab_city.replace(' ' , ",").split(',')

# The split method convert string into list
new_punjab_city = punjab_city.split(' ')
# print(punjab_city)
# print(new_punjab_city[0])
for city in new_punjab_city:
    my_specific_city = 'o' in city
    if my_specific_city:
        break
        # print(city)
    

# now convert list into string
#  The join method is convert list into string
new_punjab_city = ' '.join(new_punjab_city)
# print(new_punjab_city)


# isalpha()	Checks if all characters are letters	'hello'.isalpha() → True
# isdigit()	Checks if all characters are digits	'123'.isdigit() → True
# isalnum()	Checks if all characters are letters or numbers	'abc123'.isalnum() → True
# isspace()	Checks if all characters are whitespace	' '.isspace() → True
# swapcase()	Swaps lowercase to uppercase and vice versa	'Hello'.swapcase() → 'hELLO'
# zfill(width)	Pads string on the left with zeros	'42'.zfill(5) → '00042'










