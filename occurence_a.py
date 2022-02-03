astr=input("enter the string:\n")
char=input("enter the character:\n")
print("given string is \n",astr)
print("given character is \n",char)
res=0
for i in range(len(astr)):
    if(astr[i]==char):
        res=res+1
print("number of time charecter is present in string:\n",res)
