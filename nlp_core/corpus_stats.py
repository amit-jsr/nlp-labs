"""
MODULE 6 — Zipf's Law & Distribution Analysis

Concepts:
- Rank vs frequency relationship
- Power-law intuition in language
- Long-tail vocabulary behavior
"""

from typing import Dict
import pandas as pd


def zipf_dataframe(freq_dict: Dict[str, int]) -> pd.DataFrame:
    """
    Create a DataFrame for Zipf's law analysis.
    
    Args:
        freq_dict: Dictionary of word frequencies
        
    Returns:
        DataFrame with rank, word, frequency columns
    """
    # TODO: Implement Zipf dataframe creation
    pass


def plot_zipf_curve(freq_df: pd.DataFrame) -> None:
    """
    Plot Zipf's law curve (log-log plot of rank vs frequency).
    
    Args:
        freq_df: DataFrame from zipf_dataframe function
        
    Returns:
        None (displays plot)
    """
    # TODO: Implement Zipf curve plotting
    pass
