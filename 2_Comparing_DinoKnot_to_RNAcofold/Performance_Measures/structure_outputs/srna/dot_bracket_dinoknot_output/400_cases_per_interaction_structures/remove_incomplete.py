import os

# Specify the directory path you want to search
directory_path = '/home/tara/paper_revisions/srna/dot_bracket_dinoknot_output/400_cases_per_interaction_structures/'

# Iterate through the files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    
    # Check if the file is a regular file (not a directory) and has more than 5 lines
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) > 5:
                # If the file has more than 5 lines, you can choose to keep it or do something with it
                print(f"Keeping file: {filename}")
                # You can move, copy, or perform other actions with the file here.
            else:
                # If the file has 5 or fewer lines, you can choose to delete it or take other actions.
                print(f"Deleting file: {filename}")
                os.remove(file_path)