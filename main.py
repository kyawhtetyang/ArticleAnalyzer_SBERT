import json
from src.news_pipeline import NewsPipeline

# Load config and pipeline
with open("data/config.json") as f:
    config = json.load(f)
pipeline = NewsPipeline(config)
df, recs = pipeline.run_full_pipeline()

# Show first 2 rows of the DataFrame
print(df[['articleId','title','sentiment','cluster']].head(2))

# Show top 2 recommendations for the first 2 articles only
for k in list(recs.keys())[:2]:  # first 2 articles
    print(f"\nArticle {k} recommendations (top 2):")
    for a in recs[k][:2]:       # top 2 recommendations
        print({
            'articleId': a['articleId'],
            'title': a['title'],
            'summary': (a['summary'][:50] + '...') if len(a['summary']) > 50 else a['summary'],
            'keywords': a['keywords']
        })


import json
from src.news_pipeline import NewsPipeline

# Load config and pipeline
with open("data/config.json") as f:
    config = json.load(f)
pipeline = NewsPipeline(config)
df, recs = pipeline.run_full_pipeline()

# Show first 2 rows of the DataFrame
print(df[['articleId','title','sentiment','cluster']].head(2))

# Show top 2 recommendations for the first 2 articles only
for k in list(recs.keys())[:2]:  # first 2 articles
    print(f"\nArticle {k} recommendations (top 2):")
    for a in recs[k][:2]:       # top 2 recommendations
        print({
            'articleId': a['articleId'],
            'title': a['title'],
            'summary': (a['summary'][:50] + '...') if len(a['summary']) > 50 else a['summary'],
            'keywords': a['keywords']
        })


