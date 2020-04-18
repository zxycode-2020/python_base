import itertools

'''
_ _ _ _ _
'''

mylist = list(itertools.product("0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm", repeat=10))
#print(mylist)
print(len(mylist))


