courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
nums = [1,5,2,4,3]

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
print(nums)


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

print(courses)
# print(courses[-1:-5:-1])
# print(courses[::-1])



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