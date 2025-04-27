# Hopping in strings
# city = 'karachi'

# print(city[0:5])
#  output   "karac"

# print(city[0:5:2])
#      output  "krc"

# print(city[:2])
#     output "ka"

# print(city[4:])
#  output   "chi"


# print(city[:])
# Return Complete string





# STRING METHODS 

city = 'KaRAcHi'
# print(city.lower())  # <---  return Loswer case ----> 

city = '     kara   chi     '
# print(city.strip()) # <---- Remove extra Spaces starting from and end from not in the center   ---->
# The expected output ---->>> "kara   chi"

city = 'karachi sindh'
# print(city.replace("sindh" , "Pakistan")) 

cities = 'lahore, islamabad, pindi, sawat, mansayra, muree, naran kaghan' 

# print(cities.split(', ')) # <--- Is is converting string into list on the basis of provided parameters -->

city = 'karachi pakistan'
# print(city.find('pakistan')) # <--- it is return integer which is telling your finding word or character is straing from this indexing

# If it is returing -1 so its mean your finding word or letter is not present in the string

# print(city.count('a'))
# how much time a is appearing in the string 



# FORMATING THE STRING 
name = 'Irtaza'
city = 'karachi'

statement = 'My name is {}. I am living in {}'

# print(statement.format(name , city))
# This is formating whenever you need to add variables in the string. 

cities = ['karachi' , 'lahore' , 'islamabad']

# print(' '.join(cities))
# Convert list into string 



# CONTAINING QUESTIONS 
city = 'karachi pakistan'

print('lahore' in city)
# it is asking the question is this word or letter are appearing in the string
