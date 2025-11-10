from flask import Flask, render_template, request, jsonify
from src.news_pipeline import NewsPipeline
import json
import pandas as pd

app = Flask(__name__)

# ------------------ INITIALIZE PIPELINE ------------------
with open("data/config.json") as f:
    config = json.load(f)

pipeline = NewsPipeline(config)
df, recs = pipeline.run_full_pipeline()

def get_cluster_summary(df):
    """Group articles by cluster."""
    return df.groupby('cluster')[['articleId', 'title']].apply(
        lambda x: x.to_dict(orient='records')
    ).to_dict()

clusters_summary = get_cluster_summary(df)

# ------------------ ROUTES ------------------

@app.route("/")
def index():
    """Homepage: list all news articles."""
    return render_template("index.html", articles=df.to_dict(orient="records"))

@app.route("/analysis", methods=["POST"])
def analysis():
    """Analyze single article with summary, NER, sentiment, recs."""
    article_id = int(request.form.get("articleId"))
    if article_id not in df['articleId'].values:
        return "Invalid articleId", 400
    article = df[df['articleId'] == article_id].iloc[0]
    article_recs = recs[article_id]
    return render_template("analysis.html", article=article, recommendations=article_recs)

@app.route("/clusters")
def clusters():
    """Show article clusters (KMeans)."""
    return render_template("clusters.html", clusters=clusters_summary)

# ------------------ API ENDPOINTS ------------------

@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.json
    article_id = data.get("articleId")
    if article_id not in df['articleId'].values:
        return jsonify({"error": "Invalid articleId"}), 400
    article = df[df['articleId'] == article_id].iloc[0]
    article_recs = recs[article_id]
    return jsonify({"article": article.to_dict(), "recommendations": article_recs})

@app.route("/api/recommend", methods=["POST"])
def api_recommend():
    data = request.json
    article_id = data.get("articleId")
    if article_id not in recs:
        return jsonify({"error": "Invalid articleId"}), 400
    return jsonify({"recommendations": recs[article_id]})

@app.route("/api/clusters", methods=["GET"])
def api_clusters():
    """Return cluster structure as JSON."""
    cluster_data = {
        int(k): [{"articleId": x["articleId"], "title": x["title"]} for x in v]
        for k, v in clusters_summary.items()
    }
    return jsonify({"clusters": cluster_data})

# ------------------ MAIN ------------------
if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, request, jsonify
from src.news_pipeline import NewsPipeline
import json
import pandas as pd

app = Flask(__name__)

# ------------------ INITIALIZE PIPELINE ------------------
with open("data/config.json") as f:
    config = json.load(f)

pipeline = NewsPipeline(config)
df, recs = pipeline.run_full_pipeline()

def get_cluster_summary(df):
    """Group articles by cluster."""
    return df.groupby('cluster')[['articleId', 'title']].apply(
        lambda x: x.to_dict(orient='records')
    ).to_dict()

clusters_summary = get_cluster_summary(df)

# ------------------ ROUTES ------------------

@app.route("/")
def index():
    """Homepage: list all news articles."""
    return render_template("index.html", articles=df.to_dict(orient="records"))

@app.route("/analysis", methods=["POST"])
def analysis():
    """Analyze single article with summary, NER, sentiment, recs."""
    article_id = int(request.form.get("articleId"))
    if article_id not in df['articleId'].values:
        return "Invalid articleId", 400
    article = df[df['articleId'] == article_id].iloc[0]
    article_recs = recs[article_id]
    return render_template("analysis.html", article=article, recommendations=article_recs)

@app.route("/clusters")
def clusters():
    """Show article clusters (KMeans)."""
    return render_template("clusters.html", clusters=clusters_summary)

# ------------------ API ENDPOINTS ------------------

@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.json
    article_id = data.get("articleId")
    if article_id not in df['articleId'].values:
        return jsonify({"error": "Invalid articleId"}), 400
    article = df[df['articleId'] == article_id].iloc[0]
    article_recs = recs[article_id]
    return jsonify({"article": article.to_dict(), "recommendations": article_recs})

@app.route("/api/recommend", methods=["POST"])
def api_recommend():
    data = request.json
    article_id = data.get("articleId")
    if article_id not in recs:
        return jsonify({"error": "Invalid articleId"}), 400
    return jsonify({"recommendations": recs[article_id]})

@app.route("/api/clusters", methods=["GET"])
def api_clusters():
    """Return cluster structure as JSON."""
    cluster_data = {
        int(k): [{"articleId": x["articleId"], "title": x["title"]} for x in v]
        for k, v in clusters_summary.items()
    }
    return jsonify({"clusters": cluster_data})

# ------------------ MAIN ------------------
if __name__ == "__main__":
    app.run(debug=True)


