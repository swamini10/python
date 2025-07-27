import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq

# Download only what you need
nltk.download('punkt')
nltk.download('stopwords')

paragraph = """
In Flask, a Blueprint is a way to organize your application into smaller, reusable components. Instead of writing all routes, views, and logic in a single file, Blueprints allow you to group related functionality — such as user authentication, blog posts, or admin panels — into separate modules. Each Blueprint can define its own routes, templates, and static files, and can later be registered to the main Flask app. This makes your project more modular, scalable, and easier to maintain, especially as it grows in size.
"""

# Tokenization and preprocessing
stop_words = set(stopwords.words("english"))
word_tokens = word_tokenize(paragraph)

# Word frequency calculation
word_frequencies = {}
for word in word_tokens:
    word = word.lower()
    if word.isalnum() and word not in stop_words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

# Normalize word frequencies
max_freq = max(word_frequencies.values())
for word in word_frequencies:
    word_frequencies[word] /= max_freq

# Sentence scoring
sentence_scores = {}
sentences = sent_tokenize(paragraph)

for sent in sentences:
    for word in word_tokenize(sent.lower()):
        if word in word_frequencies:
            sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

# Pick top 3 sentences
summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)
summary = " ".join(summary_sentences)

print("Summary:")
print(summary)
