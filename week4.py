def file_read_write():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ")
        
        # Try to open and read the input file
        with open(input_filename, "r") as input_file:
            content = input_file.read()
        
        # Modify the content (e.g., append some text)
        modified_content = content + "\n\n-- Modified by File Read & Write Program --"
        
        # Ask for the output filename
        output_filename = input("Enter the name of the new file to write: ")
        
        # Write the modified content to the new file
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)
        
        print(f"Modified content successfully written to {output_filename}")
    
    except FileNotFoundError:
        print("Error: The file you are trying to read does not exist. Please check the filename.")
    except IOError:
        print("Error: An error occurred while trying to read or write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
file_read_write()
