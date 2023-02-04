import os

def rename_files(directory, new_format):
    for filename in os.listdir(directory):
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_format.format(filename)))

# Usage example:
rename_files("/path/to/directory", "new_prefix_{}")