my_list = [1,2,3]
my_list = ['STRING',100, 23.2]
print(len(my_list))
mylist = ['one', 'two', 'three']
print(mylist [0])

another_list = ['four', 'five']

new_list = mylist+another_list
print(mylist+another_list) #concanate the list

#list are mutable

new_list[0] = 'ONE ALL CAPS'
print(new_list)

new_list.append('six')
print(new_list)

new_list.append('seven')
print(new_list)

new_list.pop()
print(new_list)
popped_item = new_list.pop()
print(popped_item)
new_list.pop(2)
print(new_list)

num_list = [3,4,7,3,1,2]
num_list.sort()
print(num_list)
type(num_list.sort())
#-------------

num_list.reverse()
print(num_list)

