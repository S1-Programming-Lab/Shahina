import math
for i in range(1000,10000):
    num=int(math.sqrt(i))
    if num*num==i:
        n=i
        while n!=0:
<<<<<<< HEAD
            r=n%10
            n=n//10
            if r%2!=0:break
        else:
            print(i)
=======
         r=n%10
         n=n//10
         if r%2!=0:
             break
    else:
        print(i)
>>>>>>> 501ae390aa4bc6f3b0f3dff8fb1f97a901a4099f
