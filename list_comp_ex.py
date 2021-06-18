#create new list from the existed lists
L1=[1,20,7,4,5,8]
print(L1)#[1, 20, 7, 4, 5, 8]
L2=[i*2 for i in L1]
print("ListComprehension-L2 Based on L1")
print(L2)#[2, 40, 14, 8, 10, 16]

#More than one predivation/filter condition in List Comprehension
#Display elements from the List2 which is divisible by both 2 and 10
L3=[i for i in L2 if(i%2==0) if(i%10==0)]
print("List Comprehension with multiple predicates")
print(L3)#[40, 10]

#find the number of vowels in the given string using
s=input('enter a string')#Hellooo
vowel=[char for char in s if(char in 'aeiou')]
print(vowel)#['e', 'o', 'o', 'o']
print(len(vowel))#4
#find the number of digits in the given string
s="abc1234xyz567"
digits=[char for char in s if(char.isdigit())]
print(digits)#['1', '2', '3', '4', '5', '6', '7']
print(len(digits))#7

#find number of uppercase letters
s="Hello12345 pytHoN"
uppercase=[char for char in s if(char.isupper())]
print(uppercase)#['H', 'H', 'N']
print(len(uppercase))#3
lowercase=[char for char in s if(char.islower())]
print(lowercase)#['e', 'l', 'l', 'o', 'p', 'y', 't', 'o']
print(len(lowercase))#8
Alphabet=[char for char in s if(char.isalpha())]
print(Alphabet)#['H', 'e', 'l', 'l', 'o', 'p', 'y', 't', 'H', 'o', 'N']
print(len(Alphabet))#11
