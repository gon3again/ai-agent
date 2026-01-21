from google.genai import types

#get_file_info
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)


#get_file_content
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="given a file path relative to working directory, it returns the first 10000 characters of a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="filepath relative to the working directory",
            ),
        },
        required=["file_path"]
    ),
)

#run_python_file
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file, given a filepath relative to the working directory, returning info about the function call",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="filepath relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    ),
                description="additional arguments (deafault is None)",
            ),
        },
        required=["file_path"]
    ),
)

#write_file
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes the given content to a file at given filepath relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="filepath relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="text that is written to a file",
            ),
        },
        required=["file_path","content"],
    ),
)





available_functions = types.Tool(
    function_declarations=[schema_get_files_info,schema_get_file_content,schema_run_python_file,schema_write_file],
)
