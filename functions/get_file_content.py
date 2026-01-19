import os
from config import MAX_CHARS
def get_file_content(working_directory, file_path):
    try:
        working_directory_abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs_path, file_path))
            

        # Will be True or False
        valid_target_file = os.path.commonpath([working_directory_abs_path, target_file]) == working_directory_abs_path
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        is_file = os.path.isfile(target_file)
        if not is_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        file = open(target_file,"r")
        content = file.read(MAX_CHARS)
        if file.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f"Error: {e}"


# print(get_file_content("calculator", "tests.py"))
    