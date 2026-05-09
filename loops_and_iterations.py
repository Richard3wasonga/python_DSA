# for loop
nums = [1, 2, 3, 4, 5]

# use break when loop is to stop after a certain condition is met and continue to proceed after the condition is met
# for num in nums:
#     if num == 3:
#         print('Found!')
#         continue
#     print(num)

# for num in nums:
#     for letter in 'abc':
#         print(num, letter)

# starts at default zero and end at 9 since stop number is non inclusive
# for i in range(10):
#     print(i)

# starts at one and end at ten since the stop point value is non inclusive
# for i in range(1, 11):
#     print(i)

# while loop

x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

