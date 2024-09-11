# Step 1: Write to file
with open("my_file.txt", "w") as file:
    file.write("His street number is 34.\n")
    file.write(" Postal code is 100267.\n")
    file.write(" His phone number ends with 176.\n")

# Step 2: Reading and Displaying the File Content
with open("my_file.txt", "r") as file:
    content = file.read().strip()  # Use strip to remove any leading/trailing spaces
print("Find this guy!:\n", content)

# Step 3: Appending Additional Lines to the File
with open("my_file.txt", "a") as file:
    file.write(" He is 28 years old.\n")
    file.write(" This guy has 2 cars.\n")
    file.write(" He is married with 3 kids.\n")
     
    # Reopen the file to display the updated content
with open("my_file.txt", "r") as file:
    content = file.read().strip()  # Use strip to remove any leading/trailing spaces
print("\n", content)

try:
    # Step 1: Attempt to open a file in write mode
    with open("my_file.txt", "w") as file:
        # Write some content to the file
        file.write("Adding more info about him.\n")
        file.write(" He is 1.7m tall.\n")
    
    # Step 2: Attempt to read from the file
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\n", content)
        
except FileNotFoundError:
    # This block executes if the file is not found
    print("Error: The file you're trying to access does not exist.")
    
except PermissionError:
    # This block executes if there are permission issues
    print("Error: You do not have permission to access or modify this file.")
    
except Exception as e:
    # This catches any other general exceptions
    print(f"An unexpected error occurred: {e}")
    
finally:
    # The finally block will always run, whether an exception occurs or not
    print("File handling operation completed.")
