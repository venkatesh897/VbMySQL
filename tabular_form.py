def get_max_length_field_name(field_names):
    max_length_field_name = field_names[0]
    for field_name in field_names:
        if len(max_length_field_name) < len(field_name):
            max_length_field_name = field_name   
    return max_length_field_name

def get_max_length_field_value(field_values):
    max_length_field_value = field_values[0][0]
    for field_value in field_values:
        for index in range(len(field_value)):
            if len(str(max_length_field_value)) < len(str(field_value)):
                max_length_field_value = field_value[index]
    return max_length_field_value

def get_max_length_name(field_names, field_values):
	max_length_field_value = get_max_length_field_value(field_values)
	max_length_field_name = get_max_length_field_name(field_names)
	if len(str(max_length_field_name)) < len(str(max_length_field_value)):
		max_length_name = max_length_field_value
	else:
		max_length_name = max_length_field_name
	return max_length_name

def print_column_names(field_names, field_values):
	max_length_name = get_max_length_name(field_names, field_values)
	print_pipe(field_names, field_values)
	for field_name in field_names:
		print("|", end = "")
		print(field_name,end = "")
		print(" " * (len(str(max_length_name)) - len(field_name)), end = "")
	print("|", end = "")
	print("\t")
	print_pipe(field_names, field_values)
	
def print_field_values(field_names, field_values):
	max_length_name = get_max_length_name(field_names, field_values)
	for field_value in field_values:
		for index in range(len(field_value)):
			print("|", end = "")
			print(str(field_value[index]), end = "")
			print(" " * ((len(str(max_length_name)) - (len(str(field_value[index]))))), end = "")
		print("|", end = "")
		print("\t")

def print_pipe(field_names, field_values):
	max_length_name = get_max_length_name(field_names, field_values)
	for field_name in field_names:
		print("+", end ="")
		print("-" * len((str(max_length_name))), end ="")
	print("+", end = "")
	print("\t")
