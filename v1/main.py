import json
from pipelines.pipeline import full_pipeline

with open("data/config.json") as f:
    config = json.load(f)

df = full_pipeline(config)
print("✅ V1 Pipeline finished. Sample output:")
print(df[['articleId','title','sentiment']])

