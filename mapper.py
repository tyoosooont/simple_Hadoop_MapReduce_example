#!/usr/bin/env python3
import sys
import re

# Define a basic list of English stopwords
stopwords = {
    'the', 'and', 'to', 'of', 'a', 'in', 'that', 'it', 'is', 'was', 'he', 'for',
    'on', 'with', 'as', 'his', 'i', 'at', 'by', 'an', 'be', 'this', 'have', 'from',
    'or', 'one', 'had', 'not', 'but', 'what', 'all', 'were', 'we', 'when', 'your',
    'can', 'there', 'their', 'so', 'if', 'me', 'my', 'them', 'no', 'are', 'you', 'do',
    'who', 'which', 'will', 'would', 'could', 'should', 'been', 'he', 'she', 'they',
    'them', 'i', 'you', 'its', 'then', 'because', 'into', 'out', 'about'
}

for line in sys.stdin:
    line = line.strip().lower()
    # Remove punctuation
    line = re.sub(r'[^\w\s]', '', line)
    words = line.split()
    for word in words:
        if word and word not in stopwords:
            print(f"{word}\t1")
