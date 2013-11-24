#!/usr/bin/env python2

import os
import time
import urllib2

class GPIO(object):

	INPUT = 'in'
	OUTPUT = 'out'

	def __init__(self, number):

		self.number = number
		self.path = '/sys/class/gpio/gpio{}'.format(number)

		if not os.path.exists(self.path):
			with open('/sys/class/gpio/export', 'w') as fh:
				fh.write('{}\n'.format(number))
	
	def read_attribute(self, name):
		with open(os.path.join(self.path, name)) as fh:
			return fh.read().rstrip()
	
	def write_attribute(self, name, value):
		with open(os.path.join(self.path, name)) as fh:
			fh.write('{}\n'.format(value))

	def set_direction(self, direction):
		self.write_attribute('direction', direction)
	
	def get_direction(self):
		return self.read_attribute('direction')
	
	def set_value(self, value):
		self.write_attribute('value', int(bool(value)))

	def get_value(self):
		return bool(int(self.read_attribute('value')))

class Main(object):

	def initialize(self):
		self.check = GPIO(5)
		self.check.set_direction(GPIO.INPUT)
		self.forward = GPIO(30)
		self.forward.set_direction(GPIO.OUTPUT)
		self.backward = GPIO(31)
		self.backward.set_direction(GPIO.OUTPUT)
	
	def update(self):
		data = json.load(urllib2.urlopen('http://hando.herokuapp.com/endpoint'))

	def run(self):
		while True:
			try:
				self.update()
			except Exception as e:
				import traceback
				traceback.print_exc()
			time.sleep(1)
