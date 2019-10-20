
def calculateBMI(weight, height):
    BMI = weight/height**2
    return BMI
    global BMI

def defineBMI(BMI):
    if BMI < 18.5:
        print("Underweight")
    if 18.5 < BMI < 25:
        print("Normal Weight")
    if 25 < BMI < 30:
        print("Overweight")
    if BMI > 30:
        print("Obese")


while True:
    try:
        weight = float(input("Enter your weight in kilograms: "))
    except ValueError:
        print("please enter a number")

    else:
        try:
            height = float(input("Enter your height in metres: "))
        except ValueError:
            print("please enter a number")
        print("BMI = " ,calculateBMI(weight, height))
        defineBMI(BMI)
        
        



    
