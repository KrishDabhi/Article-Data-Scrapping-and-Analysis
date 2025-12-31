import re
import os
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

def load_words_from_file(filepath: str) -> set:
    """Load words from a text file into a set."""
    if not os.path.exists(filepath):
        print(f"Warning: {filepath} not found.")
        return set()
    with open(filepath, "r", encoding="latin1") as f:
            words = {line.strip().lower() for line in f if line.strip()}
    return words

def load_stopwords(stopwords_dir: str) -> set:
    """Load all stopwords from multiple files in the directory."""
    stopword_files = [
        "StopWords_Auditor.txt",
        "StopWords_Currencies.txt",
        "StopWords_DatesandNumbers.txt",
        "StopWords_Generic.txt",
        "StopWords_GenericLong.txt",
        "StopWords_Geographic.txt",
        "StopWords_Names.txt"
    ]
    stopwords = set()
    for filename in stopword_files:
        filepath = os.path.join(stopwords_dir, filename)
        stopwords.update(load_words_from_file(filepath))
    return stopwords

def count_syllables(word: str) -> int:
    """Count syllables in a word."""
    word = word.lower()
    if word.endswith("es") or word.endswith("ed"):
        word = re.sub(r"(es|ed)$", "", word)
    vowels = "aeiouy"
    count = 0
    prev_was_vowel = False
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_was_vowel:
            count += 1
        prev_was_vowel = is_vowel
    return max(1, count)

def is_complex_word(word: str) -> bool:
    """Return True if word has >2 syllables."""
    return count_syllables(word) > 2

class TextAnalyzer:
    def __init__(self, master_dict_dir: str, stopwords_dir: str):
        self.positive_words = load_words_from_file(os.path.join(master_dict_dir, "positive-words.txt"))
        self.negative_words = load_words_from_file(os.path.join(master_dict_dir, "negative-words.txt"))
        self.stopwords = load_stopwords(stopwords_dir)

    def analyze(self, text: str) -> dict:
        if not text.strip():
            return {key: 0 for key in [
                "POSITIVE SCORE", "NEGATIVE SCORE", "POLARITY SCORE", "SUBJECTIVITY SCORE",
                "AVG SENTENCE LENGTH", "PERCENTAGE OF COMPLEX WORDS", "FOG INDEX",
                "AVG NUMBER OF WORDS PER SENTENCE", "COMPLEX WORD COUNT", "WORD COUNT",
                "SYLLABLE PER WORD", "PERSONAL PRONOUNS", "AVG WORD LENGTH"
            ]}

        sentences = sent_tokenize(text)
        words = [word.lower() for word in word_tokenize(text) if word.isalpha()]
        clean_words = [w for w in words if w not in self.stopwords]

        positive_score = sum(1 for w in clean_words if w in self.positive_words)
        negative_score = sum(1 for w in clean_words if w in self.negative_words)

        word_count = len(clean_words)
        sentence_count = len(sentences)

        polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
        subjectivity_score = (positive_score + negative_score) / (word_count + 0.000001) if word_count else 0
        avg_sentence_length = word_count / sentence_count if sentence_count else 0

        complex_words = [w for w in clean_words if is_complex_word(w)]
        complex_word_count = len(complex_words)
        percentage_complex_words = (complex_word_count / word_count) * 100 if word_count else 0
        fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

        syllable_total = sum(count_syllables(w) for w in clean_words)
        syllable_per_word = syllable_total / word_count if word_count else 0

        personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.IGNORECASE))
        avg_word_length = sum(len(w) for w in clean_words) / word_count if word_count else 0

        return {
            "POSITIVE SCORE": positive_score,
            "NEGATIVE SCORE": negative_score,
            "POLARITY SCORE": round(polarity_score, 3),
            "SUBJECTIVITY SCORE": round(subjectivity_score, 3),
            "AVG SENTENCE LENGTH": round(avg_sentence_length, 2),
            "PERCENTAGE OF COMPLEX WORDS": round(percentage_complex_words, 2),
            "FOG INDEX": round(fog_index, 2),
            "AVG NUMBER OF WORDS PER SENTENCE": round(avg_sentence_length, 2),
            "COMPLEX WORD COUNT": complex_word_count,
            "WORD COUNT": word_count,
            "SYLLABLE PER WORD": round(syllable_per_word, 2),
            "PERSONAL PRONOUNS": personal_pronouns,
            "AVG WORD LENGTH": round(avg_word_length, 2)
        }