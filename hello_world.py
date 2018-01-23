'''Test Document, leave me alone PyLint'''
# def add(a,b):
#     x = a + b
#     return x
# result = add(3, 5)
# print result

# def multiply(arr, num):
#     for x in range(len(arr)):
#         arr[x] *= num
#     return arr
# a = [2,4,10,16]
# b = multiply(a,5)
# print b

'''
The function multiply takes two parameters, arr and num. We pass our arguments here.
for x in range(len(arr)) means
"for every index of the list(array)" and then "arr[x] *= num" means multiply
the indices of the passed in array by the value of the variable "num"
return arr sends arr back to the function


*= multiplies the variable by a value and assigns the result to that variable
'''

# def fun(arr, num):
#     for x in range (len(arr)):
#         arr[x] -= num
#     return arr
# a = [3,6,9,12]
# b = fun(a,2)
# print b

'''
Important! The variables can be anything! Use good names!
'''

# def idiot(arr, num):
#     for x in range(len(arr)):
#         arr[x] /= num
#     return arr
# a = [5,3,6,9]
# b = idiot(a,3)
# print b



# def function(arr, num):
#     for i in range(len(arr)):
#         arr[i] *= num
#     return arr
# a = [10, 9, 8, 7, 6]
# print function(a, 8)

# def avg(arr):
#     avg = 0
#     for i  in range(len(arr)):
#         avg = avg + arr[i]
#     return avg / len(arr)
# a = [10,66,77]
# print avg(a)
# Determines the average of a list (array)

weekend = {"Sun": "Sunday", "Sat": "Saturday"}
weekdays = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday",
            "Fri": "Friday"}
months = {"Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April",
          "May": "May", "Jun": "June", "Jul": "July",
          "Aug": "August", "Sep": "September", "Oct": "October", "Nov": "November",
          "Dec": "December"}

# for data in months:
#     print data

# for key in months.iterkeys():
#     print key

# for val in months.itervalues():
#     print val

# for key,data in months.iteritems():
#     print key, '=', data


# print len(months)
# print len(weekend)
# print str(months)



# context = {
#   'questions': [
#    { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
#    { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
#    { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
#    { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
#   ]
#  }

# userAnna = {"My name is": "Anna", "My age is": "101", "My country of birth is": "The U.S.A", "My favorite language is": "Python"}
# for key,data in userAnna.iteritems():
#     print key, data