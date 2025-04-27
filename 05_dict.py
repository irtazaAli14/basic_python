keys = ['pakistan' , 'uae' , 'us' , 'uk']

values = ['islamabad' , 'dubai' , 'washington' ,'london' ]

countries_capitals = {}

for i in range(len(keys)):
    countries_capitals[keys[i]] = values[i]

# print(countries_capitals)


# if 'pakistan' in countries_capitals:
    # print('yes , it has key called : pakistan')
    
cities = ''
# if not cities:
#     print('Yes , The cities Variable is empty')

def printing_keys():
    for key in countries_capitals:
        print(key)  # <----- The method to printing keys in the dictionary 
    

# printing_keys()


def printing_keys_and_values():
    for key , value in countries_capitals.items():
        print(f'{value} is {key} Capital')
    

# printing_keys_and_values()

