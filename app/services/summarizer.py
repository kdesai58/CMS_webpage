import os

# Disable parallelism to avoid deadlocks
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Importing required libraries
from transformers import pipeline, AutoTokenizer

# Load the BART summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

# Function to generate a summary of the input text
def generate_summary(text: str):
    # Tokenize the input text to get the number of tokens
    input_tokens = tokenizer.encode(text, truncation=True)
    
    # Check if the number of tokens is too large for the model
    if len(input_tokens) > 1024:  # BART's maximum token limit
        return "Text is too long to summarize. Please provide a text with fewer than 1024 tokens."
    
    return summarizer(text, max_length=200, min_length=50, do_sample=False)[0]['summary_text']