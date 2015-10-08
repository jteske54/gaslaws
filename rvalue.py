__author__ = 'jteske13'

def menu():
	print("""
1. atm
2. kPa
3. mm Hg/torr
""")
	rchoice = int(input("What is the unit of pressure you are using for R?"))
	if rchoice == 1:
		R = atm()
		return R
	elif rchoice == 2:
		R = kPa()
		return R
	elif rchoice == 3:
		R = mmHg()
		return R
	else:
		print("That was not one of the options, please make another choice.")
		input("Please press enter to continue.")
		menu()


def atm():
	R = float(0.0821)
	print(str(R) + " atm")
	return R


def kPa():
	R = float(8.341)
	print(str(R) + " kPa")
	return R


def mmHg():
	R = float(62.4)
	print(str(R) + " mmHg/torr")
	return R


if __name__ == '__main__':
    menu()