#Methods in Dictionary
dict1={1:"CSE",2:"IT",3:"PT",4:"AGRI",5:"ECE"}
print("Get the value of key 4")
print(dict1[4])#dictionary_name[key_name]
#use method
#get()-returns value based on the key
res_value=dict1.get(4)#get(key)->value
print(res_value)
#items()-returns <key,value>pair
res_item=dict1.items()
print(res_item)#dict_items([(1, 'CSE'), (2, 'IT'), (3, 'PT'), (4, 'AGRI'), (5, 'ECE')])
res_key=dict1.keys()
print(res_key)#dict_keys([1, 2, 3, 4, 5])
res_pop=dict1.pop(2)
print(res_pop)#IT
res_popitem=dict1.popitem()
print(res_popitem)#(5, 'ECE')


