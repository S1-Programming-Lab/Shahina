astr=input("enter the string:\n")
char=input("enter the character:\n")
print("given string is \n",astr)
<<<<<<< HEAD
print("given character is \n",char)
=======
("given character is \n",char)
>>>>>>> 501ae390aa4bc6f3b0f3dff8fb1f97a901a4099f
res=0
for i in range(len(astr)):
    if(astr[i]==char):
        res=res+1
print("number of time charecter is present in string:\n",res)
