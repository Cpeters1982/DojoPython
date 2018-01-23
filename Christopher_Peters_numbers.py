
# #Multiples, print odds
# for count in range(1, 1000, 2):
#   if(count % 2 != 0):
#       print count
#
#
#
# #Print 5-1,000,000 in multiples of 5
# for count in range(5,1000000, 5):
#     if(count % 5 == 0):
#         print count
#
# # Sum List: prints the some of all values in the list
# a = [1,2,5,10,255,3]
# print sum(a)
#
#
#
# # Find average
# a = [1,2,5,10,255,3]
# print sum(a) / len(a)
sI = 45
if isinstance(sI, int):
    if(sI >= 100):
        print 'That"s a big number!'
    else:
        print 'That"s a small number!'
elif isinstance(sI, str):
    if(sI >= 50):
        print 'Long sentence.'
    else:
        print 'Short sentence.'
elif isinstance(sI, list):
    if(sI >= 10):
        print 'Big list!'
    else:
        print 'Short list'






#sS = 'Rubber baby buggy bumpers'
# if(sS >= 50):
#     print 'Long sentence'
# else:
#     print 'Short'
