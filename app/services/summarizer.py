

from transformers import pipeline


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text: str):
    if(len(text) > 512):
        return "Text is too long to summarize. please provide a pdf with less than 512 words"
    return summarizer(text, max_length=200, min_length=50, do_sample=False)[0]['summary_text']