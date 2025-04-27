# print('python is a vertasyle language , which is use in multiple domains like Data Science , Data Engineering , Automation , AI , ML and Web Developing')


# Data Types :
# 
# '''' 
# There are two major datatypes in python 
#  mutable and immmutable 
#  mutable datatypes :values can be change or modify after assigning 
#  immutable datatypes : values cant be change after assigning 
# '''


country_name  = 'pakistan'
reverse_country_name = ''

for cn in country_name:
    reverse_country_name = cn + reverse_country_name


# print(reverse_country_name , 'Reverse Country Name')

my_str = 'qwertyuifovnreoa'

count_vovel = 0
vovel_letters = ['a','e','i','o','u']

for char in my_str:
    if char in vovel_letters:
        count_vovel += 1
    
print(count_vovel , 'Vovel Count in String')
# if 'b' in vovel_letters:
#     print('a')

