import os

def normalize_file_name(file_name, file_extension):
    if not file_name.endswith(file_extension):
        return file_name + file_extension
    return file_name

def is_existing_file(file_name):
    return os.path.isfile(file_name)

def validate_file(user_input, extension=".xlsx"):
    file_name = normalize_file_name(user_input, extension)
    if is_existing_file(file_name):
        return file_name
    return None