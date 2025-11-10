import pytest
from src.news_pipeline import NewsPipeline
import json

with open("data/config.json") as f:
    config = json.load(f)

pipeline = NewsPipeline(config)

def test_pipeline_run():
    df, recs = pipeline.run_full_pipeline()
    assert not df.empty
    assert isinstance(recs, dict)
    for article_id, rec_list in recs.items():
        assert isinstance(rec_list, list)


import pytest
from src.news_pipeline import NewsPipeline
import json

with open("data/config.json") as f:
    config = json.load(f)

pipeline = NewsPipeline(config)

def test_pipeline_run():
    df, recs = pipeline.run_full_pipeline()
    assert not df.empty
    assert isinstance(recs, dict)
    for article_id, rec_list in recs.items():
        assert isinstance(rec_list, list)


