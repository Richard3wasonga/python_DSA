# comparison:
# Equals:             ==
# Not Equals:         !=
# Greater Than:       >
# Less Than:          <
# Greater or Equals:  >=
# Less or Equals:     <=
# Object Identity:    is

# langauge = 'Java'

# if langauge == 'python':
#     print('Langauage is Python')
# elif langauge == 'Java':
#     print('Langauage is Java')
# elif langauge == 'Javascript':
#     print('Langauage is Javascript')
# else:
#     print('No match')

# Boolean variables:
# and
# or
# not

user = 'Admin'
logged_in = False

# if user == 'Admin' and logged_in:
#     print('Admin Page')
# else:
#     print('Bad Creds')


# if not logged_in:
#     print('Please Log In')
# else:
#     print('Welcome')



a = [1, 2, 3]
# b = [1, 2, 3] 
b = a # if now like this they have same value same memory id

# notice that in first print statement a is same as b, a in is not equal to be in second because it is not same object in memory
# is operator print(a is b) is same as print(id(a) == id(b)) behide the scenes

# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# False Values:
    # False
    # None
    # Zero of any numeric number
    # Any empty sequence: for example, '', (), [].
    # Any empty mapping: for example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')