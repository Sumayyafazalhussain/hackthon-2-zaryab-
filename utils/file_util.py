def read_file(file_path):
    """
    Reads the content of a file.
    """
    with open(file_path, 'r') as f:
        return f.read()

def write_file(file_path, content):
    """
    Writes content to a file.
    """
    with open(file_path, 'w') as f:
        f.write(content)
