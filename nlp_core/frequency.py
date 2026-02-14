"""
MODULE 4 — Vocabulary & Frequency Statistics

Concepts:
- Unique word counts
- Term frequency
- Most/least common tokens
- Document length statistics
- Corpus-level summaries
"""

from typing import List, Dict, Set, Tuple


def build_vocabulary(corpus: List[List[str]]) -> Set[str]:
    """
    Build vocabulary from corpus.
    
    Args:
        corpus: List of tokenized documents
        
    Returns:
        Set of unique tokens
    """
    # TODO: Implement vocabulary building
    pass


def term_frequency(tokens: List[str]) -> Dict[str, int]:
    """
    Calculate term frequency for a document.
    
    Args:
        tokens: List of tokens from a document
        
    Returns:
        Dictionary mapping token to its frequency
    """
    # TODO: Implement term frequency calculation
    pass


def top_k_words(freq_dict: Dict[str, int], k: int) -> List[Tuple[str, int]]:
    """
    Get the top-k most frequent words.
    
    Args:
        freq_dict: Dictionary of word frequencies
        k: Number of top words to return
        
    Returns:
        List of (word, frequency) tuples sorted by frequency
    """
    # TODO: Implement top-k word selection
    pass


def corpus_statistics(corpus: List[List[str]]) -> Dict:
    """
    Calculate corpus-level statistics.
    
    Args:
        corpus: List of tokenized documents
        
    Returns:
        Dictionary with various corpus statistics
    """
    # TODO: Implement corpus statistics
    pass
