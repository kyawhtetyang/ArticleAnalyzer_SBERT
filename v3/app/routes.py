import os, sys, json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request
from pipelines.pipeline import full_pipeline

app = Flask(__name__)

with open("data/config.json") as f:
    config = json.load(f)

df = full_pipeline(config)

@app.route("/")
def index():
    return render_template("index.html", articles=df.to_dict(orient="records"))

@app.route("/sentiment", methods=["POST"])
def sentiment():
    article_id = int(request.form.get("articleId"))
    article = df[df['articleId']==article_id].iloc[0]
    return render_template("sentiment.html", article=article)

@app.route("/ner", methods=["POST"])
def ner():
    article_id = int(request.form.get("articleId"))
    article = df[df['articleId']==article_id].iloc[0]
    return render_template("ner.html", article=article)

@app.route("/summary", methods=["POST"])
def summary():
    article_id = int(request.form.get("articleId"))
    article = df[df['articleId']==article_id].iloc[0]
    return render_template("summary.html", article=article)

@app.route("/keywords", methods=["POST"])
def keywords():
    article_id = int(request.form.get("articleId"))
    article = df[df['articleId']==article_id].iloc[0]
    return render_template("keywords.html", article=article)

if __name__ == "__main__":
    app.run(debug=True)

