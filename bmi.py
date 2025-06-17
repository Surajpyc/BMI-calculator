def main():
    height=float(input("enter your height in meters:"))
    weight=float(input("enter your weight in kilograms:"))
    BMI=(weight/height**2)
    print(f"Your BMI is {BMI:.2f}")
    if (BMI <18.5):
        print("You are Underweight\nYou need to consume more calories")
    elif (18.5<=BMI<25):
        print("Your BMI is normal\nContant consumption same amount of calories\n Keep doing minimal exercise")
    elif (25<=BMI<30):
        print("You are overweight\n need to consume less calories and\n exercise more")
    else:
        print("You are Obese")
    repeat=input("do you want to check BMI [Yes/No]:").lower()
    if repeat=="yes":
        main()
    else:
        exit()
main()
