import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pytest
from tfprimate.primate_rnaseq import preprocess_data, get_gene_table, get_heatmap


def test_get_gene_table(sfpkm):
    samples = sfpkm.columns[14:]
    gene_symbol = 'ZEB2'
    table = get_gene_table(sfpkm, samples, genesymbol=gene_symbol)
    print("hello")
    print(table.shape)
    # Check the resulting table
    assert isinstance(table, pd.DataFrame)



