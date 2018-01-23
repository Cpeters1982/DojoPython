words = 'It"s thanksgiving day. It"s my birthday, too!'
print words.find('day')
print words.replace('day', 'month')



x = [2,54,-2,3,5,8,12]
print min(x)
print max(x)



x = [1,2,3,4,5,6,7,8,9,10]
print x[0], x[-1]
new_list = []
new_list.append(x[0])
new_list.append(x[-1])
print new_list







x = [19,6,54,-2,37,6,12,15]
x.sort()
halfx = x[:len(x)/2]
new_list = []
new_list.append(halfx)
new_list.append(x)
print new_list
