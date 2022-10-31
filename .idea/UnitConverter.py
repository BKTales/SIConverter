##Length

def mmToM(meter):
    return meter * 1000

def cmToM(meter):
    return meter * 100

def dmToM(meter):
    return meter * 10

def dcmToM(meter):
    return meter * 0.1

def hmToM(meter):
    return meter * 0.01

def kmToM(meter):
    return meter * 0.001

def inputComparator(userConvertToMeters, numToConvert):
    match userConvertToMeters:
        case "1":
            print(kmToM(numToConvert))
        case "2":
            print(hmToM(numToConvert))
        case "3":
            print(dcmToM(numToConvert))
        case "4":
            print(numToConvert)
        case "5":
            print(dmToM(numToConvert))
        case "6":
            print(cmToM(numToConvert))
        case "7":
            print(mmToM(numToConvert))



##Area

def mmToM2(metersqr):
    return metersqr * 1000 ** 2

def cmToM2(metersqr):
    return metersqr * 100 ** 2

def dmToM2(metersqr):
    return metersqr * 10 ** 2

def dcmToM2(metersqr):
    return metersqr * 0.1 ** 2

def hmToM2(metersqr):
    return metersqr * 0.01 ** 2

def kmToM2(metersqr):
    return metersqr * 0.001 ** 2

def inputComparatorSqr(userConvertToMeters, numToConvert):
    match userConvertToMeters:
        case "1":
            print(kmToM2(numToConvert))
        case "2":
            print(hmToM2(numToConvert))
        case "3":
            print(dcmToM2(numToConvert))
        case "4":
            print(numToConvert)
        case "5":
            print(dmToM2(numToConvert))
        case "6":
            print(cmToM2(numToConvert))
        case "7":
            print(mmToM2(numToConvert))

##Volume

def mmToM3(metercube):
    return metercube * 1000 ** 3

def cmToM3(metercube):
    return metercube * 100 ** 3

def dmToM3(metercube):
    return metercube * 10 ** 3

def dcmToM3(metercube):
    return metercube * 0.1 ** 3

def hmToM3(metercube):
    return metercube * 0.01 ** 3

def kmToM3(metercube):
    return metercube * 0.001 ** 3

def inputComparatorCubic(userConvertToMeters, numToConvert):
    match userConvertToMeters:
        case "1":
            print(kmToM3(numToConvert))
        case "2":
            print(hmToM3(numToConvert))
        case "3":
            print(dcmToM3(numToConvert))
        case "4":
            print(numToConvert)
        case "5":
            print(dmToM3(numToConvert))
        case "6":
            print(cmToM3(numToConvert))
        case "7":
            print(mmToM3(numToConvert))

##Metres to feet

def metersToFeet(meter):
    print(meter * 3.2808)

def feetToMeters(feet):
    print(feet / 3.2808)