"""
TF-IDF (Term Frequency - Inverse Document Frequency)

Concepts:
- Term Frequency - Inverse Document Frequency
- IDF calculation
- TF-IDF matrix construction
"""

from typing import List, Dict
import numpy as np


def compute_idf(corpus: List[List[str]]) -> Dict[str, float]:
    """
    Compute Inverse Document Frequency for each term.
    
    Args:
        corpus: List of tokenized documents
        
    Returns:
        Dictionary mapping terms to their IDF values
    """
    # TODO: Implement IDF computation
    pass


def tfidf_matrix(corpus: List[List[str]]) -> np.ndarray:
    """
    Create TF-IDF matrix for corpus.
    
    Args:
        corpus: List of tokenized documents
        
    Returns:
        NumPy array with TF-IDF representation (documents x vocabulary)
    """
    # TODO: Implement TF-IDF matrix
    pass
