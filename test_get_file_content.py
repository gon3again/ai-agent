from functions.get_file_content import get_file_content

s = get_file_content("calculator", "lorem.txt")
# print(f"length: {len(s)}")
# print(s[-500:])


print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat") )
print(get_file_content("calculator", "pkg/does_not_exist.py"))
