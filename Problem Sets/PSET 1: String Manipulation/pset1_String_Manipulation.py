# Q1: Write a Program to find out no. of vowels in a string
print('Number of vowels: ', sum(c in 'aeiou' for c in s))


# Q2: Write a Program to count the no. of times "bob" occurs in a string
print("Number of times bob occurs is:", sum([s[i:i+3] == "bob" for i in range(len(s))]))


# Q3: Write a Program to find the longest alphabetical sub-string of an inputted string
s = input("Enter the string whose longest alphabetical sub-string is to be found out\n")
current, longest, st = s[0], s[0], s[1:]
while st:          
    if st[0] < current[-1]:
        current = ""
    current += st[0]
    if len(current) > len(longest):
        longest = current
    st = st[1:]
print("Longest substring in alphabetical order is: " +longest)
