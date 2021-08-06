thislist = ["banana", "Orange", "Kiwi", "cherry"]

print(''.join(sorted(thislist[3])))
thislist.reverse()

print(thislist) 

a = [0]*26

for i in thislist[3]:
	a[ord(i)-ord('a')] += 1
    
print(a)
