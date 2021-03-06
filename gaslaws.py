# TEST
__author__ = 'jteske13'

from math import *
import tempconv, rvalue


def space():
    print()
    print()
    print()


def incorrect():
    print("You have selected an incorrect number. Please select again.")


def choice():
    x = int(input("What is your unknown? "))
    return x


def xagain():
    input("Press enter to do another conversion.")


def menu():
    while True:
        space()
        print("""
Gas Law Conversions

1. Pressure and Volume
2. Volume and Temperature
3. Pressure and Temperature
4. Volume and n
5. Pressure, Volume, and Temperature
6. PV=nRT
7. Rate and Mass
8. Quit
""")
        try:
            mc = (int(input("What would you like to do? Please enter a number: ")))
        except:
            print("You seem to have typed an invalid character. You can only enter numbers.")
            menu()

        if mc == 1:
            pressureVolume()
        elif mc == 2:
            volumeTemperature()
        elif mc == 3:
            pressureTemperature()
        elif mc == 4:
            volumeN()
        elif mc == 5:
            pressureVolumeTemperature()
        elif mc == 6:
            PVEqualsNRT()
        elif mc == 7:
            rateMass()
        elif mc == 8:
            print("Quitting...")
            exit()
        else:
            print("That was not one of the options, please make another choice.")
            input("Please press enter to continue.")


def pressureVolume():
    space()
    print("""
Pressure and Volume

""")
    print("""
Unknown:

1. Pressure
2. Volume
""")
    z = choice()
    if z == 1:
        pressureVolumePressure()
    elif z == 2:
        pressureVolumeVolume()
    else:
        incorrect()
        pressureVolume()


def pressureVolumePressure():
    space()
    print("Unknown Pressure")
    P1 = float(input("P1= "))
    V1 = float(input("V1= "))
    V2 = float(input("V2= "))
    P2 = (P1 * V1) / V2
    print()
    print("P2= " + str(P2))
    xagain()


def pressureVolumeVolume():
    space()
    print("Unknown Volume")
    P1 = float(input("P1= "))
    V1 = float(input("V1= "))
    P2 = float(input("V2= "))
    V2 = (P1 * V1) / P2
    print()
    print("V2= " + str(V2))
    input("Press enter to do another conversion.")


def volumeTemperature():
    space()
    print("Volume and Temperature")
    print()
    print("""
Unknown:

1. Temperature
2. Volume
""")
    z = choice()
    if z == 1:
        volumeTemperatureTemperature()
    elif z == 2:
        volumeTemperatureVolume()
    else:
        incorrect()
        volumeTemperature()


def volumeTemperatureTemperature():
    space()
    print("Unknown Temperature")
    V1 = float(input("V1= "))
    T1 = tempconv.tempConvChoose("T1")
    V2 = float(input("V2= "))
    T2 = V2 / (V1 / T1)
    tempconv.xkelvin(T2)
    xagain()


def volumeTemperatureVolume():
    space()
    print("Unknown Volume")
    V1 = float(input("V1= "))
    T1 = tempconv.tempConvChoose("T1")
    T2 = tempconv.tempConvChoose("T2")
    V2 = (V1 / T1) * T2
    print("V2= " + str(V2))
    xagain()


def pressureTemperature():
    space()
    print("Pressure and Temperature")
    print()
    print("""
Unknown:

1. Pressure
2. Temperature
""")
    z = choice()
    if z == 1:
        pressureTemperaturePressure()
    elif z == 2:
        pressureTemperatureTemperature()
    else:
        incorrect()
        volumeTemperature()


def pressureTemperaturePressure():
    space()
    print("Unknown Pressure")
    P1 = float(input("P1 = "))
    T1 = tempconv.tempConvChoose("T1")
    T2 = tempconv.tempConvChoose("T2")
    P2 = (P1 / T1) * T2
    print("P2= " + str(P2))
    xagain()


def pressureTemperatureTemperature():
    space()
    print("Unknown Temperature")
    P1 = float(input("P1= "))
    T1 = tempconv.tempConvChoose("T1")
    P2 = float(input("P2= "))
    T2 = P2 / (P1 / T1)
    tempconv.xkelvin(T2)
    xagain()


def volumeN():
    space()
    print("Volume and n")
    print()
    print("""
Unknown:

1. Volume
2. n
""")
    z = choice()
    if z == 1:
        volumeNVolume()
    elif z == 2:
        volumeNN()
    else:
        incorrect()
        volumeTemperature()


