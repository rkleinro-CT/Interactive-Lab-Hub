from __future__ import print_function
import qwiic_joystick
import time
import sys

def runExample():

	print("\nSparkFun qwiic Joystick   Example 1\n")
	myJoystick = qwiic_joystick.QwiicJoystick()

	if myJoystick.is_connected() == False:
		print("The Qwiic Joystick device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	myJoystick.begin()

	print("Initialized. Firmware Version: %s" % myJoystick.get_version())

	while True:

		print("X: %d, Y: %d, Button: %d" % ( \
					myJoystick.get_horizontal(), \
					myJoystick.get_vertical(), \
					myJoystick.get_button()))

		time.sleep(.5)

if __name__ == '__main__':
	try:
		run_example()
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example 1")
		sys.exit(0)