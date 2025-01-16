
def print_numbers(numbers):
	for number in numbers:
		print(number.strip())

if __name__ == '__main__':
	with open('numbers.txt', 'r') as f:
		numbers = f.readlines()
		numbers = ''.join(numbers).split(",")
		print_numbers(numbers)