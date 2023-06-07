import sys

def print_script_and_variables():
    script_name = sys.argv[0]
    
    print("Script name:", script_name)
    
    if len(sys.argv) > 1:
        variables = " ".join(sys.argv[1:])
        print("Script name and variables:", script_name, variables)
    else:
        print("No variables provided.")

# Example usage
print_script_and_variables()
