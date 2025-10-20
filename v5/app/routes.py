import json, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request
from src.nlp_utils import get_top_n_similar
from src.pipeline import full_pipeline

app = Flask(__name__)

with open("data/config.json") as f:
    config = json.load(f)

df, sim_matrix = full_pipeline(config)

@app.route("/")
def index():
    return render_template("index.html", articles=df.to_dict(orient="records"))

@app.route("/analysis", methods=["POST"])
def analysis():
    article_id = int(request.form.get("articleId"))
    if article_id not in df['articleId'].values:
        return "Invalid articleId", 400
    article = df[df['articleId']==article_id].iloc[0]
    return render_template("analysis.html", article=article)

@app.route("/recommend", methods=["POST"])
def recommend():
    article_id = int(request.form.get("articleId"))
    if article_id not in df['articleId'].values:
        return "Invalid articleId", 400
    idx = df.index[df['articleId']==article_id][0]
    top_indices, scores = get_top_n_similar(sim_matrix, idx, top_n=config.get("top_n",3))
    recs = df.iloc[top_indices][['articleId','title','summary','keywords']].to_dict(orient="records")
    return render_template("recommend.html", article=df.iloc[idx], recs=recs)

if __name__ == "__main__":
    app.run(debug=True)

