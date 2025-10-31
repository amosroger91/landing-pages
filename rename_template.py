
import argparse
import os

def replace_in_file(filepath, long_name, short_name):
    """
    Replaces all occurrences of "Sample-Long-Name" and "Sample-Short-Name" with the provided names in a file.

    Args:
        filepath (str): The path to the file to modify.
        long_name (str): The long name to replace the placeholder with.
        short_name (str): The short name to replace the placeholder with.
    """
    try:
        # Ensure the file exists
        if not os.path.exists(filepath):
            print(f"Error: File not found at {filepath}")
            return

        # Read the file content
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Perform the replacements
        new_content = content.replace("Sample-Long-Name", long_name)
        new_content = new_content.replace("Sample-Short-Name", short_name)

        # Write the modified content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)

        print(f"Successfully replaced placeholders in {filepath}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Replace placeholders in a file with given long and short names.")
    parser.add_argument("long_name", help="The long name to use for replacement.")
    parser.add_argument("short_name", help="The short name to use for replacement.")
    parser.add_argument("filepath", help="The path to the file to modify.")

    args = parser.parse_args()

    replace_in_file(args.filepath, args.long_name, args.short_name)
