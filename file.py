def robust_file_processor():
    input_file = input("Enter the input filename: ")
    output_file = input("Enter the output filename: ")

    try:
        # Attempt to read the input file
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Modify content (e.g., simple uppercase conversion)
        modified_content = content.upper()

        # Attempt to write to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Successfully processed '{input_file}' and saved modified content to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: One of the files was not found. Please check '{input_file}' or '{output_file}'.")
    except PermissionError:
        print(f"Error: Permission denied for reading '{input_file}' or writing to '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- To test the combined program ---
# Uncomment and run the line below:
# robust_file_processor()
