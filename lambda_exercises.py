'''
1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x%2 == 0,numbers))
print(even_numbers)
odd_numbers = list(filter(lambda x: x%2 == 1,numbers))
print(odd_numbers)


''' 2)
find which days of the week have exactly 6 characters.
'''
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = list(filter(lambda num: len(num) == 6, weekdays))
print(days)



'''
 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
original_list = ["orange", "red", "green", "blue", "white", "black"]

new_list = list(filter(lambda x: x!= "orange" and x!= "black",original_list))
print(new_list)



''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
list2 = [2, 4, 6, 8]

remove_elements = list(filter(lambda x: x not in list2,list1))
print(remove_elements)







''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]
'''
colors = ['red', 'black', 'white', 'green', 'orange']

substring1 = "ack"
substring2 = "abc"

specific_substring1 = list(filter(lambda colors: substring1 in colors, colors))
specific_substring2 = list(filter(lambda colors: substring2 in colors, colors))

print(specific_substring1)
print(specific_substring2)



''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''
string1 = "SoccerFan"
pq = [lambda string1: any(char.isupper() for char in string1),
    lambda string1: any(char.islower() for char in string1),
    lambda string1: len(string1) >= 8
]
if all (pq(string1) for pq in pq):
    print("Your password works!")
else:
    print("Your password does not work")

string2 = "soccerfan"
pq = [lambda string2: any(char.isupper() for char in string2),
    lambda string2: any(char.islower() for char in string2),
    lambda string2: len(string2) >= 8
]
if all (pq(string2) for pq in pq):
    print("Your password works!")
else:
    print("Your password does not work")

string3 = "SOCCERFAN"
pq = [lambda string3: any(char.isupper() for char in string3),
    lambda string3: any(char.islower() for char in string3),
    lambda string3: len(string3) >= 8
]
if all (pq(string3) for pq in pq):
    print("Your password works!")
else:
    print("Your password does not work")







''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
original_scores.sort(key = lambda subject: subject[1])
print(original_scores)
