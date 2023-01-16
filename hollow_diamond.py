'''See GET HELP you can get more clarity'''
n=int(input())
print(' '*(n-1)+'*')
holl_count=-1
for each in range(1,n):
    spaces=' '*(n-each-1)
    holl_count+=2
    hollow=' '*(holl_count-1)
    print(spaces+'* '+hollow+'*')
for each in range(1,n-1):
    spaces=' '*each
    holl_count-=2
    hollow=' '*(holl_count-1)
    print(spaces+'* '+hollow+'*')
print(' '*(n-1)+'*')
