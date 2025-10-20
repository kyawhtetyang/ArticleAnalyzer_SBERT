import json, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, render_template, request
from src.pipeline import full_pipeline
from app.api import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp)

with open("data/config.json") as f:
    config = json.load(f)

df, recs = full_pipeline(config)

@app.route("/")
def index():
    return render_template("index.html", articles=df.to_dict(orient="records"))

@app.route("/analysis", methods=["POST"])
def analysis():
    article_id = int(request.form.get("articleId"))
    if article_id not in df['articleId'].values:
        return "Invalid articleId", 400
    article = df[df['articleId']==article_id].iloc[0]
    article_recs = recs[article_id]
    return render_template("analysis.html", article=article, recommendations=article_recs)

if __name__ == "__main__":
    app.run(debug=True)

