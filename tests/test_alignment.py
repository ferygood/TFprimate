import pytest
from tfprimate.alignment import detect_msa_format, draw_msa

@pytest.mark.parametrize(
    "msa_path, expected_format",
    [
        ("data/NANOG.fa.aligned", "fasta"),
        ("data/ENSG00000288616_codon.fa", "fasta")
    ]
)

def test_detect_msa_format(msa_path, expected_format):
    assert detect_msa_format(msa_path) == expected_format