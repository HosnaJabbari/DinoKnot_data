import pandas as pd
import os
import glob
import re
import csv




def convert_to_bpseq(sequence, structure):

    results = list(structure)
    stack_bracket = []
    stack_paranthesis = []

    for i in range(len(structure)):
        bp = structure[i]
        char = sequence[i]

        if bp in ".:_":
            results[i] = f"{i + 1} {char} 0\n"
        elif bp == "[":
            stack_bracket.append(i)
            results[i] = f"{i + 1} {char} "
        elif bp == "(":
            stack_paranthesis.append(i)
            results[i] = f"{i + 1} {char} "
        elif bp == "]":
            index = stack_bracket.pop()
            results[index] += f"{i + 1}\n"
            results[i] = f"{i + 1} {char} {index + 1}\n"
        elif bp == ")":
            index = stack_paranthesis.pop()
            results[index] += f"{i + 1}\n"
            results[i] = f"{i + 1} {char} {index + 1}\n"
        else:
            print("INCORRECT structure character")
            print2file = False
            break


    return results








def main():
    
    final_output_file_headers = ['interaction',  'free_energy', 'TP', 'FP', 'FN', 'TN', 'TPR', 'PPV', 'MCC']
    final_combined_output_list = []

    # Read in master srna csv files with interaction, positions, expected structure etc.
    snorna_csv = pd.read_csv('/home/tara/paper_revisions/RNAcofold/snorna/snorna_calc.csv') # THIS FILE IS OBTAINED FROM SUPPLEMENTAL MATERIAL https://doi.org/10.1093/nar/gkv1477 , with an appended column "all possible base pairs", calculated using TN equation from paper



    # Path where dinoknot outputs are located
    snorna_input_path = '/home/tara/paper_revisions/RNAcofold/snorna/dot_bracket_RNAcofold_output/single_mfe_structures'




    # Get the list of files - one file per interaction
    snorna_file_list = glob.glob(f'{snorna_input_path}/*snoRNA_output.txt')
 
    
    

    # do process for snorna then repeat for snorna
    for snorna_interaction in snorna_file_list: 

        with open(snorna_interaction, 'r') as snorna_input_file:
            #print(snorna_interaction)

            pair_id = int(re.search(r'(\d+)_RNAcofold_snoRNA_output\.txt', snorna_interaction).group(1)) if re.search(r'(\d+)_RNAcofold_snoRNA_output\.txt', snorna_interaction) else None

            #print("pair_id:", pair_id)
            snorna_lines = snorna_input_file.readlines()
            # Change: read first line instead of list comp

            
            sequence = snorna_lines[1].strip()
            sequence = sequence.replace("&", "")
            #print(sequence)

            structure_line = snorna_lines[2]
            structure = structure_line.split(" ")[0]
            structure = structure.replace("&", "")
            free_energy = structure_line.split(" ")[1]

            #print("sequence:"+ sequence)
            #print("structure:" + str(structure))
            #print("energy:" + str(free_energy))

            #print(len(structure))
            #print(len(sequence))


                
            assert len(sequence) == len(structure), "The length of predicted structure doesn't match the length of input sequence"
            
            bpseq = convert_to_bpseq(sequence, structure)

            #print(bpseq)

            snorna_full_bpseq_file_path = '/home/tara/paper_revisions/RNAcofold/snorna/output_bpseq/single_mfe_structures/full_bpseq/interaction_' + str(pair_id) + '_RNAcofold_output_full_bpseq.csv'
            
            with open(snorna_full_bpseq_file_path, 'w') as output_file:
            # Iterate through the list and write each item to the file
                for item in bpseq:
                    output_file.write(item)

            filtered_dinoknot_bpseq = filter_bpseq_to_snorna_interaction_site(snorna_csv, bpseq, pair_id)

            ## import filtered reference


            # Specify the path to the file
            filtered_reference_bpseq_path = "/home/tara/paper_revisions/RNAcofold/snorna/reference_bpseq/filtered_bpseq/" + str(pair_id) + "_filtered_snorna_ref_output.bpseq" 

            # Initialize an empty list to store the lines
            #filtered_reference_bpseq = []

            # Open the file for reading
            with open(filtered_reference_bpseq_path, 'r') as file:
                # Read each line from the file and append it to the list
                filtered_reference_bpseq = [line for line in file]
            


            TP, FP, FN, TN, TPR, PPV, MCC = calculate_metrics(filtered_reference_bpseq, filtered_dinoknot_bpseq, pair_id, snorna_csv)

            final_result_row = [pair_id, free_energy.strip().strip("(").strip(")"), TP, FP, FN, TN, TPR, PPV, MCC]

            
            final_combined_output_list.append(final_result_row)

 
    final_output_df = pd.DataFrame(final_combined_output_list, columns = final_output_file_headers)                     
    final_output_df.to_csv("/home/tara/paper_revisions/RNAcofold/snorna/calculations/single_mfe_structures/snorna_performance_calculations.csv", index = False)        




