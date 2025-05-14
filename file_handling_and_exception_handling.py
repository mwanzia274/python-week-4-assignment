# File Read & Write Challenge with Error Handling

def read_file(filename):
    """Reads content from the given file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except IOError:
        print(f"Error: Unable to read the file '{filename}'.")
        return None

def write_file(filename, content):
    """Writes content to a given file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Modified content has been written to '{filename}'.")
    except IOError:
        print(f"Error: Unable to write to the file '{filename}'.")

def modify_content(content):
    """Modifies the content of the file."""
    if content:
        modified_content = content.replace("example", "demo")
        modified_content += "\nThis is a new line added by Python."
        return modified_content
    else:
        return None

def main():
    # Ask the user for the filename
    input_filename = "input_file.txt"  # Ensure the input file exists in the same folder
    output_filename = "output_file.txt"

    # Read content from the input file
    content = read_file(input_filename)
    
    # If reading was successful, modify the content and write it to the output file
    if content:
        modified_content = modify_content(content)
        write_file(output_filename, modified_content)

if __name__ == "__main__":
    main()
