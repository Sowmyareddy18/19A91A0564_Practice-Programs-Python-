b=list(("banana","kiwi"))
print(b)
b.append("jiwi")
print(b)
x=b.copy()
print(x)
x.clear()
print(x)
y=b.copy()
print(*y)
y.sort()
print(y)
y.sort(reverse=True)
print(y)
y.remove("banana")
print(y)
y.append("mango")
y.append("mango")
print(y.count("mango"))
y.reverse()
print(y)
'''
output:
['banana', 'kiwi']
['banana', 'kiwi', 'jiwi']
['banana', 'kiwi', 'jiwi']
[]
banana kiwi jiwi
['banana', 'jiwi', 'kiwi']
['kiwi', 'jiwi', 'banana']
['kiwi', 'jiwi']
2
['mango', 'mango', 'jiwi', 'kiwi']
'''
