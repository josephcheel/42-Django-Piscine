import sys, os, re
import settings

class FileExtensionError(Exception):
    pass

def check_file_extension(filename):
    if filename.endswith('.template'):
        return True
    raise FileExtensionError(f"{filename} wrong file extension, should be .template")

def check_file_permission(filename):
    if os.access(filename, os.R_OK):
        return True
    raise PermissionError(f"{filename} permission denied")

def check_file_exists(filename):
    if os.path.exists(filename):
        return True 
    raise FileNotFoundError(f"{filename} not found")

def check_file(filename):
    try: 
        check_file_exists(filename)
        check_file_permission(filename)
        check_file_extension(filename)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def check_settings_import():
    try:
        settings
    except NameError:
        print("Error: settings.py not found")
        sys.exit(1)

def check_args(filename):
    check_file(filename)
    check_settings_import()

def get_settings():
   
    settings_variables = {}
    for name, value in settings.__dict__.items():
        if name in dir(settings) and not name.startswith("__"):
            settings_variables[name] = value
    return settings_variables

def replace_last_occurrence(string, old, new):
    li = string.rsplit(old, 1)
    return new.join(li)

def replace_variables(filename, my_variables):
    output = ""
    with open(filename, 'r') as f:
        content = f.read()
        output = content
        pattern = "{\s*([a-zA-Z])[\w]*\s*}"
        for match in re.finditer(pattern, content):
            var = match.group(0)
            raw_var = match.group(0).replace("{", "").replace("}", "").strip()
            replacement_value = my_variables.get(raw_var, match.group(0))
            if raw_var in my_variables.keys():
                match.group(0).replace(var, str(my_variables[raw_var]))
            else:
                match.group(0).replace(var, "")
                print(f"Warning: {raw_var} not found in settings.py")
            output = output.replace(match.group(0), str(replacement_value))
        return output

def create_new_output_file(new_filename, output):
    with open(new_filename, 'w') as f:
        f.write(output)

def render(filename):

    my_variables = get_settings()
    new_filename = replace_last_occurrence(filename, ".template", ".html")
    print("HTML file generated successfully:", new_filename)
    output_content = replace_variables(filename, my_variables)
    create_new_output_file(new_filename, output_content)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python render.py <file.template>')
        sys.exit(1)
    filename = sys.argv[1]
    check_args(filename)
    render(filename)
