"""
MODULE 3 — Stopwords, Stemming, Lemmatization

Concepts:
- When stopword removal helps or harms
- Porter vs Snowball stemming
- Lemmatization with POS tagging
- Vocabulary comparison across normalization methods
"""

from typing import List, Dict


def remove_stopwords(tokens: List[str]) -> List[str]:
    """
    Remove stopwords from token list.
    
    Args:
        tokens: List of word tokens
        
    Returns:
        Filtered list without stopwords
    """
    # TODO: Implement stopword removal
    pass


def stem_tokens(tokens: List[str]) -> List[str]:
    """
    Apply stemming to tokens.
    
    Args:
        tokens: List of word tokens
        
    Returns:
        List of stemmed tokens
    """
    # TODO: Implement stemming
    pass


def lemmatize_tokens(tokens: List[str], pos: bool = True) -> List[str]:
    """
    Apply lemmatization to tokens.
    
    Args:
        tokens: List of word tokens
        pos: Whether to use POS tagging for better lemmatization
        
    Returns:
        List of lemmatized tokens
    """
    # TODO: Implement lemmatization
    pass


def compare_vocab_sizes(token_lists: Dict[str, List[str]]) -> Dict[str, int]:
    """
    Compare vocabulary sizes across different normalization methods.
    
    Args:
        token_lists: Dictionary mapping method name to token list
        
    Returns:
        Dictionary mapping method name to unique vocabulary size
    """
    # TODO: Implement vocabulary size comparison
    pass
