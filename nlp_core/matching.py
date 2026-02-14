"""
MODULE 8 — Rule-Based Matching & Fuzzy Search

Concepts:
- Exact vs case-insensitive matching
- Keyword search in corpus
- Edit distance intuition
- Simple fuzzy matching thresholds
"""

from typing import List


def exact_match(query: str, text: str) -> bool:
    """
    Check for exact match of query in text.
    
    Args:
        query: Search query
        text: Text to search in
        
    Returns:
        True if exact match found, False otherwise
    """
    # TODO: Implement exact matching
    pass


def contains_keyword(query: str, corpus: List[str]) -> List[int]:
    """
    Find documents containing keyword.
    
    Args:
        query: Keyword to search for
        corpus: List of documents
        
    Returns:
        List of document indices containing the keyword
    """
    # TODO: Implement keyword search
    pass


def levenshtein_distance(a: str, b: str) -> int:
    """
    Calculate Levenshtein (edit) distance between two strings.
    
    Args:
        a: First string
        b: Second string
        
    Returns:
        Edit distance (minimum number of edits to transform a to b)
    """
    # TODO: Implement Levenshtein distance
    pass


def fuzzy_match(query: str, corpus: List[str], threshold: float) -> List[str]:
    """
    Find fuzzy matches in corpus.
    
    Args:
        query: Search query
        corpus: List of strings to search
        threshold: Similarity threshold (0-1)
        
    Returns:
        List of strings from corpus that match above threshold
    """
    # TODO: Implement fuzzy matching
    pass
