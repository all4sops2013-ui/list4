# task 1
#  Write a program to perform the following operations on a List: 
# 1. Create an empty list 2. A list with elements 3. Use * operator 4. Reverse a list

list1 = []
list2 = [34,56,67,87,32]
print(list2*3)
list2.reverse()
print(list2)





list_even = []
list1 = [12,34,78,89,100,200,250]
for i in list1:
    if i % 2 == 0:
        list_even.append(i)

print(list_even)

#for loop can be executed on a list
#you can check conditions based on list values




# task 2
#Write a Python program to count the number of strings where the string length 
#is two or more, and the first and last characters are the same from a given list of strings.

count = 0
list1 = ['apple', 'asmita', 'mango', 'amanda','e','grape']
for i in list1:
    if len(i) >= 2 and i[0] == i[len(i)-1]:
        count = count + 1
print(count)        




# task 3
# Write a Python program to find the sum and average of the list. 
# The average of the list is defined as the sum of the elements divided by the number of the elements.
#  Also, find the largest and the smallest number in the list.

sum = 0
list1 = [45,6,78,57,23,12,34,5]
for i in list1:
    sum = sum + i
avg = sum / len(list1)

print("the sum = ",sum)
print("The avg = ",avg)
