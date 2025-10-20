import json
from src.pipeline import full_pipeline

# Load config
with open("data/config.json") as f:
    config = json.load(f)

# Run full pipeline
df, recs = full_pipeline(config)

# Print sample output
print("✅ Pipeline finished. Sample output:")
print(df[['articleId','title','sentiment']].head(2))  # first 2 articles

# Print top 2 recommendations for first 2 articles
for k in list(recs.keys())[:2]:  # first 2 articles
    print(f"\nArticle {k} recommendations (top 2):")
    for a in recs[k][:2]:        # top 2 recommendations
        print({
            'articleId': a['articleId'],
            'title': a['title'],
            'summary': (a['summary'][:50] + '...') if len(a['summary']) > 50 else a['summary'],
            'keywords': a['keywords']
        })

