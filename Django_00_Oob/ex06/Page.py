from elem import Text, Elem
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br

class Wrong(Elem):
	def __init__(self):
		super().__init__(tag='div', content=[Text('Hello ground!')])


valid_name_classes = (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br)

# print(valid_name_classes)

class Page():
	def __init__(self, elem):
		# print("Page.__init__()", type(elem))
		# print(self.is_subclass(elem))
		print(self.is_valid_instance(elem))
		if not Elem.check_type(elem):
			raise TypeError("Page only accepts Html elements")
		else:
			self.elem = elem
		# self.elem = elem
	
	def is_valid_name_class(self, elem):
		# print("is_valid_name_class()", elem.__class__)
		# for valid_name_class in valid_name_classes:
		if type(elem.__class__)  not in valid_name_classes:
			return False
		return True
	
	# def is_subclass(self, elem):
	# 	# print("is_subclass()", elem.__class__)
	# 	if  Elem.check_type(elem) and  self.is_valid_name_class(elem) and type(elem) is not Text and elem.content is None: 
	# 		return True
	# 	if not Elem.check_type(elem) and not self.is_valid_name_class(elem):
	# 		return False
	# 	elif isinstance(elem, Text):
	# 		return True
	# 	else:
	# 		for e in elem.content:
	# 			if not self.is_subclass(e):
	# 				return False
	# 		return False

	def is_valid_instance(self, obj):
		"""
		Recursively checks whether the object's self.content is None or an instance of a subclass of Base.
		Special handling for Text class where self.content doesn't exist.
		"""
		# if isinstance
		if Elem.check_type(obj.content):
			print("Not an instance of Elem")
			return False
		
		if isinstance(obj, Text):
			# Text has no content, so it's valid by default
			return True

		if hasattr(obj, "content"):
			content = obj.content
			if content is None:
				return True
			if Elem.check_type(content):
				return self.is_valid_instance(content)
		print("Invalid instance")
		print(type(obj))
		return False

	# def is_subclass(self, elem):
	# 	if Elem.check_type(elem):
	# 		return True
	# 	else:
	# 		return all([self.is_subclass(e) for e in elem.content])
	# def


	def is_valid(self) -> bool:
		if not isinstance(self.elem, valid_name_classes) or type(self.elem) is Text:
			return False # or raise an exception
		if type(self.elem) == Text:
			return True
		if isinstance(self.elem, Html) and len(self.elem.content) == 2 and isinstance(self.elem.content[0], Head) and isinstance(self.elem.content[1], Body):
			return True
		if isinstance(self.elem, Head) and len(self.elem.content) == 1 and isinstance(self.elem.content[0], Title):
			return True
		if isinstance(self.elem, (Body, Div)) and all(self.is_valid(e, (H1, H2, Div, Table, Ul, Ol, Span, Text)) for e in self.elem.content):
			return True

		return True 

if __name__ == '__main__':
	page = Page(Html([Head(Title(Text('"Hello ground!"')), Meta(attr={'charset':"UTF-8"})), Wrong(), Body([H1(Text('"Oh no, not again!"')), Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})])]))

	page2 = Page(Html([Head(Title(Text('"Hello ground!"')), Meta(attr={'charset':"UTF-8"})),  Body([H1(Text('"Oh no, not again!"')), Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})])]))
	if page.is_valid():
		# print(page)
		pass
	else:
		print("Invalid page")

	if page2.is_valid():
		# print(page2)
		pass
	else:
		print("Invalid page2")