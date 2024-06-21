import os


def create_file(filename):
    try:
        with open(filename, 'w') as file:
            file.write('Hello, world!\n')
        print(f"File {filename} created successfully.")
    except IOError:
        print(f"Error: could not create file {filename}")


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except IOError:
        print(f"Error: could not read file {filename}")


def append_file(filename, text):
    try:
        with open(filename, 'a') as file:
            file.write(text)
        print(f"Text appended to file {filename} successfully.")
    except IOError:
        print(f"Error: could not append to file {filename}")


def rename_file(current_filename, new_filename):
    try:
        os.rename(current_filename, new_filename)
        print(f"File {current_filename} renamed to {new_filename} successfully.")
    except OSError:
        print(f"Error: could not rename file {current_filename} to {new_filename}")


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File {filename} deleted successfully.")
    except OSError:
        print(f"Error: could not delete file {filename}")


if __name__ == '__main__':
    filename = "test.txt"
    new_filename = "test1.txt"

    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    read_file(filename)
    # rename_file(filename, new_filename)
    # read_file(new_filename)
    # delete_file(new_filename)

