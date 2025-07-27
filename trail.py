import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

text = "This is a test. This should be tokenized into two sentences."
print(sent_tokenize(text))
