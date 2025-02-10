h=float(input("enter your height:"))
w=float(input("enter your weight:"))

bmi=w/(h/100)**2

print("The BMI:",bmi)

if bmi<=18.5:
    print("underweight...")
elif bmi<=24.6:
    print("healthy")
elif bmi<=29.5:
    print("overweight")
elif bmi<=34.6:
    print("severly overweight")
elif bmi<=39.6:
    print("obese")
else:
    print("severly obese...")
    