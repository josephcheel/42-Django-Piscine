from path import Path

if __name__ == '__main__':
	Path('./test').mkdir_p()
	file = Path('./test/test.txt') 
	file.write_text("This is a test")
	file_content = file.read_text()
	print(file_content)