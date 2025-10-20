import json
from src.pipeline import full_pipeline

with open("data/config.json") as f:
    config = json.load(f)

df = full_pipeline(config)
print("✅ V4 Pipeline finished. Sample output:")
print(df[['articleId','title','sentiment','summary']])

