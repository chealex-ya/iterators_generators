nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator:

	def __init__(self, any_list):
		self.any_list = any_list

	def __iter__(self):
		self.cursor = 0
		self.cursor_2 = -1
		x = len(self.any_list[self.cursor])
		return self

	def __next__(self):
		self.cursor_2 += 1
		if len(self.any_list[self.cursor]) == self.cursor_2:
			self.cursor += 1
			self.cursor_2 = 0
		if len(self.any_list) == self.cursor:
			raise StopIteration
		return self.any_list[self.cursor][self.cursor_2]

for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)