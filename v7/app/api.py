from flask import Blueprint, request, jsonify
import json
from src.pipeline import full_pipeline
from src.api_helpers import validate_article_id

api_bp = Blueprint('api', __name__)

with open("data/config.json") as f:
    config = json.load(f)

df, recs = full_pipeline(config)

@api_bp.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.json
    article_id = data.get("articleId")
    try:
        article = validate_article_id(df, article_id)
        article_recs = recs[article_id]
        return jsonify({"article": article.to_dict(), "recommendations": article_recs})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@api_bp.route("/api/recommend", methods=["POST"])
def api_recommend():
	data = request.json
	article_id = data.get("articleId")
	if article_id not in recs:
	    return jsonify({"error": "Invalid articleId"}), 400
	return jsonify({"recommendations": recs[article_id]})

