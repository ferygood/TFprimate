import pytest
import pandas as pd

@pytest.fixture
def sfpkm():
    df = pd.read_csv("data/nhprtr_refseq_sfpkm_preproccesed.csv")
    return df