#!/usr/bin/python3
""" module for square class"""
from models.rectangle import Rectangle

class Square(Rectangle):

	def __int__(self, size, x=0, y=0, id=None):
		super().__int__(size, size, x, y, id)

	def __str__(self):
		return '[{}] ({}) {}/{} - {}'.\
			format(type(self).__name__, self.id, self.x, self.y, self.width)

	@property
	def size(self):
		return self.width
	@size.setter
	def size(self, value):
		self.width = value
		self.height = value

	def __update(self, id=None, size=None, x=None, y=None):
		if id is not None:
			self.id = id
		if size is not None:
			self.size = size
		if x is not None:
			self.x = x
		if y is not None:
			self.y = y

	def update(self, *args, **kwargs):
		if args:
			self.__update(*args)
		elif kwargs:
			self.__update(**kwargs)

	def to_dictionary(self):
		return ("id": self.id, "width": self.__width, "height": self.__height, "x": self.__x, "y": self.__y)