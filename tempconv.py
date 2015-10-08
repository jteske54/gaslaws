__author__ = 'jteske13'


def incorrect():
    print("You have selected an incorrect number. Please select again.")


def tempConvChoose(temp):
    print("""
1. Kelvin
2. Celsius
3. Fahrenheit
""")
    tempChoice = int(input("Please enter the unit of temperature for " + temp + ":"))
    if tempChoice == 1:
        k = kelvin(temp)
        return k
    elif tempChoice == 2:
        k = celcius(temp)
        return k
    elif tempChoice == 3:
        k = fahrenheit(temp)
        return k
    else:
        incorrect()
        input()
        tempConvChoose()


def kelvin(temp):
    k = float(input(temp + "K= "))
    c = k - 273
    f = (c * 1.8) + 32
    print(temp + " K= " + str(k))
    print(temp + " ºC= " + str(c))
    print(temp + " ºF= " + str(f))
    return k


def celcius(temp):
    c = float(input(temp + "ºC= "))
    k = c + 273
    f = (c * 1.8) + 32
    print(temp + " K= " + str(k))
    print(temp + " ºC= " + str(c))
    print(temp + " ºF= " + str(f))
    return k


def fahrenheit(temp):
    f = float(input(temp + "ºF= "))
    c = (f - 32) / 1.8
    k = c + 273
    print(temp + " K= " + str(k))
    print(temp + " ºC= " + str(c))
    print(temp + " ºF= " + str(f))
    return k


def xkelvin(pull):
    k = float(pull)
    c = k - 273
    f = (c * 1.8) + 32
    print("K= " + str(pull))
    print("ºC= " + str(c))
    print("ºF= " + str(f))
    return k


def xcelcius(pull):
    c = float(pull)
    k = c + 273
    f = (c * 1.8) + 32
    print("K= " + str(k))
    print("ºC= " + str(c))
    print("ºF= " + str(f))
    return k


def xfahrenheit(pull):
    f = float(pull)
    c = (f - 32) / 1.8
    k = c + 273
    print("K= " + str(k))
    print("ºC= " + str(c))
    print("ºF= " + str(f))
    return k


def main():
    tempConvChoose()


if __name__ == '__main__':
    main()
