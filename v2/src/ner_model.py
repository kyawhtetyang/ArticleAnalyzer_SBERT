from transformers import pipeline

def load_ner_model(model_name="dbmdz/bert-large-cased-finetuned-conll03-english"):
    return pipeline("ner", model=model_name, grouped_entities=True)

def predict_entities(classifier, texts):
    return [classifier(t) for t in texts]

