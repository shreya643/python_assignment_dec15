#Write a function that prompts user to input his/her full name.
#After user enter's his/her full name, split it and store it in variables first_name and last_name.

count=0
k=0
name=str(input("Enter your full name: "))

s=name.split(" ")

print("The first name is:",s[0])
if len(s)==3:
    print("The middle name is:",s[1])
    print("The last name is:", s[2])
else:
    print("The last name is:", s[1])









