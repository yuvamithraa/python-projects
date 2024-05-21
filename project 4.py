y=[1,3,6,4,0,77,45,32,48]
even=[]
odd=[]
for i in y:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even list",even)
print("odd list",odd)