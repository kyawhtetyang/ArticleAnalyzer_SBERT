from transformers import pipeline

def load_ner_model(model_name: str):
    return pipeline("ner", model=model_name, grouped_entities=True)

def predict_entities(classifier, texts):
    return [classifier(t) for t in texts]

