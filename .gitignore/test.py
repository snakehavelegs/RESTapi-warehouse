class names:
	def func(self, name):
  		self.variable = name.split(',')

name = names()
name.func('foo, bar')

print(name.variable)