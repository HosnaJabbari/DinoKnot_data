# DinoKnot_data
This folder contains all test data for DinoKnot


This README and the corresponding data is organized in sections as presented in the Materials and Methods section of our paper.


## qRT-PCR interaction structures

This section contains:

1. the output files containing the dot-bracket interaction structure predicted by DinoKnot within the folder **\1_DinoKnot_structures\reverse_primer_RNA_transcript_interaction**.
    - The sequence of the interaction structure is located on the 5th line from the bottom of the .txt file (Seq:) (eg. line 401 of *2019-nCoV-N1-R_reference_genome_NC_045512.2.txt*) 
    - The structure of the interaction structure in dot-bracket form is located on the 3rd line from the bottom of the .txt file (Result_0:) (eg. line 403 of *2019-nCoV-N1-R_reference_genome_NC_045512.2.txt*)
    - The Free Energy of the interaction structure is located on the second line from the bottom if the .txt file (Energy_0:) (eg. line 404 of *2019-nCoV-N1-R_reference_genome_NC_045512.2.txt*)

2. the VARNA visualizations of the dot-bracket interaction structures within the folder **\2_VARNA_Structure_Visualization**.
    - The interaction structures are visualized in linear view and the primer sequence is highlighted in red and the expected binding region is highlighted in green.  
    - The sequence (Seq:) and dot-bracket structure (Result_0:) from the DinoKnot output is input into VARNA to get the structure visualizations. 

3. the sequences of the forward and reverse primers of the primer-probe sets investigated in the file **3_SARS-CoV-2_qRT-PCR_primer_sequences.txt**.

4. the free energy of the primer structure predicted by Simfold in the file **4_primer_energy.txt**.

5. the sequences in FASTA format of the SARS-CoV-2 (NC_045512.2) gene transcript areas investigated in the file **5_SARS-CoV-2_RNA_transcript_sequences.txt**.

6. the structures of the gene transcript areas prior to interaction predicted by Iterative HFold in dot-bracket format within the folder **\6_SARS-CoV-2_Transcript_Structures**.

7. the WHO qRT-PCR assays containing the sequence of the primer-probe sets investigated in the file **7_whoinhouseassays.pdf**.

## Comparing DinoKnot to RNAcofold

Within the folder **\2_Comparing_DinoKnot_to_RNAcofold\RNA_cofold_ViennaRNA-2.1.9h** contains:

1. an Excel Spread Sheet containing the reverse primer along with the sequence input into RNAcofold, the output from RNAcofold of the interaction structure in dot-bracket form, and the MFE in the file **1_RNAcofold_input_output.xlsx**. 

2. the terminal output from RNAcofold (the raw terminal log used to generate the data within the excel file from RNAcofold) in the file **2_RNAcofold_terminal_output.txt**.

3. the RNAcofold dot-bracket interaction structures visualized with VARNA in the folder **\3_RNAcofold_terminal_output**.
    - Within this folder the interaction structures are visualized in both linear and nucleic acid view. The primer sequence is highlighted in red and the expected binding region is highlighted in green.  

## Mutations

### 1. Primer/probe binding region

Within the folder **\1_Primer_probe_binding_region** contains: 

1. The output interaction structures of the corresponding primer/probe and the mutated SARS-CoV-2 gene area predicted by DinoKnot in dot-bracket form within the folder **\1_DinoKnot_Mutations_in_primer_binding_region**. 

2. The interaction structure visualizations of the corresponding primer/probe and the mutated SARS-CoV-2 gene area within the folder  **\2_VARNA_Visualization_Mutation_in_primer_binding_region_Structures**. 


Note: Both folders are organized with sub-folders labelled with the affected primer/probe. 
- For example, the folder **\1_DinoKnot_Mutations_in_primer_binding_region\2019-nCoV-N1-P** contains the DinoKnot output for the interaction structure of the 2019-nCoV-N1-P probe with the reference genome within the *2019-nCoV-N1-P_reference_genome_NC_045512.2_DNA/DNA.txt* file and the mutated genome within the file *2019-nCoV-N1-P_C28,311T_mutation_DNA/DNA.txt*
- For example, the folder **2_VARNA_Visualization_Mutation_in_primer_binding_region_Structures\2_VARNA_Visualization_Mutation_in_primer_binding_region_Structures** contains the VARNA interaction structure visualation to the reference genome in the file *2019_nCoV_N1-P.jpg* and the visualization of the mutated genome in the file *2019_nCoV-N1-P_28311C>T.jpg*. 
- The reference genome data is present in each folder to be able to compare the mutation to the reference genome. 


### 2. Variants of Concern

Within the folder **\2_Variants_of_Concern** contains: 

1. The interaction structure of the reverse primer and the gene area transcript of the variant of concern with mutations in this area predicted by DinoKnot in dot-bracket form the folder **DinoKnot_Structures**. This folder contains subfolders for each of the variants of concern studied. 

### 3. Clinical report of variant causing N gene detection issues

Within the folder **\3_Clinical_report_of_variant_causing_N gene_detection_issues** contains: 

1. the DinoKnot predicted interaction structure in dot-bracket form of the CCDC-N-F primer with the variant strain (accession ID: EPI_ISL_1061414) in the file **CCDC-N-F_EPI_ISL_1061414_DinoKnot_output.txt**

2. the VARNA interaction structure visualization of the CCDC-N-F primer with the variant strain (accession ID: EPI_ISL_1061414) in the file **CCDC-N-F_EPI_ISL_1061414_VARNA_Structure.png**.

3.  the DinoKnot predicted interaction structure in dot-bracket form of the CCDC-N-P probe with the variant strain (accession ID: EPI_ISL_1061414) in the file **CCDC-N-P_EPI_ISL_1061414_DinoKnot_output(PROBE).txt**

4.  the DinoKnot predicted interaction structure in dot-bracket form of the CCDC-N-R primer with the variant strain (accession ID: EPI_ISL_1061414) in the file **CCDC-N-R_EPI_ISL_1061414_DinoKnot_output(REVERSE).txt**

5. the same data as #1-4 above but for the corresponding primer and probe with the SARS-CoV-2 reference genome (NC_045512.2) in the folder **\Reference_Genome_Comparison** to be able to compare the variant strain to the reference genome.





## Conference Paper

This folder contains data presented in the IEEE ICHI 2021 conference preceeding paper that are not presented in the journal article: https://ieeexplore.ieee.org/document/9565741 
(The conference paper contains preliminary results to our study)


The folder **\GISAID_mutation_Screenshot_hCoV-19_app** contains screenshots of the GISAID hCoV-19-app on the frequency of mutations in the areas surrounding the primer binding regions of the reverse primers, along with the entire genome from the dates July 23, 2020 and March 28 2021. 
