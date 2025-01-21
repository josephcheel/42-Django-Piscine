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

def create_html_file(content):
		with open("periodic_table.html", "w") as f:
			f.write(content)

def generate_html_periodic_element(element: dict) -> str:
	html_element = ' ' * 16 + "<td style=\"border: 1px solid black; padding:10px;\">\n"
	html_element += ' ' * 20 + f"<h4>{element['name']}</h4>\n"
	html_element += ' ' * 20 + "<ul>\n"
	html_element += ' ' * 24 + f"<li>Symbol: {element['small']}</li>\n"
	html_element += ' ' * 24 + f"<li>Atomic Number: {element['number']}</li>\n"
	html_element += ' ' * 24 + f"<li>Atomic Mass: {element['molar']}</li>\n"
	html_element += ' ' * 20 + "</ul>\n"
	html_element += ' ' * 16 + "</td>\n"
	return html_element

def main():
	periodic_table = parse_input()
	file_content = "<!DOCTYPE html>\n\
<html lang=\"en\">\n\
<head>\n\
    <meta charset=\"UTF-8\">\n\
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\
    <title>periodic table</title>\n\
</head>\n\
<body>\n"

	file_content += '    <table>\n            <tr>\n'
	printing_index = 0
	for element in periodic_table:
		if int(element["position"]) < printing_index:
			printing_index = 0
			file_content += " </tr><tr>\n"
		for _ in range(printing_index, int(element["position"]) - 1):
			file_content += ' ' * 16 + "<td></td>\n"
		printing_index = int(element["position"])
		file_content += generate_html_periodic_element(element)
	
	file_content += ' ' * 16 + '</tr>\n'
	file_content += ' ' * 12 + '</table>\n'
	file_content += ' ' * 8 + '</body>\n'
	file_content += '</html>\n'
	create_html_file(file_content)


if __name__ == '__main__':
	main()
	

