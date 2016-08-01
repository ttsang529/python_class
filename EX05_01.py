class Demo:
	#__x = 0
	def __init__(self, i):
		self.i = i
		#print(self.i)
		#Demo.__x += 1

	def hello(self):
		print("hello")





a = Demo("AAA")
print(a.hello())
b = Demo("Tom")
print(b.hello())
c = Demo("CCC")
print(c.hello())
