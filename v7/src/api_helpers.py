def validate_article_id(df, article_id):
    if article_id not in df['articleId'].values:
        raise ValueError("Invalid articleId")
    return df[df['articleId']==article_id].iloc[0]

