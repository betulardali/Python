'''Body mass index is calculated by dividing body weight by the square of height. (kg/m²)
If the result is below 18.5 kg/m^2, means you'rebelow ideal weight (low weight)
If the result is between 18.5 to 24.9 kg/m^2, means you're ideal weight (normal weight)
If the result is between 25 to 29.9 kg/m^2, means you're above ideal weight (overweight)
If the result is between 30 to 39.9 kg/m^2, means you're too much above ideal weight (obesity)
If the result is above 40 kg/m^2, means you're above ideal weight extremely (extremely obese)'''




while True:

    weight=float(input("Enter your body mass: "))
    height=float(input("Enter your height as meter: (exp: 1.72) "))
    index= weight /height**2

    print("\nBody mass index: {}\n".format(round(index,2)))

    min_weight=height**2 * 18.5
    max_weight=height**2 * 24.9

    if index < 18.5:
    
        print("Low weight!\nYou must be between {} and {}.\n".format(round(min_weight,2),round(max_weight,2)))
        
    elif index >= 18.5 and index <25:
        print("Normal weight!")

    elif index >=25 and index < 30:
        print("Overweight!\nYou must be between {} and {}.\n".format(round(min_weight,2),round(max_weight,2)))
    
    elif index <40:
        print( "Obese!\nYou must be between {} and {}.\n".format(round(min_weight,2),round(max_weight,2)))

    else:
        print("Extremely obese!\nYou must be between {} and {}.\n".format(round(min_weight,2),round(max_weight,2)))
    

    choice=(input("Choose one: exit (0) or continue(enter) \n"))
    if choice=="0":
        break
    else:
        continue