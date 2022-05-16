while True:
    w = float(input('Enter Weight(kg): '))
    h = float(input('Enter Height(m): '))

    bmi = (w/(h**2))
    print(bmi)

    if bmi<18.5:
        print("Underweight")
    if bmi>=18.5 and bmi<25:
        print("Normal")
    if bmi>=25 and bmi<30:
        print("Ovrweight")
    if bmi>=30 and bmi<35:
        print("Obese")
    if bmi>=35:
        print("Extremely Obese")
