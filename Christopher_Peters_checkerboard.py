# word_ls = ['hello','world','my','name','is','Chris']
# char = 'o'
# new_ls = []
# for i in range(0,len(word_ls)):
#     if char in word_ls[i]:
#         new_ls.append(word_ls[i])
# print new_ls

# for char in range(4):
#     print "* " * 4
#     print " *" * 4


import turtle

DIST = 50
for x in range(0,7):
    print "x", x
    for y in range(1,6):
        print "y", y
        turtle.right(90)
        turtle.forward(DIST)
        turtle.left(90)
        turtle.forward(DIST)
    DIST += 20