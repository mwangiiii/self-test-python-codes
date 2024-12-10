def read_and_modify_file(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes it to a new file.
    Handles file reading and writing errors gracefully.
    """
    try:
        # Read the input file
        with open(input_filename, 'r') as infile:
            content = infile.readlines()

        # Modify the content (e.g., prepend line numbers)
        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]

        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"File has been successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
try:
    # Ask the user for the input file name
    input_file = input("Enter the name of the file to read: ")
    # Ask the user for the output file name
    output_file = input("Enter the name of the file to save the modified content: ")
    
    # Process the files
    read_and_modify_file(input_file, output_file)

except Exception as e:
    print(f"An unexpected error occurred in the program: {e}")
