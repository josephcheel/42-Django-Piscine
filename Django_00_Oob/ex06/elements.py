from elem import Elem, Text 

# • html, head, body
# • title
# • meta
# • img
# • table, th, tr, td
# • ul, ol, li
# • h1
# • h2
# • p
# • div
# • span
# • hr
# • br

# html, head, body
class Html(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__('html', content=content, attr=attr)

class Head(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='head', content=content, attr=attr)

class Body(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='body', content=content, attr=attr)

# title, meta, img
class Title(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='title', content=content, attr=attr)

class Meta(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='meta', content=content, attr=attr)

class Img(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='img', content=content, attr=attr, tag_type='simple')

# Table, th, tr, td
class Table(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='table', content=content, attr=attr)

class Th(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='th', content=content, attr=attr)

class Tr(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='tr', content=content, attr=attr)

class Td(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='td', content=content, attr=attr)

# ul, ol, li
class Ul(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='ul', content=content, attr=attr)

class Ol(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='ol', content=content, attr=attr)

class Li(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='li', content=content, attr=attr)

# h1, h2
class H1(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='h1', content=content, attr=attr)
class H2(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='h2', content=content, attr=attr)

# p
class P(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='p', content=content, attr=attr)

# div
class Div(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='div', content=content, attr=attr)

# span
class Span(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='span', content=content, attr=attr)

# hr
class Hr(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='hr', content=content, attr=attr, tag_type='simple')

# br
class Br(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='br', content=content, attr=attr, tag_type='simple')

# 
if __name__ == '__main__':
	print("-------------------------------")
	print('Classes Tests')
	print("-------------------------------")
	print('Html Class,\tOutput:\t\t', Html())
	print('Head Class,\tOutput:\t\t', Head())
	print('Body Class,\tOutput:\t\t', Body())
	print('Title Class,\tOutput:\t\t', Title())
	print('Meta Class,\tOutput:\t\t', Meta())
	print('Img Class,\tOutput:\t\t', Img())
	print('Table Class,\tOutput:\t\t', Table())
	print('Th Class,\tOutput:\t\t', Th())
	print('Tr Class,\tOutput:\t\t', Tr())
	print('Td Class,\tOutput:\t\t', Td())
	print('Ul Class,\tOutput:\t\t', Ul())
	print('Ol Class,\tOutput:\t\t', Ol())
	print('Li Class,\tOutput:\t\t', Li())
	print('H1 Class,\tOutput:\t\t', H1())
	print('H2 Class,\tOutput:\t\t', H2())
	print('P Class,\tOutput:\t\t', P())
	print('Div Class,\tOutput:\t\t', Div())
	print('Span Class,\tOutput:\t\t', Span())
	print('Hr Class,\tOutput:\t\t', Hr())
	print('Br Class,\tOutput:\t\t', Br())

	print("-------------------------------")
	print("html file test1")
	print("-------------------------------")
	print( Html( [Head(), Body()] ) )

	print("-------------------------------")
	print("html file test2")
	print("-------------------------------")

	head = Head(Title(Text('"Hello ground!"')))
	body = Body([H1(Text('"Oh no, not again!"')), Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})])
	print( Html([head, body]) )

	print("-------------------------------")
	print("html file test3")
	print("-------------------------------")

	head = Head([ Meta(attr={'charset': 'UTF-8'}), Meta(attr={'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}),  Title(Text('Test Page'))])

	
	body_titles = [H1(Text('H1 Title')), H2(Text('H2 Title'))]
	img_title = Img(attr={'src': 'https://picsum.photos/seed/picsum/1000/600'})
	paragraph = P(Text('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac tincidunt diam. Nulla facilisi. Nullam in ligula nec purus ultricies interdum. Nullam in ligula nec purus ultricies interdum. Nullam in ligula nec pur'))
	div = Div([Hr(), paragraph, Br()])
	table = Table([Tr([Th(Text('Header 1')), Th(Text('Header 2'))]), Tr([Td(Text('Data 1')), Td(Text('Data 2'))])], attr={'border': '1'})
	ul = Ul([Li(Text('Item 1')), Li(Text('Item 2'))])
	ol = Ol([Li(Text('Item 1')), Li(Text('Item 2'))])
	span = Span(Text('This is a span element'))
	complete_body = []


	for title in body_titles:
		complete_body.append(title)
	# complete_body
	complete_body.append(img_title)
	complete_body.append(div)
	complete_body.append(table)
	complete_body.append(ul)
	complete_body.append(ol)
	complete_body.append(span)
	# print(type(complete_body))
	body = Body(content=complete_body)
	print( Html([head, body]) )
	print("-------------------------------")
	
