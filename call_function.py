from google.genai import types
from functions import get_file_content,get_files_info,run_python_file,write_file_content

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


def call_function(function_call:types.FunctionCall, verbose=False):
    function_name = function_call.name or ""
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")
    pass

    function_map = {
    "get_file_content": get_file_content.get_file_content,
    "get_files_info": get_files_info.get_files_info,
    "run_python_file": run_python_file.run_python_file,
    "write_file": write_file_content.write_file,   
    }
    if function_name not in function_map:
        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    args = dict(function_call.args) if function_call.args else {}
    args["working_directory"] = "./calculator"

    function_result = function_map[function_name](**args)

    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"result": function_result},
            )
        ],
    )