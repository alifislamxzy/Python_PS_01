import os

# Get the list of files and directories in the current working directory
directory_contents = os.listdir('+')

# Print the contents of the directory
for item in directory_contents:
    print(item)
