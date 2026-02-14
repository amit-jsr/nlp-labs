"""
Bag of Words (BoW) Vectorization

Concepts:
- Bag of Words intuition
- Document-term matrix construction
- Sparse matrix representation
"""

from typing import List
import numpy as np
import pandas as pd


def bag_of_words(corpus: List[List[str]]) -> np.ndarray:
    """
    Create Bag of Words representation of corpus.
    
    Args:
        corpus: List of tokenized documents
        
    Returns:
        NumPy array with BoW representation (documents x vocabulary)
    """
    # TODO: Implement Bag of Words
    pass


def build_document_term_matrix(corpus: List[List[str]]) -> pd.DataFrame:
    """
    Build document-term matrix as DataFrame.
    
    Args:
        corpus: List of tokenized documents
        
    Returns:
        DataFrame with documents as rows and terms as columns
    """
    # TODO: Implement document-term matrix
    pass
