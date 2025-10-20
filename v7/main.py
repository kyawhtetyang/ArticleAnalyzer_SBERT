import json
from src.pipeline import full_pipeline

with open("data/config.json") as f:
    config = json.load(f)

df, recs = full_pipeline(config)
print("✅ V7 Pipeline finished. Sample output:")
print(df[['articleId','title','sentiment','summary','keywords']].head(2))
for k in list(recs.keys())[:2]:  # first 2 articles
    print(f"\nArticle {k} recommendations (top 2):")
    for a in recs[k][:2]:        # top 2 recommendations
        print({
            'articleId': a['articleId'],
            'title': a['title'],
            'summary': (a['summary'][:50] + '...') if len(a['summary']) > 50 else a['summary'],
            'keywords': a['keywords']
        })

