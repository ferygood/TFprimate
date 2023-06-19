#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:24:10 2023

@author: Ekin Deniz Aksu
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess_data(fpkm_file):
    data = pd.read_csv(fpkm_file, sep='\t', header=None, comment='#', dtype=str)
    header = []
    with open(fpkm_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                header.append(line.strip().split('\t'))
            else:
                break
    
    header[7][0] = 'gene_symbol'
    header[7][12] = 'sumofreads'
    data.columns = [x.replace('#','') for x in header[7]]
    data.columns = [x.replace('BrainLeft', 'Brain') for x in data.columns]
    #data.columns = [x.replace('BrainRight', 'Brain') for x in data.columns]
    data.columns = [x.replace('Heart1', 'Heart') for x in data.columns]
    
    data.drop('Heart2_notThm_MST', axis=1, inplace=True)
    data.drop('Liver_mRNA_CMM', axis=1, inplace=True)
    data.drop('Liver_mRNA_CMC', axis=1, inplace=True)
    data.drop('BrainRight_MST', axis=1, inplace=True)
    
    samples = data.columns[13:]
    data[samples] = data[samples].replace({"NE/": "", "NA/":""}, regex=True)
    data[samples] = data[samples].astype(float)
    
    return data, samples

def get_gene_table(data, samples, genesymbol=None, ensemblid=None):
    
    if genesymbol:
        selected_row = data.loc[data.gene_symbol == genesymbol, samples]
    elif ensemblid:
        selected_row = data.loc[data.ensembl_id == ensemblid, samples]
    else:
        print("get_gene_table: No gene selected. Use gene_symbol or ensemblid paramaters.")
        return None

    new_data = {}
    # Iterate over the column names and extract the tissue and species information
    for column in selected_row.columns:
        tissue, species = column.split('_')
        if tissue not in new_data:
            new_data[tissue] = {}
        new_data[tissue][species] = selected_row[column].iloc[0]
    
    new_df = pd.DataFrame(new_data).transpose()
    return new_df

def get_heatmap(table, gene, output=False):
    plt.figure(figsize=(18,12))
    sns.heatmap(table, cmap='Blues', annot=True, fmt=".1f", cbar_kws={'label': 'sFPKM'})
    
    plt.title(f'Gene {gene}\nTissue-Species Heatmap', fontsize=16)
    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)
    
    if output:
        plt.savefig(output, format='png')
    else:
        plt.show()
        
if __name__ == '__main__':
    
    # Main file will be "Tissue_export.RefSeq.GENE.u.sFPKM.txt"
    #fpkm_file = '../../data/nhprtr_refseq_sFPKM_test.csv'
    preprocessed_data = pd.read_csv('../../data/nhprtr_refseq_sfpkm_preproccesed.csv')
    samples = preprocessed_data.columns[14:]
    gene_ensembl_id = 'ENSG00000111640'
    
    #data, samples = preprocess_data(fpkm_file)
    table = get_gene_table(preprocessed_data, samples, ensemblid=gene_ensembl_id)
    get_heatmap(table, gene_ensembl_id, output= '../../tests/test_rnaseq.png')
