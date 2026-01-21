import os
from google.genai import types
def get_files_info(working_directory, directory="."):
    try:    
        working_directory_abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs_path, directory))
        

        # Will be True or False
        valid_target_dir = os.path.commonpath([working_directory_abs_path, target_dir]) == working_directory_abs_path
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        target_files = os.listdir(target_dir)
        file_info_lines = []
        for file in target_files:
            name = str(file)
            file_size = os.path.getsize(os.path.join(target_dir,name))
            is_dir = os.path.isdir(os.path.join(target_dir,name))
            #print(f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")
            file_info_lines.append(f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")
        file_info_text = "\n".join(file_info_lines)
        return file_info_text
    except Exception as e:
        return f"Error: {e}"



#get_files_info("/home/dustin/workspace/github.com/bootdotdev/curriculum/Ai-agent/calculator")
#print(get_files_info("calculator", "pkg"))





