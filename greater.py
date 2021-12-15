print("enter the list")
list[0]
result=[]
for i in list:
    if i>100:
        result.append('over')
    else:
        result.append(i)
    print(result)
