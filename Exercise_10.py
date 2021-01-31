str=input("Enter a string:")
char=str[0]
print("Actual string:",str)
str=str.replace(char,'$')
str1=char+str[1:]
print("Modified string:",str1)