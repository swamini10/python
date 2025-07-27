from transformers import pipeline
import torch

# Load the summarization model
summarizer = pipeline("summarization")

# Input: Long paragraph
paragraph = """
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines 
that are programmed to think like humans and mimic their actions. The term may also be 
applied to any machine that exhibits traits associated with a human mind such as learning 
and problem-solving. The ideal characteristic of artificial intelligence is its ability 
to rationalize and take actions that have the best chance of achieving a specific goal. 
Machine learning is a subset of AI which refers to the concept that computer programs can 
automatically learn from and adapt to new data without being assisted by humans.
"""

# Summarize the paragraph
summary = summarizer(paragraph, max_length=80, min_length=30, do_sample=False, model="facebook/bart-large-cnn" )

#" Output
print("Summary:")
print(summary[0]['summary_text'])
