
def my_var():
	var = [42, "42", "quarante-deux", 42.0, True, [42], {42: 42}, (42,), set()]
	for v in var:
		print(f"{v} has a type {type(v)}")

# 	42 has a type <class 'int'>
# 42 has a type <class 'str'>
# quarante-deux has a type <class 'str'>
# 42.0 has a type <class 'float'>
# True has a type <class 'bool'>
# [42] has a type <class 'list'>
# {42: 42} has a type <class 'dict'>
# (42,) has a type <class 'tuple'>
# set() has a type <class 'set'>

if __name__ == '__main__':
	my_var()