student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# A key can be a sting, interger
# When trying to access a key that doesn't exists it causes a keyerror

# print(student['courses'])

# sometimes  you just want  when accessing a key that does not exist it just gives none use .get method
# by default None is the default value if not found you can add your own by passing extra argument in the get method

# print(student.get('phone', 'Not found')) 

# student['phone'] = '555-5555'
# student['name'] = 'Jane'

# student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

# pop method returns the value being deleted as seen in lists also
# del student['age']
# age = student.pop('age')

# print(student)
# print(age)

# return number of keys in our dictionry
# .keys prints all keys, .values prints all values, .items print both key and values in pairs
# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())

# for key in student:
#     print(key)

# the first one will only loop on keys only to loop through both key and value we use the .items method

for key, value in student.items():
    print(key, value)