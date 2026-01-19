import os
import subprocess
def run_python_file(working_directory, file_path, args=None):
    try:
        working_directory_abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs_path, file_path))
        valid_target_file = os.path.commonpath([working_directory_abs_path, target_file]) == working_directory_abs_path
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args!= None:
            command.extend(args)
        #continue here_________________________________________________________________________________________
        result = subprocess.run(command,capture_output=True,timeout=30,text=True)
        return_code = result.returncode
        output = ""
        if return_code != 0:
            output += f"Process exited with code {return_code}"
        if result.stderr == "" and result.stdout =="":
            output += "No output produced"
        else:
            output += f"STDOUT:{result.stdout}STDERR:{result.stderr}"
        
        return output
   

    except Exception as e:
        return f"Error: executing Python file: {e}"
    

#print(run_python_file(".","placeholder.py"))