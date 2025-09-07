# 1. Write a program that prints all even numbers from 10 to 20 (inclusive) using the range() function without using any loop.
for i in range(10, 20 + 1, 2):
    print(i)

# 2. Write a program that keeps asking the user to enter a positive number. Stop only when the user enters 0. Ensure the user is asked at least once (simulate do-while).
while True:
    num = int(input('enter +ve number: '))
    if(num == 0):
        break
    
    if(num > 0):
        print(num)

# 3. Write a program using a while loop to calculate the factorial of a number entered by the user.
n = int(input('enter number for factorial: '))
prod = 1

while n > 1:
    prod *= n
    n -= 1

print('factorial: ', prod)

# 4. Write a program to assign a grade based on the score:

# If score > 90: Grade A

# If score > 80: Grade B

# If score > 70: Grade C

# If score > 60: Grade D

# Else: Grade F

# Use nested if-else.

score = int(input('enter score for grade: '))
if score > 90:
    print('grade is A')
elif score > 80:
    print('grade is B')
elif score > 70:
    print('grade is C')
elif score > 60:
    print('grade is D')
else:
    print('grade is F')

# 5. Write a program that asks the user to enter a number from 1 to 7 and prints the day of the week using match-case:

# 1: Monday

# 2: Tuesday

# ...

# 7: Sunday

# Any other number: Invalid input

day = int(input('enter number for day: '))
match day:
    case 1:
        print('monday')
    case 2:
        print('tuesday')
    case 3:
        print('wednesday')
    case 4:
        print('thursday')
    case 5:
        print('friday')
    case 6:
        print('saturday')
    case 7:
        print('sunday')
    case default:
        print('invalid input')


# 6. Write a Python program that manages a list of student scores. Perform the following operations step-by-step:
# Create an empty list to store scores.
# Append the scores: 85, 90, 78, 92, 88
# Insert the score 80 at index 
# Remove the score 92 from the list
# Sort the scores in ascending order
# Reverse the list
# Find and print the maximum and minimum score
# Check if 90 is in the list
# Print the total number of scores
# Slice and print the first three scores
# Iterate through the list and print each score

# find the last element from the list
# replace the score with new score on the index 2
# create a new copied list also

list = []
list.append(85)
list.append(90)
list.append(78)
list.append(92)
list.append(88)

print(list)

list.insert(3, 80)
print(list)

list.remove(92)
print(list)

list = sorted(list)
print(list)

list.reverse()
print(list)

print('min: ', min(list))
print('max: ', max(list))

print('list contains 90: ', 90 in list)
print('total count: ', len(list))
print('first 3: ', list[0:3])

for n in list:
    print(n)

print('last: ', list[len(list) - 1])

list[2] = 77
print(list)

list2 = list.copy()
list[0] = 9
print('orig: ', list)
print('copy: ', list2)