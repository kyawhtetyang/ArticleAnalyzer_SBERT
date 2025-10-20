from transformers import pipeline

def load_summarizer(model_name: str):
    return pipeline("summarization", model=model_name)

def summarize_text(classifier, texts):
    summaries = []
    for t in texts:
        max_len = min(len(t.split()) + 3, 8)  # dynamic max length
        min_len = min(len(t.split()), 5)      # dynamic min length
        summary = classifier(t, max_length=max_len, min_length=min_len, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    return summaries


