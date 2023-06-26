
people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'female',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'male', 'id': 3},
]

# SORTING
# sort() method: sorts iterable object in some order. Modifies original list and returns it. Does NOT create a new list
# Named arguments

# sorting by id, descending order
# -> people_list.sort(key = lambda p: p['id'], reverse=True)

# sorting by weight, ascending order
people_list.sort(key=lambda person_object: person_object['weight'], reverse=True)
# print(people_list)

# --------------------------------------------------------------------------------------------------
# FILTERING
# CREATES NEW list based on 1. original list and 2. a condition
# Positional arguments

# filter list: 1. male, weight > 140
new_list = list(
                filter(
                    lambda person_object: person_object['sex'] == 'female' and person_object['weight'] > 140,
                    people_list
                )
)
# print('filtered list: ', new_list)

# --------------------------------------------------------------------------------------------------
# MAPPING
# CREATES a new list by applying a given function to each element of a list

# Return name with Mr. or Mrs. and age
def transform (person_object):
    new_person = {'age': person_object['age']}

    if person_object['sex'] == 'male':
        new_person.update({'name': f"Mr. {person_object['name']}"})
    else:
         new_person['name'] = f"Mrs. {person_object['name']}"

    return new_person

# variable = result1 if () else result2
# variable = () ? result1 : result2

result_list = list(
    map(
        lambda person_object: {
            'age': person_object['age'],
            'name': f"Mr. {person_object['name']}" if (person_object['sex'] == 'male') else f"Mrs. {person_object['name']}"
        },
        people_list
    )
)

print(result_list)


# --------------------------------------------------------------------------------------------------
#  List Comprehension

car_list = [
    {'id': 1, 'make': 'Ford',   'model': 'Mustang',  'price': 36000, },
    {'id': 2, 'make': 'Chevy',  'model': 'Corvette', 'price': 60000, },
    {'id': 3, 'make': 'Toyota', 'model': 'Prius',    'price': 35000, },
    {'id': 4, 'make': 'Mazda',  'model': 'Mazda6',   'price': 32000, },
]

# print ([c['id'] for c in car_list if c['price'] > 33000])