import sys

def open_file(file_name):
	try:
		with open(file_name, "r") as f:
			return f.readlines()
	except FileNotFoundError:
		print("File not found")
		sys.exit(1)

def parse_input():
	periodic_table_file = open_file("periodic_table.txt")
	periodic_table = []
	for values in periodic_table_file:
		element_periodic_table = {}
		values = values.strip()
		name = str(values).split("=")[0].strip()
		element_periodic_table.update({"name": name})
		values = str(values).split("=")[1]
		values = values.split(",")
		for value in values:
			value = value.strip().split(":")
			element_periodic_table.update({value[0]: value[1]})
		periodic_table.append(element_periodic_table)
	return periodic_table


# def create_html_file():
# 	with open("periodic_table.html", "w") as f:
# 		f.write("<html>\n")
# 		f.write("<head>\n")
# 		f.write("<title>Periodic Table</title>\n")
# 		f.write("</head>\n")
# 		f.write("<body>\n")
# 		f.write("<table>\n")
# 		f.write("<tr>\n")
# 		f.write("<th>Name</th>\n")
# 		f.write("<th>Symbol</th>\n")
# 		f.write("<th>Atomic number</th>\n")
# 		f.write("<th>Atomic mass</th>\n")
# 		f.write("</tr>\n")
# 		f.write("</table>\n")
# 		f.write("</body>\n")
# 		f.write("</html>\n")

def create_html_file(periodic_table):
		with open("periodic_table.html", "w") as f:
			f.write("<html>\n")
			f.write("<head>\n")
			f.write("<title>Periodic Table</title>\n")
			f.write("</head>\n")
			f.write("<body>\n")
			f.write("<table border='1'>\n")
			f.write("<tr>\n")
			f.write("<th>Name</th>\n")
			f.write("<th>Symbol</th>\n")
			f.write("<th>Atomic number</th>\n")
			f.write("<th>Atomic mass</th>\n")
			f.write("</tr>\n")
			for element in periodic_table:
				f.write("<tr>\n")
				f.write(f"<td>{element['name']}</td>\n")
				# f.write(f"<td>{element['symbol']}</td>\n")
				f.write(f"<td>{element['number']}</td>\n")
				# f.write(f"<td>{element['weight']}</td>\n")
				f.write("</tr>\n")
			f.write(f"<td>{element['symbol']}</td>\n")
			f.write(f"<td>{element['weight']}</td>\n")
			f.write("</tr>\n")
			f.write("</table>\n")
			f.write("</body>\n")
			f.write("</html>\n")

	
if __name__ == '__main__':
	periodic_table = parse_input()
	# length = len(periodic_table)
	# print(f"Found {length} elements")
	print(periodic_table)
	create_html_file(periodic_table)

