import os
import pandas as pd

def filter_bpseq_files(input_directory, output_directory, csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Process BP seq files from the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".bpseq"):
            pair_id = int(filename.split('_')[0])
            if df['pair_id'].isin([pair_id]).any():
                print("YES")
                row = df[df['pair_id'] == pair_id].iloc[0]
                query_site_start = int(row['query_site_start'])
                query_site_end = int(row['query_site_end'])
                query_length = int(row['query_length'])
                target_site_start = int(row['target_site_start'])
                target_site_end = int(row['target_site_end'])
                
                filtered_rows = []
                with open(os.path.join(input_directory, filename), 'r') as file:
                    for line in file:
                        parts = line.split()
                        if len(parts) == 3:
                            index = int(parts[0])
                            # Check if the row falls within the query or target range
                            if (index >= query_site_start and index <= query_site_end) or \
                               (index >= (target_site_start + query_length + 5) and index <= (target_site_end + query_length + 5)):
                                filtered_rows.append(line)
                
                # Write the filtered rows to the output directory with the modified filename
                output_filename = f"{pair_id}_filtered_snorna_dinoknot_output.bpseq"
                with open(os.path.join(output_directory, output_filename), 'w') as outfile:
                    outfile.writelines(filtered_rows)

# Example usage:
input_dir = '/home/tara/dinoknot_revisions/final_bpseq_files/dinoknot/snorna'
output_dir = '/home/tara/dinoknot_revisions/final_bpseq_files/dinoknot/snorna/filtered'
csv_file = 'snorna.csv'
filter_bpseq_files(input_dir, output_dir, csv_file)
