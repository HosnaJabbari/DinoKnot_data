# DinoKnot_data
This folder contains all test data for DinoKnot


This README is organized in sections as presented in the paper.


## qRT-PCR interaction structures

This section contains:

1. the output files containing the dot-bracket interaction structure predicted by DinoKnot within the folder **\1_DinoKnot_structures**.

2. the VARNA visualizations of the dot-bracket interaction structures within the folder **\2_VARNA_Structure_Visualization**.
    - The interaction structures are visualized in linear view and the primer sequence is highlighted in red and the expected binding region is highlighted in green.  

3. the sequences of the forward and reverse primers of the primer-probe sets investigated in the file **3_SARS-CoV-2_qRT-PCR_primer_sequences.txt**.

4. the free energy of the primer structure predicted by Simfold in the file **4_primer_energy.txt**.

5. the sequences in FASTA format of the SARS-CoV-2 (NC_045512.2) gene transcript areas investigated in the file **5_SARS-CoV-2_RNA_transcript_sequences.txt**.

6. the structures of the gene transcript areas prior to interaction predicted by Iterative HFold in dot-bracket format within the folder **\6_SARS-CoV-2_Transcript_Structures**.

7. the WHO qRT-PCR assays containing the sequence of the primer-probe sets investigated in the file **7_whoinhouseassays.pdf**.

## Comparing DinoKnot to RNAcofold

Within the folder **\RNA_cofold_ViennaRNA-2.1.9h** contains:

1. an Excel Spread Sheet containing the reverse primer along with the sequence input into RNAcofold, the output from RNAcofold of the interaction structure in dot-bracket form, and the MFE in the file **1_RNAcofold_input_output.xlsx**. 

2. the terminal output from RNAcofold (the raw terminal log used to generate the data within the excel file from RNAcofold) in the file **2_RNAcofold_terminal_output.txt**.

3. the RNAcofold dot-bracket interaction structures visualized with VARNA in the folder **\3_RNAcofold_terminal_output**.
    - Within this folder the interaction structures are visualized in both linear and nucleic acid view. The primer sequence is highlighted in red and the expected binding region is highlighted in green.  

## Mutations

### Primer/probe binding region

### Variants of Concern

### Clinical report of variant causing N gene detection issues



## Conference Paper

This folder contains data presented in the IEEE ICHI 2021 conference preceeding paper (preliminary results to our study not presented in the journal article).


The folder **\GISAID_mutation_Screenshot_hCoV-19_app** contains screenshots of the GISAID hCoV-19-app on the frequency of mutations in the areas surrounding the primer binding regions of the reverse priemrs, along with the entire genome from the dates July 23, 2020 and March 28 2021. 
