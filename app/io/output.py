
def output_to_console(text):
    """
    Prints text to console.

    Args:
        text (str): Text to be printed.

    Returns:
        None.
    """
    print(text)
    return None


def output_to_file(text, filename):
    """
    Writes text to the file. If the file does not exist, it will be created.
    If the file already exists, it will be overwritten.

    Args:
        text (str): The text to be written.
        filename (str): The name of the file.

    Returns:
        None.
    """
    with open(filename, 'w') as file:
        file.write(text)
    return None
