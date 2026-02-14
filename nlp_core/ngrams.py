"""
MODULE 5 — N-grams & Local Language Structure

Concepts:
- Unigram, bigram, trigram generation
- Phrase frequency
- Context windows
- Simple next-word probability from counts
"""

from typing import List, Dict, Tuple


def generate_ngrams(tokens: List[str], n: int) -> List[Tuple]:
    """
    Generate n-grams from token list.
    
    Args:
        tokens: List of tokens
        n: Size of n-gram (1=unigram, 2=bigram, etc.)
        
    Returns:
        List of n-gram tuples
    """
    # TODO: Implement n-gram generation
    pass


def ngram_frequencies(tokens: List[str], n: int) -> Dict[Tuple, int]:
    """
    Calculate n-gram frequencies.
    
    Args:
        tokens: List of tokens
        n: Size of n-gram
        
    Returns:
        Dictionary mapping n-gram to frequency
    """
    # TODO: Implement n-gram frequency calculation
    pass


def next_word_prob(prefix: Tuple, ngram_counts: Dict[Tuple, int]) -> Dict[str, float]:
    """
    Calculate probability distribution for next word given prefix.
    
    Args:
        prefix: Tuple of preceding words
        ngram_counts: Dictionary of n-gram counts
        
    Returns:
        Dictionary mapping possible next words to their probabilities
    """
    # TODO: Implement next word probability
    pass
