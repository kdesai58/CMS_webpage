from transformers import pipeline

summarizer = pipeline("summarization", model="google/flan-t5-small")

def generate_summary(text: str):
    return summarizer(text, max_length=250, min_length=30, do_sample=False)[0]['summary_text']