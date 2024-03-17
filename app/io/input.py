import pandas as pd


def input_from_console():
    """
    Reads text from console.

    Returns:
        str. The text from console.
    """
    return input("Enter some text: ")


def input_from_file(filename):
    """
    Reads text from file.

    Args:
        filename (str): The name of the file.

    Returns:
        str. The text from file if it exists, otherwise returns error message.
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return 'File not found'


def input_from_file_with_pandas(filename):
    """
    Reads data from file using pandas.

    Args:
        filename (str): The name of the file.

    Returns:
        DataFrame. The data frame from file if it exists, otherwise returns error message.
    """
    try:
        data_frame = pd.read_csv(filename)
        return data_frame
    except FileNotFoundError:
        return 'File not found'
