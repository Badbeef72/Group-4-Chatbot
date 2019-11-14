#muscle
#losing wieght - diet - fitbess plan - take weight + height
#if overwight lose wirgt, if underwieght then buid muscle
#track progress and make siggetseions 
import random


weight = 67

bicep = ["Dumbell Curl", "Hammer Curl", "Incline Dumbbell Curl"]
tricep = ["Tricep Dips", "seated dumbbell press", "V-Bar Pulldown"]
legs = ["barbell squat", "Leg press", "Leg extensions"]
chest = ["Bench press", "Seated machine chest press", "Incline Dumbbell press"]
back = ["Barbell deadlift", "Pull ups", "Close grip pulldown"]


def proteinCalculator(weight):
    protein = weight * 2.2
    return protein

def randomExercise(bodyPart):
    if bodyPart == "bicep":
        random.shuffle(bicep)
        print(*bicep[0])
        
    elif bodyPart == "tricep":
        random.shuffle(tricep)
        print(*tricep[0])
        
    elif bodyPart == "legs":
        random.shuffle(legs)
        print(*legs[0])

    elif bodyPart == "chest":
        random.shuffle(chest)
        print(*chest[0])

    elif bodyPart == "back":
        random.shuffle(back)
        print(*back[0])

    else:
        print("Please enter a valid body part")

while True:
    userWeight = float(input("Enter your weight: "))
    print("You need ", proteinCalculator(userWeight), " grams of protein per day")  
    userChoice = input("What would you like to work on today?: ")
    randomExercise(userChoice)
        


print("You need ", proteinCalculator(weight), " grams of protein per day")    
    
