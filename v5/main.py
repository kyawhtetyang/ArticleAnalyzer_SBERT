import json
from src.pipeline import full_pipeline

with open("data/config.json") as f:
    config = json.load(f)

df, sim_matrix = full_pipeline(config)
print("✅ V5 Pipeline finished. Sample output:")
print(df[['articleId','title','sentiment','summary','keywords']])

