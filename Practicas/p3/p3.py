list=[]
list.append([1,2,3,4])
list.append([5,6,7,8])
for i in range(0,10):
    list.append(i)
    
# for i in range(len(list)):
#     print(list[i])

print(list[0],list[-1])
list.append(list)
print(list[-1])
print(list[0][3])
print(list[1][3])