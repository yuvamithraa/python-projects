weight=float(input("enter your weight:"))
hight=float(input("enter your hight:"))
BMI=weight/hight**2
print(BMI)
if BMI<=18.5:
    print("you are under weight")
elif  BMI>=18.5 and BMI<=24.9:
    print("you are normal")
elif  BMI>=25:
    print("you are over weight")
    if BMI>=30 and  BMI<=34.9:
        print("you are moderatr obesity")
    elif BMI>=35 and BMI<=39.9:
        print("you are severe obsity")
    else:
        print ("you are very severe or mobid obisity")
else:
    print("please enter your weight or hight correctly ")