def filter_bpseq_to_srna_interaction_site(df, bpseq, pair_id):

    outpath = '/home/tara/paper_revisions/RNAcofold/srna/output_bpseq/single_mfe_structures/filtered_bpseq'

    
    if df['pair_id'].isin([pair_id]).any():
                #print("YES")
                row = df[df['pair_id'] == pair_id].iloc[0]
                srna_site_start = int(row['srna_site_start'])
                srna_site_end = int(row['srna_site_end'])
                srna_length = int(row['srna_length'])
                mrna_site_start = int(row['mrna_site_start'])
                mrna_site_end = int(row['mrna_site_end'])

                #filtered_bpseq = [line for line in bpseq if (mrna_site_start + srna_length + 5) <= int(line.split()[0]) <= (mrna_site_end + srna_length + 5)]
                
                filtered_rows = []
                for row in bpseq:
                    index = int(row.split()[0])
                            # Check if the row falls within the sRNA or mRNA range
                    if (index >= srna_site_start and index <= srna_site_end) or \
                               (index >= (mrna_site_start + srna_length + 1) and index <= (mrna_site_end + srna_length + 1)):  # +5 handles linker
                                filtered_rows.append(row)
                
                # Write the filtered rows to the output directory with the modified filename
                #output_filename = f"interaction_{pair_id}_result_{i}_filtered_srna_dinoknot_output.bpseq"
                #with open(os.path.join(outpath, output_filename), 'w') as outfile:
                 #   outfile.writelines(filtered_rows)

    return filtered_rows



def filter_bpseq_to_snorna_interaction_site(df, bpseq, pair_id):

    outpath = '/home/tara/paper_revisions/RNAcofold/snorna/output_bpseq/single_mfe_structures/filtered_bpseq'

    filtered_rows = []
    if df['pair_id'].isin([pair_id]).any():
        
                row = df[df['pair_id'] == pair_id].iloc[0]
                query_site_start = int(row['query_site_start'])
                query_site_end = int(row['query_site_end'])
                query_length = int(row['query_length'])
                target_site_start = int(row['target_site_start'])
                target_site_end = int(row['target_site_end'])

            
                filtered_rows = []
                for row in bpseq:
                    index = int(row.split()[0])
                            # Check if the row falls within the sRNA or mRNA range
                    if (index >= query_site_start and index <= query_site_end) or \
                               (index >= (target_site_start + query_length ) and index <= (target_site_end + query_length )):
                                filtered_rows.append(row)
                
                # Write the filtered rows to the output directory with the modified filename
                output_filename = f"interaction_{pair_id}_result_filtered_snorna_RNAcofold_output.bpseq"
                with open(os.path.join(outpath, output_filename), 'w') as outfile:
                    outfile.writelines(filtered_rows)

    return filtered_rows



def calculate_metrics(reference_file, dinoknot_file, pair_id, df):

    

    # Initialize counts for TP, FP, and FN
    TP = 0
    FP = 0
    FN = 0
    
    # Iterate through lines in both lists
    for ref_line, dinoknot_line in zip(reference_file, dinoknot_file):
        ref_parts = ref_line.strip().split()
        dinoknot_parts = dinoknot_line.strip().split()

        # Ensure the lines have the expected format (3 columns)
        if len(ref_parts) != 3 or len(dinoknot_parts) != 3:
            continue

        ref_value = int(ref_parts[2])
        dinoknot_value = int(dinoknot_parts[2])

    # Calculate TP, FP, and FN
        if ref_value > 0 and dinoknot_value > 0 and ref_value == dinoknot_value:
            TP += 1
        elif ref_value > 0 and dinoknot_value == 0:
            FN += 1
        elif ref_value == 0 and dinoknot_value > 0:
            FP += 1
        elif ref_value > 0 and dinoknot_value > 0 and dinoknot_value != ref_value:
            FP += 1

    TP = TP /2 if TP >0 else 0
    FP = FP /2 if FP >0 else 0
    FN = FN /2 if FN >0 else 0

    # Calculate TPR and PPV
    TPR = TP / (TP + FN) if TP + FN > 0 else 0
    PPV = TP / (TP + FP) if TP + FP > 0 else 0
    
    row = df[df['pair_id'] == pair_id].iloc[0]
    TN = int(row['all_possible_base_pairs']) - TP
    

    # Calculate MCC
    denominator = ((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)) ** 0.5
    MCC = ((TP * TN) - (FP * FN)) / denominator if denominator != 0 else 0
    return TP, FP, FN, TN, TPR, PPV, MCC





main()

