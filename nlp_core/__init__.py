# NLP Core Module
# Basic NLP utilities for text processing and analysis

from .cleaning import clean_text, normalize_unicode, remove_punctuation, basic_preprocess
from .tokenization import sent_tokenize, word_tokenize, char_tokenize, regex_tokenize
from .normalization import remove_stopwords, stem_tokens, lemmatize_tokens, compare_vocab_sizes
from .frequency import build_vocabulary, term_frequency, top_k_words, corpus_statistics
from .ngrams import generate_ngrams, ngram_frequencies, next_word_prob
from .corpus_stats import zipf_dataframe, plot_zipf_curve
from .regex_utils import extract_emails, extract_phone_numbers, extract_urls, extract_dates, regex_extract
from .matching import exact_match, contains_keyword, levenshtein_distance, fuzzy_match

__all__ = [
    # cleaning
    "clean_text", "normalize_unicode", "remove_punctuation", "basic_preprocess",
    # tokenization
    "sent_tokenize", "word_tokenize", "char_tokenize", "regex_tokenize",
    # normalization
    "remove_stopwords", "stem_tokens", "lemmatize_tokens", "compare_vocab_sizes",
    # frequency
    "build_vocabulary", "term_frequency", "top_k_words", "corpus_statistics",
    # ngrams
    "generate_ngrams", "ngram_frequencies", "next_word_prob",
    # corpus_stats
    "zipf_dataframe", "plot_zipf_curve",
    # regex_utils
    "extract_emails", "extract_phone_numbers", "extract_urls", "extract_dates", "regex_extract",
    # matching
    "exact_match", "contains_keyword", "levenshtein_distance", "fuzzy_match",
]
