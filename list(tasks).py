

# task 2
#Write a Python program to count the number of strings where the string length 
#is two or more, and the first and last characters are the same from a given list of strings.

count = 0
list1 = ['apple', 'asmita', 'mango', 'amanda','e','grape']
for i in list1:
    if len(i) >= 2 and i[0] == i[len(i)-1]:
        count = count + 1
print(count)        