# print('counter librabry of collection modeule')
from collections import Counter  

cities = ['multan' , 'khairpur' , 'karachi' , 'sakhar'  , 'hydrabad' , 'karachi' , 'khairpur']

# count_of_cities = Counter(cities)
#  <<----  Counter Methods and its sub methods or sub-function ---->>
#  <<---- A Counter Method count the element in the list and return in the  Dictionary ---->>

count_of_cities = Counter(cities)

# <----- Sub-Counter Method  => Which is use to add more Functionality in the counter methods 
#  and it is use after Applying Counter Method ----->

# my_sub_counter = count_of_cities.most_common(3)
my_sub_counter = list(count_of_cities.elements())
print(count_of_cities)
print(my_sub_counter)

# my_tuple = ('irtaza' , 'ali' , 'ali')
# my_set = {'1' , '2' , '1'}
# print(my_set) 