import UnitConverter

isValid = True

print("This is a SI unit converter")
print("1 -> Lenght")
print("2 -> Area")
print("3 -> Volume")
print("4 -> Feet to meter")
print("5 -> Meter to Feet")

userSIUnit = str(input("-> "))

match userSIUnit:
    case "1":
        print("\n\n\nWhich unit you want to convert to meters?")
        print("1 -> Km")
        print("2 -> Hm")
        print("3 -> Dcm")
        print("4 -> M")
        print("5 -> Dm")
        print("6 -> Cm")
        print("7 -> Mm")

        userConvertToMeters = str(input("-> "))

        print("Great! Your choice was ", userConvertToMeters)
        numToConvert = float(input("Input a number to convert: "))
        UnitConverter.inputComparator(userConvertToMeters, numToConvert)

        isValid

    case "2":
        print("\n\n\nWhich unit you want to convert to meters squared?")
        print("1 -> Km²")
        print("2 -> Hm²")
        print("3 -> Dcm²")
        print("4 -> M²")
        print("5 -> Dm²")
        print("6 -> Cm²")
        print("7 -> Mm²")

        userConvertToMeters = str(input("-> "))

        print("Good! Your choice was ", userConvertToMeters)
        numToConvert = float(input("Input a number to convert: "))
        UnitConverter.inputComparatorSqr(userConvertToMeters, numToConvert)

        isValid

    case "3":
        print("\n\n\nWhich unit you want to convert to cubic meters?")
        print("1 -> Km³")
        print("2 -> Hm³")
        print("3 -> Dcm³")
        print("4 -> M³")
        print("5 -> Dm³")
        print("6 -> Cm³")
        print("7 -> Mm³")

        userConvertToMeters = str(input("-> "))

        print("Perfect! Your choice was ", userConvertToMeters)
        numToConvert = float(input("Input a number to convert: "))
        UnitConverter.inputComparatorCubic(userConvertToMeters, numToConvert)

        isValid

    case "4":
        print("You are about to convert feet to meters")
        feet = float(input("Input how much feet do you want to convert: "))
        UnitConverter.feetToMeters(feet)

        isValid

    case "5":
        print("You are about to convert meters to feet")
        meter = float(input("Input how much meters do you want to convert: "))
        UnitConverter.metersToFeet(meter)

        isValid

    case _:
        print("INVALID INPUT\nEXITING!!!")

        isValid = False

if(isValid):
    print("You are awesome, goodbye!\nEXITING!!!")





