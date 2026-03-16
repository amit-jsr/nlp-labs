"""
MODULE 1 — Text Cleaning & Normalization

Concepts:
- Lowercasing strategies
- Unicode normalization
- Removing punctuation, digits, symbols
- Whitespace cleanup
- HTML / special character removal
- Expanding contractions
"""

import re
import unicodedata
import string

class TextCleaner:
    """
    Class for comprehensive text cleaning and normalization.
    """

    def clean_text(self, text: str) -> str:
        """
        Apply comprehensive text cleaning.
        
        Args:
            text: Raw input text
            
        Returns:
            Cleaned text with normalized whitespace and lowercase
        """
        # Example pipeline: normalize unicode, lowercase, remove punctuation, clean whitespace
        text = self.normalize_unicode(text)
        text = text.lower()
        text = self.remove_punctuation(text)
        text = self.clean_whitespace(text)
        return text

    def normalize_unicode(self, text: str) -> str:
        """
        Normalize unicode characters to their canonical form (NFC).
        
        Args:
            text: Input text with potential unicode variations
            
        Returns:
            Unicode normalized text (NFC form)
        """
        return unicodedata.normalize('NFC', text)

    def remove_punctuation(self, text: str) -> str:
        """
        Remove all punctuation from text.
        
        Args:
            text: Input text
            
        Returns:
            Text with punctuation removed
        """
        return text.translate(str.maketrans('', '', string.punctuation))

    def clean_whitespace(self, text: str) -> str:
        """
        Normalize and clean up whitespace.
        
        Args:
            text: Input text
            
        Returns:
            Text with cleaned whitespace
        """
        return re.sub(r'\s+', ' ', text).strip()

    def basic_preprocess(self, text: str) -> str:
        """
        Apply basic preprocessing pipeline: lowercase, normalize, clean whitespace.
        
        Args:
            text: Raw input text
            
        Returns:
            Preprocessed text
        """
        text = self.normalize_unicode(text)
        text = text.lower()
        text = self.clean_whitespace(text)
        return text
