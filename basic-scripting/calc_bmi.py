def gather_info():
    age = int(input("What is your age? "))
    height = float(input("What is your height? (inches) "))
    weight = float(input("What is your approx. weight? (lbs) "))
    return (age, height, weight)

def calculate_bmi(weight, height):
    print("Your BMI is {}".format((weight/(height**2))))
    return (weight / (height ** 2))

age, height, weight = gather_info()
calculate_bmi(weight, height)