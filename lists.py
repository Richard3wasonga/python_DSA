courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
nums = [1,5,2,4,3]

# Empty list
# empty_list = []
# empty_list = list()

# courses.reverse()
# When using sort we alter the original list to not alter the original list use sorted which returns a sorted version of the list
# courses.sort()
# sorted_courses = sorted(courses)
# print(sorted_courses)
# nums.sort()
# courses.sort(reverse=True)

# lib = sorted(courses)
# lib.reverse()

# or
# courses.sort()
# lib = courses.copy()
# lib.reverse()

# or
# lib = sorted(courses, reverse=True)
# print(lib)

# nums.sort(reverse=True)

# print(min(nums))
# print(max(nums))
# print(sum(nums))

# pop returns the item removed
# pop uses indexes not values
# courses.pop(1)
# popped = courses.pop()
# print(popped)

#if you append or insert course_2 to course it puts the entire list not individual items hence just extend
#courses.remove('Math')
#courses.extend(courses_2)
#courses.append('Art')
#courses.insert(0,'Art')

# print(courses)

# To find the index of a value
# print(courses.index('CompSci'))

# To find if a value exists and returns true or false
# print('Art' in courses)

# for course in courses:
#     print(course)

# Enumerate give the index of the value currently being looped
# The start gives which value the index should start being couted from
# for index, course in enumerate(courses, start=1):
#      print(index, course)

# print(courses[-1:-5:-1])
# print(courses[::-1])

course_str = ', '.join(courses)
print(course_str)

new_list = course_str.split(', ')
print(new_list)



# sample_url = 'http://coreyms.com'
# print(sample_url)

# Reverse the sample_url
# print(sample_url[::-1])

# Get the top level domain
# print(sample_url[-4:])

# Print the url without the http://
# print(sample_url[7:])

# Print the url without the http:// or the top level domain
# print(sample_url[7:-4])