word_ls = ['hello','world','my','name','is','Chris']
char = 'o'
new_ls = []
for i in range(0,len(word_ls)):
    if char in word_ls[i]:
        new_ls.append(word_ls[i])
print new_ls
