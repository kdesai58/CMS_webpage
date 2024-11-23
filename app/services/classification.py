from transformers import pipeline

classifier = pipeline('zero-shot-classification', model = "facebook/bart-large-mnli")

def classify_document(text, candidate_labels):
    result = classifier(text, candidate_labels)
    return result