def volumeNVolume():
    space()
    print("Unknown Volume")
    V1 = float(input("V1= "))
    n1 = float(input("n1= "))
    n2 = float(input("n2= "))
    V2 = (V1 / n1) * n2
    print("V2= " + str(V2))
    xagain()


def volumeNN():
    space()
    print("Unknown n")
    V1 = float(input("V1= "))
    n1 = float(input("n1= "))
    V2 = float(input("V2= "))
    n2 = V2 / (V1 / n1)
    print("n2= " + str(n2))
    xagain()


def pressureVolumeTemperature():
    space()
    print("Pressure, Volume, and Temperature")
    print()
    print("""
Unknown:

1. Pressure
2. Volume
3. Temperature
""")
    z = choice()
    if z == 1:
        pressureVolumeTemperaturePressure()
    elif z == 2:
        pressureVolumeTemperatureVolume()
    elif z == 3:
        pressureVolumeTemperatureTemperature()
    else:
        incorrect()
        volumeTemperature()


def pressureVolumeTemperaturePressure():
    space()
    print("Unknown Pressure")
    P1 = float(input("P1= "))
    V1 = float(input("V1= "))
    T1 = tempconv.tempConvChoose("T1")
    V2 = float(input("V2= "))
    T2 = tempconv.tempConvChoose("T2")
    P2 = (((P1 * V1) / T1) * T2) / V2
    print("P2 =" + str(P2))
    xagain()


def pressureVolumeTemperatureVolume():
    space()
    print("Unknown Volume")
    P1 = float(input("P1= "))
    V1 = float(input("V1= "))
    T1 = tempconv.tempConvChoose("T1")
    P2 = float(input("P2= "))
    T2 = tempconv.tempConvChoose("T2")
    V2 = (((P1 * V1) / T1) * T2) / P2
    print("V2 =" + str(V2))
    xagain()


def pressureVolumeTemperatureTemperature():
    space()
    print("Unknown Temperature")
    P1 = float(input("P1= "))
    V1 = float(input("V1= "))
    T1 = tempconv.tempConvChoose("T1")
    P2 = float(input("P2= "))
    V2 = tempconv.tempConvChoose("T2")
    T2 = (P2 * V2) / ((P1 * V1) / T1)
    tempconv.xkelvin(T2)
    xagain()


def PVEqualsNRT():
    space()
    print("PV=nRT")
    print()
    print("""
Unknown:

1. Pressure
2. Volume
3. Moles
4. Temperature
""")
    z = choice()
    if z == 1:
        PVEqualsNRTPressure()
    elif z == 2:
        PVEqualsNRTVolume()
    elif z == 3:
        PVEqualsNRTMoles()
    elif z == 4:
        PVEqualsNRTTemperature()
    else:
        incorrect()
        volumeTemperature()


def PVEqualsNRTPressure():
    space()
    print("Unknown Pressure")
    V = float(input("V= "))
    n = float(input("n= "))
    R = rvalue.menu()
    T = tempconv.tempConvChoose("T")
    P = (n * R * T) / V
    print("P= " + str(P))
    xagain()


def PVEqualsNRTVolume():
    space()
    print("Unknown Volume")
    P = float(input("P= "))
    n = float(input("n= "))
    R = rvalue.menu()
    T = tempconv.tempConvChoose("T")
    V = (n * R * T) / P
    print("V= " + str(V))
    xagain()


def PVEqualsNRTMoles():
    space()
    print("Unknown Moles")
    P = float(input("P= "))
    V = float(input("V= "))
    R = rvalue.menu()
    T = tempconv.tempConvChoose("T")
    n = (P * V) / (R * T)
    print("n= " + str(n))
    xagain()


def PVEqualsNRTTemperature():
    space()
    print("Unknown Temperature")
    P = float(input("P= "))
    V = float(input("V= "))
    n = float(input("n= "))
    R = rvalue.menu()
    T = (P * V) / (n * R)
    tempconv.xkelvin(T)
    xagain()


def rateMass():
    space()
    print("Rate and Mass")
    denser = float(input("A (Denser)= "))
    lessdense = float(input("B (Less dense= "))
    ans = sqrt(denser / lessdense)
    print(str(ans))
    xagain()


def main():
    menu()


if __name__ == '__main__':
    main()
