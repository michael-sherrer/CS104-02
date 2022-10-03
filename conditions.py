temp = input("Please enter the current temperature:")
if int(temp)>90:
    print("Wear shorts")
elif int(temp)>70:
    print("Short sleeves are fine")
elif int(temp)>50:
    print("Wear a jacket")
elif int(temp)>32:
    print("Wear a heavy coat")
elif int(temp)<=32:
    print("Stay inside")
