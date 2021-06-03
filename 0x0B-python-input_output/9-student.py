#!/usr/bin/python3
""" Student class """


class Student:
	""" Information about students """
	def __init__(self, first_name, last_name, age):
		""" Initializate """
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def to_json(self):
		"""Directory"""
		return self.__dict__
