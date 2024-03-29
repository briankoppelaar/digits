from digit.digit import Digit
from time import sleep
from ABE_helpers import ABEHelpers
from ABE_IoPi import IoPi
import json
import logging

class Shotclock:

	def __init__(self):

		i2c_helper = ABEHelpers()
		i2c_bus = i2c_helper.get_smbus()
		multibus = [ IoPi(i2c_bus, 0x20), IoPi(i2c_bus, 0x21)]

		self.tendigit = Digit(multibus, 1)
		self.digit = Digit(multibus, 8)
	
	def getJSONTime(self):

		# Try 2 times as it can return ValueError if time is changing
		for i in range(1,2):
			try:
				ten = self.tendigit.read() *10 

			except ValueError as e:

				sleep(0.01)
				continue
		
			try:
				time = self.digit.read()
				return json.dumps({'status' : 'OK', 'time': time + ten})

			except ValueError as e:

				sleep(0.01)
				continue
		return json.dumps({'status' : 'Error', 'ErrorDetail' : str(e), 'ErrorMessage' : 'No valid time read' })

