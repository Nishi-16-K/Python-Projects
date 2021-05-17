Height=float(input("Enter your Height in centimeters: "))
Weight=float(input("Enter your Weight in kilograms: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("Your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("You are severely underweight")
	elif(BMI<=18.5):
		print("You are underweight")
	elif(BMI<=25):
		print("Congrats!! You are Healthy")
	elif(BMI<=30):
		print("you are overweight")
	else: print("You are severely overweight")
else:("Enter valid details")
      
