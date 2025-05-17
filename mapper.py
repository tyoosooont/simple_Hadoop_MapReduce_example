#!/usr/bin/env python3
import sys
import re

# Modern English stopwords
modern_stopwords = {
    'the', 'and', 'to', 'of', 'a', 'in', 'that', 'it', 'is', 'was', 'he', 'for',
    'on', 'with', 'as', 'his', 'i', 'at', 'by', 'an', 'be', 'this', 'have', 'from',
    'or', 'one', 'had', 'not', 'but', 'what', 'all', 'were', 'we', 'when', 'your',
    'can', 'there', 'their', 'so', 'if', 'me', 'my', 'them', 'no', 'are', 'you', 'do',
    'him', 'her', 'will', 'our', 'now', 'they', 'she', 'would', 'which', 'how', 'am'
}

# Shakespearean stopwords
shakespearean_stopwords = {
    'thou', 'thy', 'thee', 'thine', 'ye', 'hath', 'doth',
    'art', 'wilt', 'shalt', 'canst', 'couldst', 'wouldst',
    'shouldst', 'mayst', 'mightst', 'must', 'didst', 'wert',
    'tis', 'twas', 'oft', 'nay', 'aye', 'ere', 'wherefore',
    'shall', 'o'
}

# Combined stopwords
stopwords = modern_stopwords.union(shakespearean_stopwords)

# Process each line from standard input
for line in sys.stdin:
    line = line.strip().lower()
    line = re.sub(r'[^\w\s]', '', line)  # remove punctuation
    words = line.split()
    for word in words:
        if word and word not in stopwords:
            print(f"{word}\t1")
