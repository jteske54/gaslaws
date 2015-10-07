__author__ = 'jteske13'

def incorrect():
    print("You have selected an incorrect number. Please select again.")

def tempConvChoose():
    print("""
    1. Kelvin
    2. Celsius
    3. Fahrenheit
    """)
    tempChoice = int(input("What would you like to convert? "))
    if tempChoice == 1:
        kelvin()
    elif tempChoice == 2:
        celcius()
    elif tempChoice == 3:
        fahrenheit()
    else:
        incorrect()
        input()
        tempConvChoose()

def kelvin():
    k = int(input("K= "))
    c = k - 273
    f = (c * 1.8) + 32
    print("K= " + str(k))
    print("ºC= " + str(c))
    print("ºF= " + str(f))
    return k

def celcius():
    c = int(input("ºC= "))
    k = c + 273
    f = (c * 1.8) + 32
    print("K= " + str(k))
    print("ºC= " + str(c))
    print("ºF= " + str(f))
    return k

def fahrenheit():
    f = int(input("ºF= "))
    c = (f - 32) / 1.8
    k = c + 273
    print("K= " + str(k))
    print("ºC= " + str(c))
    print("ºF= " + str(f))
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