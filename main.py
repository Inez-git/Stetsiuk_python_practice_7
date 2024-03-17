from app.io import input
from app.io import output


def main():
    text_from_console = input.input_from_console()
    text_from_file = input.input_from_file('./data/input_file.txt')
    text_from_file_pandas = input.input_from_file_with_pandas('./data/username.csv')

    output.output_to_console(text_from_console)
    print('='*30)
    output.output_to_console(text_from_file)
    print('=' * 30)
    output.output_to_console(text_from_file_pandas)
    print('=' * 30)

    text_to_file = "My name is Inna"
    output.output_to_file(text_to_file, './data/output_file.txt')


if __name__ == '__main__':
    main()
