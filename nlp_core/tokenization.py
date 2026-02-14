"""
MODULE 2 — Tokenization

Concepts:
- Sentence tokenization
- Word tokenization
- Character tokenization
- Handling abbreviations, emojis, punctuation joins
"""

import re
from typing import List


def sent_tokenize(text: str) -> List[str]:
    """
    Split text into sentences.
    
    Args:
        text: Input text
        
    Returns:
        List of sentences
    """
    # TODO: Implement sentence tokenization
    pass


def word_tokenize(text: str) -> List[str]:
    """
    Split text into words/tokens.
    
    Args:
        text: Input text
        
    Returns:
        List of word tokens
    """
    # TODO: Implement word tokenization
    pass


def char_tokenize(text: str) -> List[str]:
    """
    Split text into individual characters.
    
    Args:
        text: Input text
        
    Returns:
        List of characters
    """
    # TODO: Implement character tokenization
    pass


def regex_tokenize(text: str, pattern: str) -> List[str]:
    """
    Tokenize text using a custom regex pattern.
    
    Args:
        text: Input text
        pattern: Regex pattern to use for tokenization
        
    Returns:
        List of tokens matching the pattern
    """
    # TODO: Implement regex-based tokenization
    pass
